# agent-police

**Your AI coding agent said "done". Was it?**

agent-police sits next to the agent (Claude Code, Cursor, Copilot, Gemini, Lovable, Bolt…) and does not let it say "done"
until the work is real: no deleted or disabled tests, no stubs, no secrets in the code, no red test suite — and it asks
instead of guessing. When something is not done, it says what and why.

## Install

**Claude Code** — one step:

```
/plugin install agent-police --marketplace agentpolice/police
```

then type `/agent-police:police` in your project.

**Anywhere else** (inside your project's git folder):

```
npx --yes github:agentpolice/police install
```

The install adds a `.agent-police/` folder and short instructions for your agents. Commit them, so every clone is guarded.

## Use

| | |
|---|---|
| `node .agent-police/bin/agent-police.mjs check` | the verdict on the current work: DONE / NOT DONE, and why |
| `node .agent-police/bin/agent-police.mjs prove` | judge finished work it never saw (a teammate's PR, a Lovable export): honest · gamed · failed |
| `node .agent-police/bin/agent-police.mjs handoff` | the plain-language report: done · not done and why · what I need from you |
| `node .agent-police/bin/agent-police.mjs license` | trial / license status |
| `node .agent-police/bin/agent-police.mjs uninstall` | remove it |

## Trial and license

Two days free from the first run. After that it stops checking (it never blocks your work) until you install a license.
For a license: 064105@gmail.com

Proprietary software — see LICENSE.
