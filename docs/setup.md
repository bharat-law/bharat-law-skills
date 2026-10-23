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

## Connect from the Claude directory

If Bharat Law is not yet available in the directory, use the custom connector instructions below.

When the listing is available, open Claude **Customize → Connectors** (or **Settings → Connectors**, depending on the client), find **Bharat Law**, and choose **Connect**. Review the disclosure, sign in to Bharat Law, and consent to the requested permissions. Your available data follows your Bharat Law account's access rules.

The connector supplies tools. The companion Bharat Law plugin adds the verification, citation-checking, and next-hearing skills. Both use the same MCP URL. Install the plugin through its Claude directory listing, and reuse an existing connection if Claude offers that option.

## Add as a custom connector

You can also add the connector by URL: **Customize → Connectors → Add custom connector**, name it **Bharat Law**, and enter `https://api.bharat.law/mcp`. Leave the OAuth client ID and secret fields empty; Claude registers itself automatically and you sign in with your own Bharat Law account.

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

The connector supports Claude on the web, desktop, mobile, and Cowork. Claude Code is not currently supported. Source coverage and freshness vary. A recorded hearing can change, and an unknown legal-treatment result is not confirmation that an authority is current.
