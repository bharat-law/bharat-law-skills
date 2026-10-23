# Connect Bharat Law to Claude

Use your existing Bharat Law account to work with authorized cases, conversations, documents, legal sources, and recorded court matters from Claude.

## Before connecting

- Have a Bharat Law account with access to the workspace or matters you want to use.
- Check that required documents are processed and ready. Research, fresh court retrieval, drafting, and extended workflows remain subject to account permissions, feature availability, and credits.
- Review [permissions and data handling](permissions-and-data.md), including shared saved work and the effect of workspace switching.

| Setting | Value |
| --- | --- |
| Connector name | Bharat Law |
| Remote MCP URL | `https://api.bharat.law/mcp` |
| User authentication | Sign in with your Bharat Law account using OAuth |
| Bharat Law API key | Not required |
| Support | `support@bharat.law` |
| Privacy policy | `https://bharat.law/legal/privacy-policy` |

## Published directory connection

When the listing is available, open Claude **Customize → Connectors** (or **Settings → Connectors**, depending on the client), find **Bharat Law**, and choose **Connect**. Review the disclosure, sign in to Bharat Law, and consent to the requested permissions. Your available data follows your Bharat Law account's access rules.

The connector supplies tools. The companion Bharat Law plugin adds the verification, citation-checking, and next-hearing skills. Both use the same MCP URL. Install the plugin through its Claude directory listing when available, and reuse an existing connection if Claude offers that option.

This repository is a publication candidate; these steps do not imply that either directory listing is already live.

## Pre-publication company setup

The company operator should follow [the company setup handoff](company-claude-setup.md). A URL-added custom connector needs the new Claude OAuth client ID and secret entered privately through **Use your own OAuth client** or **Advanced settings**. It does not inherit the client secret entered for a directory submission.

Ordinary end users should not obtain or distribute the company OAuth client secret. Published-directory users sign in with their own Bharat Law accounts.

## Try the connection

1. “List my Bharat Law workspaces and identify the active one.”
2. “Find my saved Bharat Law conversations so I can choose one to continue.”
3. “Find the recorded next hearing for my subscribed matter. Ask me to choose if several matters match.”
4. “Verify the Indian legal claims in the following answer. Show supporting or conflicting passages and leave unresolved points explicit.” Then provide the answer to check.

For citation checking, provide the citation and the proposition or quotation you want tested. For a hearing lookup, provide enough parties, court/bench, or case identifiers to identify the intended matter.

## Saved work and disconnection

Tell Claude to continue the same Bharat Law conversation for related follow-ups. Search and research may save work in Bharat Law; drafts and deep research can create further saved artifacts. A workspace switch also changes the workspace selected in the Bharat Law web and mobile apps.

To revoke access, sign in to Bharat Law, open **MCP connections** at `/integrations/mcp`, select the intended Claude connection, and choose **Revoke access**. Revocation stops further access through that connection. Already-submitted work may finish and use credits; saved work remains under normal workspace/case permissions. Disconnecting Claude and revoking Bharat Law access are separate account-management actions.

## Supported clients and limits

Hosted Claude is the initial authentication target. Claude Code uses a separate client identity and loopback callbacks; this package does not claim tested Code OAuth support. Other client surfaces must be tested before compatibility is advertised. Source coverage and freshness vary. A recorded hearing can change, and an unknown legal-treatment result is not confirmation that an authority is current.
