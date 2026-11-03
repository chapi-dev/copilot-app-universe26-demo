# 5. Steer sessions from any device

**Goal:** a long-running session keeps going and you steer it from a second device.

## Steps
1. Desktop: start a long task, e.g.
   > Add a CLI to sample-app (`python -m cart add|total`), with tests and docs. Ask me before choosing the CLI library.
2. Switch to the second device (phone/laptop) signed in with the same account.
3. Open the session: show live progress, answer the pending question, send a steering message ("use argparse, no extra deps").
4. Back on desktop: show the session picked up the instruction.

## Talking points
- You don't have to babysit the desktop; approvals and corrections work remotely.
- Pair with demo 3: automation results can be reviewed from the phone.

> Verify in your build which remote/steering options are enabled for your account.
