# Bharat Law MCP support

Get help connecting Bharat Law to Claude, finding sources, and continuing saved research or drafts. A Bharat Law account is required. For account-specific help, email [support@bharat.law](mailto:support@bharat.law).

| Symptom | Action |
| --- | --- |
| Connector says “Not connected” or shows zero tools | Complete OAuth sign-in and consent, then refresh the tool list. A saved URL alone does not establish a connection. |
| Claude cannot complete sign-in | Leave the OAuth client ID and secret fields empty and try again. If needed, disconnect Bharat Law in Claude and reconnect. Contact support if the problem continues. |
| Sign-in or a redirect fails | Contact support with the approximate time and a safe error reference. Do not bypass identity verification or provide tokens in a chat. |
| Research, drafting, or workspace-switch permission is missing | Reauthorize with the requested permission. Read permission does not grant these capabilities. Ordinary document access denial must be resolved in Bharat Law, not by repeatedly reconnecting. |
| No court or statute target matches | Use the returned choices to refine the request. A High Court lookup needs its name; a statute lookup should identify the provision and Act. |
| Source text is unavailable or changes during reading | Leave the affected verification unresolved. Read the source again if appropriate. A summary cannot verify an exact quotation from the original judgment. |
| Wrong workspace or unclear case/matter | List available workspaces or matching records and select the intended one. Application cases and court matters are distinct. |
| Several similarly named court matters | Compare court/bench, case number, CNR, and parties. Refine the query or select the intended match. |
| No upcoming listing is recorded | Report that state and its freshness. It does not establish that no hearing is scheduled. Wider or fresh retrieval requires your intent and may use credits. |
| Work remains queued/running or the connection drops | Recover the existing work rather than starting it again. Follow any retry guidance returned by the connector. |
| A clarification is requested | Answer the current question. Complete any required court verification in Bharat Law when directed. |
| A court retrieval needs recovery | Check the existing work in Bharat Law. Do not start a duplicate lookup while the original request's outcome is uncertain. |
| Document is not ready or is no longer accessible | Check readiness and current access in Bharat Law. Do not substitute unrelated material or silently drop the selected document. |
| Insufficient credits or an unavailable feature | Check your Bharat Law credits and entitlements. Repeated requests do not grant access. |
| A citation or legal proposition cannot be established | Read the available evidence and leave the unresolved portion explicit. A failed search does not prove nonexistence or fabrication. |
| Latest-order request cannot be fulfilled | Latest-order retrieval is not currently available through the connector. Use the Bharat Law app's available matter workflow; do not infer an order from a hearing record. |
| Claude Code sign-in fails | Claude Code is not currently supported. Use Claude on the web, desktop, mobile, or Cowork. |

See [Claude setup](setup.md) and [permissions and data handling](permissions-and-data.md) for connection and account details.

Contact [support@bharat.law](mailto:support@bharat.law) with a short description, plugin version, approximate time, and a safe error reference if available. Do not include passwords, OAuth secrets, tokens, or confidential matter content in public reports.
