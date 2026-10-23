# Claude connector listing content

Use this copy in the company-owned Claude connector submission. The connector and companion plugin are separate submissions under the same long-term Claude organization. The permanent slug should be reviewed before final submission.

## Connection and listing fields

| Field | Value |
| --- | --- |
| MCP server URL | `https://api.bharat.law/mcp` |
| Name | Bharat Law |
| Slug | `bharat-law` |
| Category | Legal |
| Author name | Bharat Technologies, Inc. |
| Author URL | `https://bharat.law` |
| Support | `support@bharat.law` |
| Privacy policy | `https://bharat.law/legal/privacy-policy` |
| Icon | Prefer the server URL's favicon; check any existing custom icon in the portal. |

**One-liner**

Research Indian law, check court hearings, and work with your Bharat Law cases and documents in Claude.

**Description**

Connect your existing Bharat Law account to Claude to search available Indian legal sources, generate cited research, run extended research or drafting when requested, and work with authorized cases, documents, and saved conversations. Find subscribed or authorized workspace court matters and check their recorded next hearing, with source freshness and coverage limitations kept explicit.

Continue related conversations across Bharat Law and Claude. Search and research can save work in Bharat Law; drafts and extended workflows may create additional saved artifacts. Saved work follows workspace and case permissions. Changing the active workspace also changes the workspace selected in the Bharat Law web and mobile apps.

A Bharat Law account is required. Available features depend on permissions, entitlements, ready documents, source coverage, and credits. Court listings can change; missing records and unknown legal treatment remain unresolved. The companion plugin adds guided legal-answer verification, citation checking, and next-hearing workflows. Latest-order retrieval is not included in the current MCP tool catalogue.

**Documentation**

Use [the public setup guide](https://github.com/bharat-law/bharat-law-skills/blob/release/docs/setup.md): `https://github.com/bharat-law/bharat-law-skills/blob/release/docs/setup.md`. Publish the public `release` branch before using this URL in the portal or deploying metadata that advertises it. The authenticated `/developer` and `/integrations/mcp` pages are account-management destinations, not public documentation.

## Three use cases and example prompts

| Use case | Example prompt | Expected behavior |
| --- | --- | --- |
| Evidence-based Indian legal verification | “Verify the Indian legal claims in the answer I provide. Find supporting and conflicting evidence, show the source passages, and distinguish unresolved treatment from established findings.” | Source-backed claim assessment with corrections and evidence limits. Supply a controlled sample answer during review. |
| Citation checking | “Check this Indian judgment citation and the proposition beside it. Assess authority identity, quotation accuracy, proposition support, applicability, and known treatment separately.” | Separate evidence findings. Supply a controlled citation/proposition during review. |
| Next hearing | “Find the recorded next hearing for my subscribed matter. Ask me to select a match if there are several, and show when the data was checked and how fresh the source is.” | Correct matter selection and qualified listing information. The reviewer account must contain a suitable matter. |

## Authentication selections

Choose **Always required → OAuth sign-in → Anthropic-held client credentials → Anthropic holds a client secret**. Enter the deployed confidential directory client's ID and secret only in the portal's private fields. The hosted callback is `https://claude.ai/api/mcp/auth_callback`.

The earlier public Claude client and arbitrary CIMD/DCR identities are not the directory configuration. See [company setup](company-claude-setup.md) for deployment and private credential-entry steps.

## Data handling and reviewer fields

- Describe queries, selected facts/documents, source passages, generated results, saved-work sharing, credits, and revocation using [permissions and data handling](permissions-and-data.md).
- Legal documents can contain personal health information. Use the portal's conditional/other explanation when applicable rather than an unconditional “No.” Base all remaining answers on the actual service and source integrations.
- Explain underlying court-source integrations and rights accurately; ownership of the hosted API is not ownership of every retrieved source.
- Supply company contact details and a populated controlled reviewer account through private portal fields. Reviewer access should cover useful conversations, processed documents, court matters, and enough credits to exercise the submitted tools. No reviewer credentials belong in this repository.
- Resync the deployed catalogue and confirm 18 tools. Complete real tool tests and portal validation before checking test, launch, or compliance attestations. Do not certify tests from package validation alone.

Account ownership, private reviewer access, company declarations, and final attestations must be completed by the company operator. This file prepares the copy; it does not assert that those steps have occurred.
