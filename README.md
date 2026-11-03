# GitHub Copilot app – Universe '26 demo

Repo to demo, one by one, the six announcements of **"Explore what's new in GitHub Copilot app"**.

| # | Announcement | Demo guide | What you show |
|---|--------------|-----------|---------------|
| 1 | Work smarter with Copilot Fusion | [demos/01-fusion](demos/01-fusion/README.md) | Same bug, different Auto tiers (efficiency / balance / intelligence / Fusion) |
| 2 | Parallelize work with Projects | [demos/02-projects](demos/02-projects/README.md) | A coordinator splitting `sample-app` issues across child sessions |
| 3 | Automate recurring work | [demos/03-automations](demos/03-automations/README.md) | Scheduled Copilot automations + GitHub Actions in this repo |
| 4 | Bring your tools together | [demos/04-tools](demos/04-tools/README.md) | MCP servers, custom agents, instructions |
| 5 | Steer sessions from any device | [demos/05-steer-anywhere](demos/05-steer-anywhere/README.md) | Start on desktop, steer / approve from another device |
| 6 | Turn ideas into images | [demos/06-images](demos/06-images/README.md) | Generate and refine images inside a session |

Full run of show (~25 min): [docs/run-of-show.md](docs/run-of-show.md)

## Layout

```
.github/
  copilot-instructions.md   repo-wide instructions (demo 4)
  agents/                   custom agents (demo 4)
  ISSUE_TEMPLATE/           demo-task template (demo 2)
  workflows/                CI + nightly health check (demo 3)
automations/                prompts ready to paste into Copilot app Automations (demo 3)
demos/                      one folder per announcement
docs/                       run of show, prep checklist
mcp/                        sample MCP config (demo 4)
sample-app/                 tiny Python cart with deliberate bugs + tests
assets/                     output folder for generated images (demo 6)
```

## Quick start

```powershell
cd sample-app
python -m pip install pytest
python -m pytest        # 2 tests fail on purpose (these are the demo bugs)
```

> Features are demoed as shown in the announcement. Check names and availability in your own Copilot app build before presenting (see [docs/prep-checklist.md](docs/prep-checklist.md)).
