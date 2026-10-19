---
name: police
description: Install agent-police in this project (one step) — or show its status if it is already installed
---
Install agent-police in the current project and tell the user, in their language, what changed.

1. If `.agent-police/bin/agent-police.mjs` already exists, run `node .agent-police/bin/agent-police.mjs license` and `node .agent-police/bin/agent-police.mjs check --fast`, and report the status in two lines. Stop.
2. Otherwise install from the copy that ships with this skill (local files, nothing is downloaded): run exactly
   `node "<this skill's base directory>/agent-police/bin/agent-police.mjs" install`
   with the skill's base directory filled in. Only if that file is missing, fall back to `npx --yes github:agentpolice/police install`.
3. Report to the user in plain words (no jargon):
   - the police is on: from now on the agent is not "done" until the checks pass;
   - commit the new `.agent-police/` folder and the instruction files, so every clone is guarded;
   - the trial status (`node .agent-police/bin/agent-police.mjs license`);
   - how to remove it: `node .agent-police/bin/agent-police.mjs uninstall`.
Do not read or open the files inside `.agent-police/`.
