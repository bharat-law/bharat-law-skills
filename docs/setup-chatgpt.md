# Connect Bharat Law to ChatGPT

Use your existing Bharat Law account to research Indian law and work with authorized cases, documents, saved conversations, and recorded court matters.

## Before connecting

Have access to the intended Bharat Law workspace and cases, with any documents needed for your task ready to use. Read [permissions and data handling](permissions-and-data.md), including saved-work sharing, credits, and the effect of workspace switching.

| Setting | Value |
| --- | --- |
| Name | Bharat Law |
| MCP endpoint | `https://api.bharat.law/mcp` |
| Authentication | OAuth sign-in with your Bharat Law account |
| Bharat Law API key | Not required |
| Support | [MCP troubleshooting and contact guide](https://github.com/bharat-law/bharat-law-skills/blob/release-chatgpt/docs/troubleshooting.md) |
| Privacy | [Bharat Law privacy policy](https://bharat.law/legal/privacy-policy) |

## Connect

When Bharat Law is available in the ChatGPT Plugins directory, install it and connect your Bharat Law account. Review the permissions and disclosure before signing in. The plugin bundles the MCP connection and three guided skills; availability depends on the supported client surface. Connecting does not expand your Bharat Law account permissions.

For a custom connection, add a custom MCP server from ChatGPT **Plugins** using the endpoint above. Sign in with your Bharat Law account. See [troubleshooting](troubleshooting.md) if sign-in fails or an authentication update is required.

Sign-in requests `openid`, `email`, `profile`, `bharat-law-mcp/read`, `bharat-law-mcp/run`, `bharat-law-mcp/draft`, and `bharat-law-mcp/switch_workspace`. These permissions cover identity, reading, research, drafting, and workspace switching. They do not bypass workspace, case, or document access.

## Try the connection

1. “List my Bharat Law workspaces and identify the active one.”
2. “Find my saved Bharat Law conversations so I can choose one to continue.”
3. “Find the recorded next hearing for my subscribed matter. Ask me to choose if several matters match.”
4. “Verify the Indian legal claims in this answer and show supporting or conflicting passages.” Then supply the answer.
5. “Check this Indian judgment citation and the proposition beside it.” Then supply both.
6. “Run Bharat Law's research on this question and compare it with your answer. Check penalties against every relevant subsection, weigh authorities for my court, and link the sources for each correction.” Provide the question and your court or jurisdiction.

Legal lookup returns up to three matches and available source text through Bharat Law links. Assess only the evidence returned: a summary cannot verify an exact quotation from the original judgment. Legal lookup does not save searches or create conversations.

For separately requested research or document work, use the intended workspace/case and continue the same conversation for related follow-ups. Research saves answers; drafting and extended research can save additional work and use credits. Extended research requires your intent. Switching workspace also changes the workspace selected in Bharat Law web and mobile apps.

See [worked examples](examples.md) for inputs, sample outcomes, and evidence limits. The service publishes readable tool titles while retaining the existing API identifiers. If a connected plugin still shows an older catalogue, refresh it from plugin settings; reconnect if sign-in needs renewal.

## Disconnect or revoke

Disconnect from ChatGPT's plugin settings when you no longer want that account connected. To revoke Bharat Law access, sign in to Bharat Law, open **MCP connections** at `/integrations/mcp`, select the intended ChatGPT connection, and revoke access. Disconnecting in ChatGPT and revoking in Bharat Law are separate actions.

Revocation blocks further access and token refresh for that connection. Accepted work may finish and use credits; saved work retains normal workspace/case permissions and retention rules. Do not restart accepted work merely because a connection was interrupted.

## Limits

Latest-order retrieval is not currently available. Source coverage and freshness vary. A recorded hearing can change; no recorded date does not establish that no hearing is scheduled. Missing evidence and unknown legal treatment remain unresolved. Review generated answers and drafts before relying on them, filing, or sharing them.
