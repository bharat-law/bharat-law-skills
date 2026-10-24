# Bharat Law for connected assistants

Use your Bharat Law account to check Indian legal answers, examine citations, and find recorded court hearings. The package bundles three skills with the remote Bharat Law MCP connector at `https://api.bharat.law/mcp`.

## Included skills

| Skill | Example request | Result |
| --- | --- | --- |
| `bharat-law-verify-legal-answer` | “Verify the Indian legal claims in this answer and show the evidence for each correction.” | Claim-level findings, source passages, qualifications, and corrections. |
| `bharat-law-check-citation` | “Check whether this Indian judgment citation exists and supports the proposition beside it.” | Separate findings on identity, quotation, support, applicability, and known treatment. |
| `bharat-law-next-hearing` | “Find the recorded next hearing for my subscribed matter; ask me to choose if more than one matches.” | Identified matter, recorded listing, source freshness, and check time. |

Legal lookup returns up to three matches and available source text through Bharat Law links. Assess only the evidence returned: a summary cannot verify an exact quotation from the original judgment. Missing text, incomplete coverage, and unknown legal treatment remain unresolved. Legal lookup does not save a search or conversation.

When a Bharat Law match is unavailable, the verification skills may use the assistant's web tools to consult official court sites or other public sources. These lookups use only authority identifiers, with external evidence labelled separately; unrelated private matter or document content must not be sent to those sites. News reports do not establish a judgment's holding.

These skills do not promise universal court coverage. Latest-order retrieval is not currently available, and recorded hearings can change. Review generated answers and drafts before relying on them, filing, or sharing them.

## Connect and use

Follow [Claude setup](docs/setup.md) or [ChatGPT setup](docs/setup-chatgpt.md) to connect with your existing Bharat Law login. No Bharat Law API key is required. Available features depend on account permissions, entitlements, ready documents, source coverage, and credits.

Read [permissions and data handling](docs/permissions-and-data.md) for information about saved-work sharing, credits, workspace switching, and revocation. See [troubleshooting](docs/troubleshooting.md) for connection and usage problems.

## Support

Support: [support@bharat.law](mailto:support@bharat.law). Privacy: [Bharat Law privacy policy](https://bharat.law/legal/privacy-policy). Report vulnerabilities using [SECURITY.md](SECURITY.md).

The MIT license applies to package files. It does not grant rights to service access, retrieved legal sources, customer documents, or third-party content.
