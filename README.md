# Bharat Law for Claude

Use your Bharat Law account in Claude to check Indian legal answers, examine citations, and find recorded court hearings. This plugin bundles three skills with the remote [Bharat Law MCP connector](https://api.bharat.law/mcp).

Version 0.1.0 is a publication candidate. Creating this local package does not publish a GitHub repository or a Claude directory listing.

## Included skills

| Skill | Example request | Result |
| --- | --- | --- |
| `bharat-law-verify-legal-answer` | “Verify the Indian legal claims in this answer and show the evidence for each correction.” | Claim-level findings, source passages, qualifications, and corrections. |
| `bharat-law-check-citation` | “Check whether this Indian judgment citation exists and supports the proposition beside it.” | Separate findings on identity, quotation, support, applicability, and known treatment. |
| `bharat-law-next-hearing` | “Find the recorded next hearing for my subscribed matter; ask me to choose if more than one matches.” | Identified matter, recorded listing, source freshness, and check time. |

Latest-order retrieval is deferred: the current public MCP tool catalogue does not expose a latest-order capability. These skills do not promise universal court coverage or establish unknown legal treatment.

## Connect and use

Follow [setup](docs/setup.md) to connect `https://api.bharat.law/mcp` with your existing Bharat Law login. No Bharat Law API key is required. Available features depend on your account permissions, entitlements, ready documents, source coverage, and credits.

The connector and plugin are separate Claude directory submissions. The connector supplies tools; the plugin supplies workflow guidance and references the identical server URL. Hosted Claude is the initial connection target. Claude Code and other client surfaces require separate authentication testing before compatibility is advertised.

## Documentation

- [Setup and prerequisites](docs/setup.md)
- [Permissions and data handling](docs/permissions-and-data.md)
- [Troubleshooting](docs/troubleshooting.md)
- [Connector listing content](docs/connector-listing.md)
- [Company Claude setup handoff](docs/company-claude-setup.md)
- [Release and publication procedure](docs/release.md)
- [Local validation and remaining live checks](docs/validation.md)
- [Evaluation cases](evals/cases.json) and [grading](evals/grading.md)

## Package and support

This package contains Markdown, JSON, and the existing Bharat Law brand icon, with no hooks, executable installation steps, runtime dependencies, credentials, or private case records. The remote service remains hosted by Bharat Law; its implementation is not included here.

Support: [support@bharat.law](mailto:support@bharat.law). Privacy: [Bharat Law privacy policy](https://bharat.law/legal/privacy-policy). Report vulnerabilities using [SECURITY.md](SECURITY.md).

The MIT license applies to this plugin's files. It does not grant rights to service access, retrieved legal sources, customer documents, or third-party content.
