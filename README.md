# Bharat Law for Claude

Use your Bharat Law account in Claude to check Indian legal answers, examine citations, and find recorded court hearings. This plugin bundles three skills with the remote Bharat Law MCP connector at `https://api.bharat.law/mcp`.

## Included skills

| Skill | Example request | Result |
| --- | --- | --- |
| `bharat-law-verify-legal-answer` | “Verify the Indian legal claims in this answer and show the evidence for each correction.” | Claim-level findings, source passages, qualifications, and corrections. |
| `bharat-law-check-citation` | “Check whether this Indian judgment citation exists and supports the proposition beside it.” | Separate findings on identity, quotation, support, applicability, and known treatment. |
| `bharat-law-next-hearing` | “Find the recorded next hearing for my subscribed matter; ask me to choose if more than one matches.” | Identified matter, recorded listing, source freshness, and check time. |

These skills do not promise universal court coverage or establish unknown legal treatment. Latest-order retrieval is not currently available.

## Connect and use

Follow [setup](docs/setup.md) to connect with your existing Bharat Law login. No API key or OAuth client details are needed. Available features depend on your account permissions, entitlements, ready documents, source coverage, and credits.

## Documentation

- [Setup and prerequisites](docs/setup.md)
- [Permissions and data handling](docs/permissions-and-data.md)
- [Troubleshooting](docs/troubleshooting.md)

## Package and support

This package contains Markdown, JSON, and the Bharat Law brand icon, with no hooks, executable installation steps, runtime dependencies, credentials, or customer records. The remote service is hosted by Bharat Law; its implementation is not included here.

Support: [support@bharat.law](mailto:support@bharat.law). Privacy: [Bharat Law privacy policy](https://bharat.law/legal/privacy-policy). Report vulnerabilities using [SECURITY.md](SECURITY.md).

The MIT license applies to this plugin's files. It does not grant rights to service access, retrieved legal sources, customer documents, or third-party content.
