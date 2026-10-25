# Bharat Law for Claude

Research Indian law, verify answers and citations, and check recorded court hearings in Claude. Connect your existing Bharat Law account to work with your permitted cases, documents, and saved conversations.

The connector can generate cited research and legal drafts when requested. Three guided skills help you verify an answer, check a citation, or find a recorded hearing. Available features depend on your account permissions, source coverage, ready documents, and credits. Research and drafting save work in Bharat Law; legal lookup does not save a search or conversation.

## Included skills

| Guided workflow | Example request | Result |
| --- | --- | --- |
| Verify a legal answer | “Verify the Indian legal claims in this answer and show the evidence for each correction.” | Claim-level findings, source passages, qualifications, and corrections. |
| Check a citation | “Check whether this Indian judgment citation exists and supports the proposition beside it.” | Separate findings on identity, quotation, support, applicability, and known treatment. |
| Find a recorded hearing | “Find the recorded next hearing for my subscribed matter; ask me to choose if more than one matches.” | Identified matter, recorded listing, source freshness, and check time. |

Legal lookup returns up to three matches and available source text through Bharat Law links. Assess only the evidence returned: a summary cannot verify an exact quotation from the original judgment. Missing text, incomplete coverage, and unknown legal treatment remain unresolved. Legal lookup does not save a search or conversation.

When a Bharat Law match is unavailable, the verification skills may use the assistant's web tools to consult official court sites or other public sources. These lookups use only authority identifiers, with external evidence labelled separately; unrelated private matter or document content must not be sent to those sites. News reports do not establish a judgment's holding.

These skills do not promise universal court coverage. Latest-order retrieval is not currently available, and recorded hearings can change. Review generated answers and drafts before relying on them, filing, or sharing them.

See [worked examples](docs/examples.md) for what to provide and how to read the results. Skill command identifiers remain `bharat-law-verify-legal-answer`, `bharat-law-check-citation`, and `bharat-law-next-hearing`.

## Connect and use

Follow [Claude setup](docs/setup.md) to connect with your existing Bharat Law login. No Bharat Law API key is required. Available features depend on account permissions, entitlements, ready documents, source coverage, and credits.

Read [permissions and data handling](docs/permissions-and-data.md) for information about saved-work sharing, credits, workspace switching, and revocation. See [troubleshooting](docs/troubleshooting.md) for connection and usage problems.

## Support

Support: [MCP troubleshooting and contact guide](https://github.com/bharat-law/bharat-law-skills/blob/release-claude/docs/troubleshooting.md) or [support@bharat.law](mailto:support@bharat.law). Privacy: [Bharat Law privacy policy](https://bharat.law/legal/privacy-policy). Report vulnerabilities using [SECURITY.md](SECURITY.md).

The MIT license applies to package files. It does not grant rights to service access, retrieved legal sources, customer documents, or third-party content.
