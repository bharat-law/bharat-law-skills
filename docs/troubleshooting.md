# Troubleshooting

| Symptom | Action |
| --- | --- |
| Connector says “Not connected” or shows zero tools | Complete OAuth sign-in and consent, then resync the tool list. A saved URL alone does not establish a connection. |
| “Couldn't register with Bharat Law's sign-in service” | Leave the OAuth client ID and secret fields empty so Claude registers automatically, then retry. If it persists, contact support with the `ofid_` reference shown in the error. |
| Earlier Claude connection stops working | Reconnect Bharat Law from Claude's connector settings and sign in again. |
| Sign-in completes but Claude reports authorization failed | Disconnect Bharat Law in Claude and connect again, leaving OAuth client details empty. If it still fails, contact support with the approximate time and error reference. |
| Unexpected redirect or callback error | Remove any OAuth client ID you entered for the connector, then reconnect. |
| Wrong workspace or unclear case/matter | List available workspaces or matching records and select the intended one. Application cases and court matters use different references. |
| Several similarly named court matters | Compare court/bench, case number, CNR, and parties. Refine the query or ask the user to select a match. |
| No upcoming listing is recorded | Report that record state and freshness. It does not establish that no hearing is scheduled. Request wider/live retrieval only when the user intends it. |
| Operation remains queued/running or the connection drops | Recover it with `list_operations` or poll its returned operation reference. Respect retry timing. Do not restart accepted work. |
| A question appears while work is running | Answer the current clarification using its current question reference. Complete required court verification in Bharat Law when directed. |
| `retrieval_recovery_required` | Inspect the existing retrieval in Bharat Law. Do not submit another lookup to replace an uncertain submission. |
| `request_key_conflict` or `answer_conflict` | A previous identifier was reused with changed inputs. Check the existing work; use a new work key for a genuinely new request. Do not overwrite an already-answered question. |
| Document not ready or no longer accessible | Check processing and current access in Bharat Law. Do not silently drop the selected document or substitute unrelated material. |
| Insufficient credits or unavailable feature | Review the Bharat Law account's credits and entitlements. Repeated requests do not grant access. |
| Citation or legal proposition cannot be established | Read the available evidence and report the unresolved portion. A failed search does not prove nonexistence or fabrication. |
| Latest-order request cannot be fulfilled | The current public MCP catalogue lacks a latest-order tool. Use the Bharat Law app's available matter workflow; do not infer an order from a hearing record. |
| Claude Code sign-in fails | Claude Code is not currently supported. Use Claude on the web, desktop, mobile, or Cowork. |

Contact [support@bharat.law](mailto:support@bharat.law) with a short description, plugin version, approximate time, and a safe error code if available. Do not include passwords, OAuth secrets, tokens, or confidential matter content in public reports.
