# Release procedure

## Repository visibility and ownership

Use the dedicated organization repository `bharat-law/bharat-law-skills`. It can be private while preparing and reviewing the package, but Claude requires it to be public before its plugin listing goes live. The BFF service remains in its separate private repository.

This release uses a protected `release` branch and deliberate manual publishing. Publish that branch publicly before the directory-ready BFF deployment and portal validation, because the advertised public documentation URL is:

`https://github.com/bharat-law/bharat-law-skills/blob/release/docs/setup.md`

Protect the branch using the organization's normal reviewed-change controls. Publishing GitHub contents and submitting the two Claude listings are operator actions; they are not implied by a local package build.

The prepared local repository starts on `main` with an `origin` URL for the intended organization repository. Review and commit the package, create `release` at that reviewed commit, and push the two branches after creating the GitHub repository. Keep generated plugin ZIP archives outside the source repository. To test before listing, upload a ZIP of the plugin files through **Customize → Plugins → Add → Upload plugin**, excluding `.git`.

## Validate the candidate

1. Check `.claude-plugin/plugin.json`, root `.mcp.json`, each skill's name/description frontmatter, and local Markdown references. Keep the MCP URL identical to the connector listing.
2. Run `claude plugin validate .` from the package root with the official Claude CLI. Resolve reported errors. Do not treat this as live authentication or portal validation.
3. Inspect the complete file inventory for secrets, personal/client data, unused files, symlinks, unnecessary binaries, unfinished content, and claims not supported by the public tool catalogue. The package contains Markdown/JSON and its existing official brand icon, apart from ordinary repository metadata.
4. Run the [behavior evaluations](../evals/grading.md) and retain actual results privately with the tested plugin/server versions. Controlled runs can save work and use credits; use an appropriately populated test account.
5. Test the deployed connector's full 18-tool inventory, OAuth lifecycle, access boundaries, actionable errors, bounded content, operation recovery, and public streaming. Then run Claude portal validation for both submissions.

## Publish and pair

Use one long-term company Claude organization for the **MCP connector** and **Plugin bundle** submissions. The GitHub account connected for the plugin must have push access. Select this repository and its protected `release` branch. Both listings use `https://api.bharat.law/mcp`.

Provide private reviewer access and company-specific declarations in the portal. Review the permanent connector slug, documentation link, final previews, tool tests, and compliance attestations before submitting. Public source availability does not remove account authentication or hosted-service entitlements.

## Updates

For each reviewed update, increment the manifest version, update `CHANGELOG.md`, rerun checks appropriate to the change, and publish through the tracked branch deliberately. Do not let ordinary development commits become automatic releases. Revert the release branch to the last reviewed compatible package if a regression requires rollback, and use the portal's available controls to halt an affected release.

Add the latest-order skill only after a real public MCP capability can identify, retrieve, and read the authorized matter's order with adequate date/freshness semantics. Authenticate and test Claude Code separately before advertising support.

## Brand asset provenance

`.claude-plugin/icon.png` is the existing Bharat Law app icon copied unchanged from the iOS app's `AppIcon-512@2x.png` asset. It is a 1024 × 1024 PNG. No new artwork or image transformation is introduced by this package.
