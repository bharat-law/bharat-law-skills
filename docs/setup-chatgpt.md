# Connect Bharat Law to ChatGPT

Use your existing Bharat Law account to research Indian law and work with authorized cases, documents, saved conversations, and recorded court matters. The OpenAI package is a draft until its directory submission has passed review and been published.

## Before connecting

Have access to the intended Bharat Law workspace and cases. Documents needed for a task must be processed and ready. Read [permissions and data handling](permissions-and-data.md), including saved-work sharing, credits, and the effect of workspace switching. Use synthetic, nonconfidential data while testing the integration.

| Setting | Value |
| --- | --- |
| Name | Bharat Law |
| MCP endpoint | `https://api.bharat.law/mcp` |
| Authentication | OAuth sign-in with your Bharat Law account |
| Bharat Law API key | Not required |
| Support | [support@bharat.law](mailto:support@bharat.law) |

## Install from the directory

After publication, find **Bharat Law** in the ChatGPT Plugins directory, install it, and connect your Bharat Law account. Review the permissions and disclosure before signing in. The plugin bundles the MCP connection and three guided skills; their availability depends on the supported client surface. Installing a package does not expand your Bharat Law account permissions.

## Test a development connection

This section is for maintainers testing before publication. From ChatGPT **Plugins**, add a custom MCP server using the endpoint above. Use the existing registered **public** ChatGPT OAuth client, not Claude dynamic registration. The portable `mcp.json` contains the production public client ID, `provided` registration, and token authentication method `none`. No client secret exists for this client.

The package requests `openid`, `email`, `profile`, `bharat-law-mcp/read`, `bharat-law-mcp/run`, `bharat-law-mcp/draft`, and `bharat-law-mcp/switch_workspace`. These permissions allow the full 18-tool catalogue; they do not bypass workspace, case, or document access. Some clients show the advanced settings only through the package/connection flow.

Use the callback URL displayed by the specific connection flow. The operator must register that exact URL with both the OAuth provider and the BFF allowlist. Do not substitute a wildcard or an older connection's callback. Authentication also uses Cognito discovery and the BFF UserInfo proxy declared in `mcp.json`; those server changes must be deployed before testing.

If an older development connection says **Authentication update required**, reconnect and sign in again, then verify that the tool catalogue contains the current 18 tools. Confirm that `search` accepts `query`, `artifact_type`, and a free-text court or statute target, and that `read_content` accepts returned `source_url` values. Do not use a stale catalogue as submission evidence. See [troubleshooting](troubleshooting.md) if sign-in fails.

## Try the connection

1. “List my Bharat Law workspaces and identify the active one.”
2. “Find my saved Bharat Law conversations so I can choose one to continue.”
3. “Find the recorded next hearing for my subscribed matter. Ask me to choose if several matters match.”
4. “Verify the Indian legal claims in this answer and show supporting or conflicting passages.” Then supply the answer.
5. “Check this Indian judgment citation and the proposition beside it.” Then supply both.

Legal lookup returns up to three matches as Markdown and reads stored judgment details/headnotes and available statute text through returned Bharat Law links. Exact judgment quotations remain unresolved when only headnotes are available. It does not save searches or create conversations. For separately requested research or document work, use the selected workspace/case and reuse its conversation for related follow-ups. Research saves answers; drafts and extended research can save additional artifacts and use credits. Starting extended research requires the user's intent. A workspace switch also changes the workspace selected in Bharat Law web and mobile apps.

## Disconnect or revoke

Disconnect from ChatGPT's plugin settings when you no longer want that account connected. To revoke the Bharat Law grant, sign in to Bharat Law, open **MCP connections** at `/integrations/mcp`, select the intended ChatGPT connection, and revoke access. Disconnecting in ChatGPT and revoking in Bharat Law are separate actions.

Revocation blocks future access and refresh for that connection. Accepted work may finish and use credits; saved artifacts retain normal workspace/case permissions and retention rules. Do not restart accepted work merely because a connection was interrupted.

## Limits

This release has no embedded UI and no latest-order retrieval tool. Source coverage and freshness vary. A recorded hearing can change; no recorded date does not establish that no hearing is scheduled. Unknown legal treatment remains unresolved. Review generated answers and drafts before relying on them, filing, or sharing them.
