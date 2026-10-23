import importlib.util
import json
from pathlib import Path
import shutil
import tempfile
import unittest
import zipfile

spec = importlib.util.spec_from_file_location('package_openai', Path(__file__).with_name('package_openai.py'))
package = importlib.util.module_from_spec(spec)
spec.loader.exec_module(package)

class PublicPackageTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name) / 'source'
        shutil.copytree(package.ROOT, self.root, ignore=shutil.ignore_patterns('.git','dist','__pycache__'))

    def tearDown(self):
        self.temp.cleanup()

    def write_json(self, name, update):
        path = self.root/name
        data = json.loads(path.read_text())
        update(data)
        path.write_text(json.dumps(data))

    def test_draft_archive_is_reproducible_and_omits_private_authoring_files(self):
        (self.root/'.env').write_text('PRIVATE_CONFIGURATION=not-for-distribution')
        (self.root/'docs/private-reviewer-access.txt').write_text('test-private-authoring-data')
        left, right = Path(self.temp.name)/'first.zip', Path(self.temp.name)/'second.zip'
        a = package.build(self.root,left)
        b = package.build(self.root,right)
        self.assertEqual(a['sha256'],b['sha256'])
        self.assertFalse(a['review_ready'])
        self.assertEqual(a['artifact_kind'],'draft_candidate')
        with zipfile.ZipFile(left) as archive:
            names = archive.namelist()
            self.assertIn('plugin.json',names)
            self.assertIn('mcp.json',names)
            self.assertEqual(sum(n.endswith('SKILL.md') for n in names),3)
            self.assertFalse(any(n.startswith(('.','scripts/')) for n in names))
            self.assertNotIn('docs/private-reviewer-access.txt',names)
            self.assertNotIn('docs/openai-review-fixtures.md',names)
            self.assertEqual(archive.testzip(),None)

    def test_skill_symlink_cannot_exfiltrate_an_outside_file(self):
        outside = Path(self.temp.name)/'outside.md'
        outside.write_text('private content')
        (self.root/'skills/bharat-law-check-citation/leak.md').symlink_to(outside)
        with self.assertRaisesRegex(package.PackageError,'Symlink'):
            package.validate(self.root)

    def test_private_key_and_credential_files_in_skills_fail_validation(self):
        file = self.root/'skills/bharat-law-check-citation/notes.md'
        file.write_text('-----BEGIN PRIVATE KEY-----\nsynthetic test material\n')
        with self.assertRaisesRegex(package.PackageError,'Possible private credential'):
            package.validate(self.root)
        file.unlink()
        (self.root/'skills/bharat-law-check-citation/private.pem').write_text('synthetic material')
        with self.assertRaisesRegex(package.PackageError,'Executable or private artifact'):
            package.validate(self.root)

    def test_missing_assets_and_review_case_drift_are_rejected(self):
        (self.root/'assets/icon.png').unlink()
        with self.assertRaises(OSError):
            package.validate(self.root)
        shutil.copy2(package.ROOT/'assets/icon.png',self.root/'assets/icon.png')
        self.write_json('plugin.json',lambda d: d['extensions']['com.openai']['review']['test_cases']['positive'].pop())
        with self.assertRaisesRegex(package.PackageError,'review cases drifted'):
            package.validate(self.root)

    def test_secret_headers_and_incorrect_oidc_are_rejected(self):
        self.write_json('mcp.json',lambda d: d['mcpServers']['bharat-law'].update(headers={'Authorization':'synthetic'}))
        with self.assertRaisesRegex(package.PackageError,'forbidden public-package field headers'):
            package.validate(self.root)
        shutil.copy2(package.ROOT/'mcp.json',self.root/'mcp.json')
        self.write_json('mcp.json',lambda d: d['mcpServers']['bharat-law']['extensions']['com.openai']['auth'].update(oidcConfigurationUrl='https://api.bharat.law/.well-known/openid-configuration'))
        with self.assertRaisesRegex(package.PackageError,'actual Cognito issuer'):
            package.validate(self.root)

    def test_claude_manifest_and_connection_are_preserved(self):
        self.assertEqual(json.loads((self.root/'.claude-plugin/plugin.json').read_text())['version'],'0.1.4')
        self.assertEqual((self.root/'.mcp.json').read_bytes(), (package.ROOT/'.mcp.json').read_bytes())
        self.assertEqual((self.root/'.claude-plugin/icon.png').read_bytes(), (self.root/'assets/icon.png').read_bytes())

if __name__ == '__main__':
    unittest.main()
