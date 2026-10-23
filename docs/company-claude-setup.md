# Company setup handoff

This is the operator's guide for setting up the Bharat Law connector and companion plugin under the company Claude account. The package is prepared locally. Live deployment, private credential entry, GitHub publication, Claude validation, and submission are separate actions to complete using this guide.

## 1. Publish the documentation and plugin repository

Create the organization repository `bharat-law/bharat-law-skills` from the prepared local package. Keep BFF code in its existing private repository. The plugin contains only public workflow guidance and a public server URL; it contains no service implementation or credentials.

The plugin repository may remain private during preparation and submission review, but it must be **public before the directory listing goes live**. For this setup, publish its reviewed `release` branch publicly before deploying the directory-ready BFF metadata so the advertised guide resolves:

`https://github.com/bharat-law/bharat-law-skills/blob/release/docs/setup.md`

Protect `release`, allow changes only through reviewed updates, and use deliberate manual publishing for the initial release. Connect a GitHub identity with push access to this repository when the Claude plugin submission requests it. See [release procedure](release.md).

## 2. Use the company Claude organization

Sign in with the long-term company account/organization that should maintain Bharat Law's listing. Create both submissions there: one **MCP connector** and one **Plugin bundle**. A connector submission alone does not distribute skills.

Use the same URL in the connector and plugin: `https://api.bharat.law/mcp`. Keep the display name **Bharat Law** and review permanent slug **bharat-law** before submission. See [listing copy](connector-listing.md).

## 3. Deploy the directory-ready BFF update

Use the BFF's existing deployment process and its `docs/cognito-mcp-oauth-setup.md` runbook. The local directory-readiness change introduces a separate confidential Cognito app client, `McpClaudeDirectoryOAuthClient`, with a generated secret. It does not add a database migration.

After deployment, confirm:

- The stack output `McpClaudeClientId` identifies the new directory client.
- The accepted runtime `MCP_CLAUDE_CLIENT_ID` is that same new ID.
- Its callback is exactly `https://claude.ai/api/mcp/auth_callback`.
- The previous public `McpClaudeOAuthClient` is retained but retired from MCP acceptance; existing Claude connections must reconnect.
- Public authorization metadata advertises `none`, `client_secret_basic`, and `client_secret_post`. `none` remains for the separate public ChatGPT client; Claude requires confidential-client authentication.
- Existing ChatGPT callbacks, native application credentials, token audience checks, refresh rotation, and revocation behavior remain intact.

Do not weaken the accepted-client or audience checks to make a connection succeed. Arbitrary CIMD/DCR clients and Claude Code loopback clients are outside this configuration.

## 4. Retrieve the new client secret privately

An authorized AWS operator opens **Cognito → the production user pool → App clients**, and selects the app client matching the newly deployed `McpClaudeClientId` stack output. Retrieve its generated app-client secret in the AWS console and enter it directly into Claude's private credential fields.

Do not print the secret in a terminal or stack output, store it in the plugin or runtime environment, paste it into chat, or include it in screenshots. The stack exposes the ID; it does not expose the secret. Do not use the retired public Claude client or the ChatGPT client.

## 5. Test through a custom connector

In the company Claude account, open **Customize → Connectors → Add custom connector** (or **Settings → Connectors**, depending on the client). Enter:

| Field | Value |
| --- | --- |
| Name | Bharat Law |
| Remote MCP server URL | `https://api.bharat.law/mcp` |
| OAuth client ID | The new deployed `McpClaudeClientId` value, entered privately |
| OAuth client secret | The new client's Cognito-generated secret, entered privately |

Use **Use your own OAuth client** or **Advanced settings** for the private OAuth fields. Complete sign-in and consent with a controlled Bharat Law account. Credentials saved in a directory submission do not automatically apply to a custom connector added by URL.

Reconnect any previous Claude test connection. Resync tools and confirm the deployed catalogue contains **18 tools**:

- Context and discovery: `list_workspaces`, `switch_workspace`, `list_cases`, `set_case_context`, `list_conversations`, `list_court_matters`, `get_next_hearing`, `list_case_documents`, `list_sources`.
- Work: `search`, `research`, `deep_research`, `draft_document`.
- Recovery and content: `list_operations`, `get_operation`, `respond_to_operation`, `cancel_operation`, `read_content`.

Exercise every tool using controlled data. Confirm login, consent, refresh, revoked access, meaningful errors, operation recovery, and public progress streaming. Use the supplied [evaluation cases](../evals/cases.json) for skill behavior. A successful package validator is not evidence that deployed authentication or every tool works.

For private skill testing before the directory listing exists, upload the prepared plugin ZIP through **Customize → Plugins → Add → Upload plugin**. The archive must contain `.claude-plugin/plugin.json` at its root or inside one top-level folder; exclude `.git` and local credentials. Open the installed plugin's **Connectors** tab and connect Bharat Law using the test connection above. Then open a new chat, confirm the three skills are available, and run the controlled evaluations. An upload to your own account does not publish a directory listing.

## 6. Complete the connector submission

At [Claude submissions](https://claude.ai/directory/manage), create or continue the company-owned MCP connector draft. Use [the prepared fields and description](connector-listing.md).

For authentication select **Always required → OAuth sign-in → Anthropic-held client credentials → Anthropic holds a client secret**. Enter the new client ID and secret privately. These credentials authenticate Claude's OAuth client; users still sign in to their own Bharat Law accounts.

Provide a populated reviewer account through the portal's private fields, with appropriate workspace/case access, processed documents, useful saved conversations, a court matter, and enough credits to exercise the submitted tools. Keep its credentials out of this repository.

Review company contact/ownership fields and data-handling answers personally. Legal documents can contain health information; explain conditional processing where applicable. Distinguish ownership of the API from rights in underlying court/legal sources. Check testing, launch, and compliance attestations only after the relevant facts are verified.

## 7. Submit the plugin and pair the listings

Create a separate **Plugin bundle** submission in the same Claude organization. Connect the GitHub account with push access, select `bharat-law/bharat-law-skills`, and track the protected `release` branch. Validate the plugin in Claude's portal, then pair it with the connector using their identical server URL.

The package version is `0.1.1`. It includes three skills: Indian legal-answer verification, citation checking, and recorded next-hearing lookup. Latest-order retrieval remains deferred. Hosted Claude is the initial authentication target; do not claim tested Claude Code authentication.

Resolve validation findings, review both final previews, and submit deliberately. Company-account access, reviewer credentials, real live tests, portal validation, and final attestations are operator steps; this package does not assert they are complete.

## Official references

- [Publish to Claude's directory](https://claude.com/docs/directory/publish)
- [Connector authentication](https://claude.com/docs/connectors/building/authentication)
- [Connector submission](https://claude.com/docs/connectors/building/submission)
- [Plugin submission](https://claude.com/docs/plugins/submit)
- [Plugin pre-submission checklist](https://claude.com/docs/plugins/pre-submission-checklist)
- [Custom remote MCP connectors](https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp)
