# Bharat Law for connected assistants

Use your Bharat Law account to check Indian legal answers, examine citations, and find recorded court hearings. The package bundles three skills with the remote Bharat Law MCP connector at `https://api.bharat.law/mcp`.

## Included skills

| Skill | Example request | Result |
| --- | --- | --- |
| `bharat-law-verify-legal-answer` | “Verify the Indian legal claims in this answer and show the evidence for each correction.” | Claim-level findings, source passages, qualifications, and corrections. |
| `bharat-law-check-citation` | “Check whether this Indian judgment citation exists and supports the proposition beside it.” | Separate findings on identity, quotation, support, applicability, and known treatment. |
| `bharat-law-next-hearing` | “Find the recorded next hearing for my subscribed matter; ask me to choose if more than one matches.” | Identified matter, recorded listing, source freshness, and check time. |

Legal lookup uses live Find and returns the top three matches as Markdown. Judgment results include details and headnotes; sections include full text; other statute targets include a description and a link to the original in Bharat Law. Verification reads available database content through those authenticated links. Judgment checks use stored details/headnotes, so exact quotations from the original judgment remain unresolved; full section text and available stored statute text support checks within their returned coverage. Lookup does not save a search or conversation.

These skills do not promise universal court coverage or establish unknown legal treatment. Latest-order retrieval is not currently available.

## Connect and use

Follow [Claude setup](docs/setup.md) or [ChatGPT setup](docs/setup-chatgpt.md). Directory installation uses your existing Bharat Law login without an API key. Available features depend on account permissions, entitlements, ready documents, source coverage, and credits.

The Claude compatibility manifest remains version **0.1.4**, matching its current submission. The portable OpenAI manifest is version **0.1.5**, initially a draft submission candidate. Packaging does not establish approval, production deployment, or successful live tests on a particular client. See [permissions and data handling](docs/permissions-and-data.md) and [troubleshooting](docs/troubleshooting.md).

## Distribution and support

The installed distribution contains Markdown, JSON, and the Bharat Law icon, with no hooks, executable installation steps, runtime dependencies, credentials, or customer records. Source-repository authoring tools are separate from the submission ZIP. The hosted service implementation is not included.

Maintainers can validate and create the OpenAI draft ZIP with `python3 scripts/package_openai.py --check` and `python3 scripts/package_openai.py`. The build uses an explicit public-file allowlist and reports remaining review gates. It does not submit, deploy, or assert that review cases have passed. Review fixture definitions live in `docs/openai-review-cases.json`; execution evidence belongs outside the public package.

Support: [support@bharat.law](mailto:support@bharat.law). Privacy: [Bharat Law privacy policy](https://bharat.law/legal/privacy-policy). Report vulnerabilities using [SECURITY.md](SECURITY.md).

The MIT license applies to package files. It does not grant rights to service access, retrieved legal sources, customer documents, or third-party content.
