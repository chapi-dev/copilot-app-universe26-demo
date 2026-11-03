# 4. Bring your tools together

**Goal:** the agent uses your context, tools and rules from one place.

## Ingredients in this repo
- `.github/copilot-instructions.md` – repo rules (style, how to run tests)
- `.github/agents/reviewer.agent.md` – a custom review agent
- `mcp/mcp.sample.json` – sample MCP server (Microsoft Learn)

## Steps
1. Add the MCP server from `mcp/mcp.sample.json` in the app (Customize > Installed / repo MCP settings).
2. Ask: *"Using Microsoft Learn, what is the recommended way to ... ?"* -> show the tool call.
3. Switch to the `reviewer` agent and ask for a review of the last diff.
4. Show that the instructions file changed behaviour (it runs pytest before finishing).

## Talking points
- Tools, agents and rules are configured once and shared by every session.
