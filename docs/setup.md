# Connect Bharat Law to Claude

Use your existing Bharat Law account to work with authorized cases, conversations, documents, legal sources, and recorded court matters from Claude.

## Before connecting

- Have a Bharat Law account with access to the workspace or matters you want to use.
- Check that documents needed for your task are ready. Research, fresh court retrieval, drafting, and extended workflows remain subject to account permissions, feature availability, and credits.
- Read [permissions and data handling](permissions-and-data.md), including saved-work sharing and the effect of workspace switching.

| Setting | Value |
| --- | --- |
| Connector name | Bharat Law |
| Remote MCP URL | `https://api.bharat.law/mcp` |
| Authentication | OAuth sign-in with your Bharat Law account |
| Bharat Law API key | Not required |
| Support | [support@bharat.law](mailto:support@bharat.law) |
| Privacy | [Bharat Law privacy policy](https://bharat.law/legal/privacy-policy) |

## Connect from the directory

When Bharat Law is available in the Claude directory, open **Customize → Connectors** or **Settings → Connectors**, find **Bharat Law**, and choose **Connect**. Review the disclosure, sign in, and consent to the requested permissions. Your available data follows your Bharat Law account's access rules.

The connector supplies tools. The companion Bharat Law plugin adds the verification, citation-checking, and next-hearing skills. Install it through its Claude directory listing, and reuse an existing connection if Claude offers that option.

If the directory connection is unavailable, use the custom connector instructions below.

## Add as a custom connector

Open **Customize → Connectors → Add custom connector**, name it **Bharat Law**, and enter `https://api.bharat.law/mcp`. Leave the OAuth client ID and secret fields empty, then sign in with your Bharat Law account.

## Try the connection

1. “List my Bharat Law workspaces and identify the active one.”
2. “Find my saved Bharat Law conversations so I can choose one to continue.”
3. “Find the recorded next hearing for my subscribed matter. Ask me to choose if several matters match.”
4. “Verify the Indian legal claims in this answer and show supporting or conflicting passages.” Then provide the answer.
5. “Check this Indian judgment citation and the proposition beside it.” Then provide both.

For citation checking, include the Supreme Court or named High Court for a judgment, or the provision with its Act name for a statute. Lookup returns up to three matches. Assess only the returned evidence; a summary cannot verify an exact quotation from the original judgment. For hearing lookup, provide enough parties, court/bench, or case identifiers to identify the intended matter.

Legal lookup does not save searches or conversations. Separately requested research saves answers; drafting and deep research can save additional work and use credits. Ask to continue the same Bharat Law conversation for related follow-ups. Extended research requires your intent. Switching workspace also changes the workspace selected in Bharat Law web and mobile apps.

## Disconnect or revoke

Disconnect Bharat Law in Claude when you no longer want that account connected. To revoke Bharat Law access, sign in to Bharat Law, open **MCP connections** at `/integrations/mcp`, select the intended Claude connection, and choose **Revoke access**. Disconnecting in Claude and revoking in Bharat Law are separate actions.

Revocation blocks further access and token refresh for that connection. Already-submitted work may finish and use credits; saved work remains under normal workspace/case permissions and retention rules. Do not restart accepted work merely because a connection was interrupted.

## Supported clients and limits

The connector supports Claude on the web, desktop, mobile, and Cowork. Claude Code is not currently supported. Source coverage and freshness vary. A recorded hearing can change; no recorded date does not establish that no hearing is scheduled. Missing evidence and unknown legal treatment remain unresolved. Review generated answers and drafts before relying on them, filing, or sharing them. Latest-order retrieval is not currently available.

See [troubleshooting](troubleshooting.md) for help.
