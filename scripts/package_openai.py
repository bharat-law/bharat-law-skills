#!/usr/bin/env python3
"""Validate and deterministically package the public OpenAI distribution.

The generated ZIP is a draft candidate, not evidence of live tool execution,
portal approval, or completed review requirements. Uses the Python standard library.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import re
import struct
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SCOPES = {'openid', 'email', 'profile', 'bharat-law-mcp/read', 'bharat-law-mcp/run', 'bharat-law-mcp/draft', 'bharat-law-mcp/switch_workspace'}
TOOLS = {'cancel_operation','deep_research','draft_document','get_next_hearing','get_operation','list_case_documents','list_cases','list_conversations','list_court_matters','list_operations','list_sources','list_workspaces','read_content','research','respond_to_operation','search','set_case_context','switch_workspace'}
SKILLS = {'bharat-law-verify-legal-answer', 'bharat-law-check-citation', 'bharat-law-next-hearing'}
PUBLIC_FILES = ('plugin.json','mcp.json','LICENSE','README.md','CHANGELOG.md','SECURITY.md','assets/icon.png','docs/setup.md','docs/setup-chatgpt.md','docs/permissions-and-data.md','docs/troubleshooting.md')
FORBIDDEN_KEYS = {'clientSecret','client_secret','access_token','refresh_token','id_token','password','test_credentials','reviewer_instructions','apps','hooks','headers'}
SECRET_PATTERNS = (re.compile(rb'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----'), re.compile(rb'\b(?:AKIA|ASIA)[A-Z0-9]{16}\b'), re.compile(rb'\beyJ[A-Za-z0-9_-]{12,}\.[A-Za-z0-9_-]{12,}\.[A-Za-z0-9_-]{12,}\b'))

class PackageError(ValueError):
    pass

def require(value, message):
    if not value:
        raise PackageError(message)

def load_json(root, name):
    return json.loads((root / name).read_text(encoding='utf-8'))

def check_keys(value, path='manifest'):
    if isinstance(value, dict):
        for key, item in value.items():
            require(key not in FORBIDDEN_KEYS, f'{path}: forbidden public-package field {key}')
            check_keys(item, f'{path}.{key}')
    elif isinstance(value, list):
        for item in value:
            check_keys(item, path)

def https(value):
    from urllib.parse import urlsplit
    if not isinstance(value, str):
        return False
    parsed = urlsplit(value)
    return parsed.scheme == 'https' and bool(parsed.hostname) and not parsed.username and not parsed.password and not parsed.fragment

def selected_files(root):
    paths = [root / name for name in PUBLIC_FILES]
    require((root / 'skills').is_dir(), 'skills/ is required')
    paths.extend(path for path in (root / 'skills').rglob('*') if path.is_file() or path.is_symlink())
    names = set()
    for path in paths:
        require(path.is_file(), f'Missing public file: {path.relative_to(root)}')
        relative = path.relative_to(root)
        require(not path.is_symlink() and not any(parent.is_symlink() for parent in path.parents if parent != root.parent), f'Symlink is not allowed: {relative}')
        require(path.resolve().is_relative_to(root.resolve()), f'File escapes package root: {relative}')
        require(all(not part.startswith('.') for part in relative.parts), f'Hidden package path: {relative}')
        require(path.suffix.lower() not in {'.pem','.key','.p12','.pfx','.zip','.sh','.exe','.py','.js','.mjs'}, f'Executable or private artifact: {relative}')
        names.add(relative.as_posix())
    return sorted(names)

def validate(root):
    root = root.resolve()
    manifest, mcp, fixtures = (load_json(root, name) for name in ('plugin.json','mcp.json','docs/openai-review-cases.json'))
    check_keys(manifest)
    check_keys(mcp)
    require(manifest.get('$schema') == 'https://agent-plugins.org/schemas/1.0.0/plugin.schema.json', 'Wrong portable plugin schema')
    require(manifest.get('name') == 'bharat-law' and manifest.get('version') == '0.1.5', 'Wrong OpenAI package identity/version')
    require(manifest.get('author', {}).get('name') == 'Bharat Technologies, Inc.', 'Wrong publisher')
    extension = manifest['extensions']['com.openai']
    interface = extension['interface']
    require(interface['displayName'] == 'Bharat Law' and interface['category'] == 'Productivity', 'Wrong listing name/category')
    require(0 < len(interface['shortDescription']) <= 30 and len(interface['longDescription']) <= 4000, 'Listing length exceeds limits')
    require(interface['shortDescription'] == 'Indian legal research', 'Wrong subtitle')
    for field in ('websiteURL','supportURL','privacyPolicyURL','termsOfServiceURL'):
        require(https(interface.get(field)), f'{field} must be a public HTTPS URL')
    require(interface['supportURL'].endswith('/release/docs/troubleshooting.md'), 'Wrong support page')
    require(extension['publication'].get('countries') == [], 'Worldwide targeting must be explicit')
    require('screenshots' not in interface, 'No UI screenshots belong in this release')
    for field in ('composerIcon','logo'):
        require(interface.get(field) == './assets/icon.png', f'{field} must use included brand icon')
    icon = (root / 'assets/icon.png').read_bytes()
    require(icon[:8] == b'\x89PNG\r\n\x1a\n', 'Brand icon must be PNG')
    width, height = struct.unpack('>II', icon[16:24])
    require(width == height and 48 <= width <= 4096 and len(icon) <= 5 * 1024 * 1024, 'Brand icon dimensions or size invalid')
    require(mcp.get('$schema') == 'https://agent-plugins.org/schemas/1.0.0/mcp.schema.json', 'Wrong portable MCP schema')
    require(set(mcp['mcpServers']) == {'bharat-law'}, 'Exactly one Bharat Law server is required')
    server = mcp['mcpServers']['bharat-law']
    require(server.get('type') == 'streamable-http' and server.get('url') == 'https://api.bharat.law/mcp', 'Wrong public server/transport')
    auth = server['extensions']['com.openai']['auth']
    require(auth.get('type') == 'oauth', 'OAuth is required')
    require(auth['client'] == {'mode':'provided','clientId':'6s04rja4c7kfglfa19nd4b9oej','tokenEndpointAuthMethod':'none'}, 'Use the verified deployed public ChatGPT OAuth client')
    require(set(auth['baseScopes']) == SCOPES and len(auth['baseScopes']) == len(SCOPES), 'Declare all seven scopes once')
    require(auth.get('resource') == server['url'], 'Wrong OAuth resource')
    require(auth.get('authorizationUrl') == 'https://api.bharat.law/oauth/authorize' and auth.get('tokenUrl') == 'https://api.bharat.law/oauth/token', 'Wrong OAuth endpoints')
    require(auth.get('oidcEnabled') is True, 'Explicit OIDC configuration is required')
    require(auth.get('oidcConfigurationUrl') == 'https://cognito-idp.us-east-1.amazonaws.com/us-east-1_UQcc1Aq0k/.well-known/openid-configuration', 'OIDC discovery must match the actual Cognito issuer')
    require(auth.get('oidcUserinfoEndpoint') == 'https://api.bharat.law/oauth/userinfo', 'Wrong UserInfo proxy')
    require(auth.get('oidcScopesSupported') == ['openid','email','profile'], 'Wrong OIDC scopes')
    require(fixtures.get('schema_version') == 1 and fixtures.get('execution_status') in {'not_run','run'}, 'Review fixture status must be explicit')
    cases = fixtures['cases']
    require([c['id'] for c in cases] == ['P1','P2','P3','P4','P5','N1','N2','N3'], 'Review cases must retain stable IDs')
    review = extension['review']
    require(review.get('commerce') is False, 'No commerce in this release')
    for kind, count in (('positive', 5), ('negative', 3)):
        actual = review['test_cases'][kind]
        expected = [{key: ', '.join(c[key]) if key == 'tools_triggered' else c[key] for key in ('description','prompt','tools_triggered','expected_behavior')} for c in cases if c['kind'] == kind]
        require(len(actual) == count and actual == expected, f'{kind} manifest review cases drifted from fixtures')
        for c in (c for c in cases if c['kind'] == kind):
            require(c.get('checks') and all(isinstance(check, str) and check for check in c['checks']), f'{c["id"]}: empty evidence checks')
            require(set(c['tools_triggered']) <= TOOLS, f'{c["id"]}: unknown tool')
    require({p.parent.name for p in (root/'skills').glob('*/SKILL.md')} == SKILLS, 'Exactly three approved skills are required')
    names = selected_files(root)
    for name in names:
        data = (root / name).read_bytes()
        require(not any(pattern.search(data) for pattern in SECRET_PATTERNS), f'Possible private credential in {name}')
    gates = []
    if fixtures['execution_status'] == 'not_run':
        gates.append('Eight ChatGPT review cases have not been executed and evidenced.')
    if not https(review.get('demo_recording_url')):
        gates.append('Accessible walkthrough recording URL has not been supplied.')
    gates.extend(['Reviewer account and private portal credentials must be verified.', 'Production deployment, callback, domain verification, public documentation, and portal scans must be checked.', 'Company operator must resolve policy eligibility and complete attestations.'])
    return manifest, names, gates

def build(root, output):
    manifest, names, gates = validate(root)
    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for name in names:
            info = zipfile.ZipInfo(name, date_time=(2026,10,23,0,0,0))
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            info.compress_type = zipfile.ZIP_DEFLATED
            archive.writestr(info, (root / name).read_bytes(), compresslevel=9)
    return {'package_valid':True,'version':manifest['version'],'artifact_kind':'draft_candidate','path':str(output.resolve()),'sha256':hashlib.sha256(output.read_bytes()).hexdigest(),'files':len(names),'review_ready':False,'remaining_gates':gates}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Validate source without creating a ZIP')
    parser.add_argument('--root', type=Path, default=ROOT, help=argparse.SUPPRESS)
    parser.add_argument('--output', type=Path, help='Draft ZIP destination (default: dist/bharat-law-openai-0.1.5-draft.zip)')
    args = parser.parse_args()
    try:
        root = args.root.resolve()
        if args.check:
            manifest, names, gates = validate(root)
            result = {'package_valid':True,'version':manifest['version'],'files':len(names),'review_ready':False,'remaining_gates':gates}
        else:
            result = build(root, args.output or root/'dist/bharat-law-openai-0.1.5-draft.zip')
        print(json.dumps(result,indent=2))
    except (PackageError, KeyError, OSError, ValueError, TypeError) as error:
        print(f'Package validation failed: {error}', file=sys.stderr)
        return 1
    return 0

if __name__ == '__main__':
    sys.exit(main())
