# Changelog

## 1.1

- **Four agents, one police:** Claude Code, Cursor, Codex and GitHub Copilot (CLI and cloud agent) — the request becomes the task contract, a stop hook sends the agent back until DONE, the judge's files cannot be read. Installed by the same one command.
- **Scope with no configuration:** when the request names its files, a change to any other file is caught.
- **The digest:** what the police caught, in plain words, to your phone (Telegram or a webhook) and as a dashboard; a stuck agent pings you.
- **GitLab** merge requests get the same trusted judge. **Windows:** CRLF checkouts no longer read as tampering; hooks run in PowerShell.
- **The same mistake never twice:** `lesson add` turns a fixed mistake into an enforced rule (a forbidden pattern or a regression test). Lessons only accumulate; removing or weakening one is caught, and its mistake is still enforced. Unsafe patterns (ReDoS) are refused.
- **Stuck loops stop:** the same failure again after the way out ⇒ the agent stops and asks you, instead of retrying the same fix.
- **Nothing passes silently:** changed files the checks cannot read (submodules, symlinks, LFS pointers, binaries) are named and fail the verdict.
- **A judge that can be trusted:** `ci` writes a GitHub workflow that judges every pull request with the engine and config from the base branch; a hand-edited engine copy is caught.
- **verify shows the test count**, and warns when a sub-package's tests may not be reached. Updating agent-police is committable; re-installing changes nothing.

## 1.0

- **Live guard** for any coding agent: instructions (AGENTS.md, CLAUDE.md, Cursor, Copilot, Gemini), git hooks, and Claude Code hooks.
- **Catches:** deleted / skipped / weakened tests, stubs, swallowed errors, secrets and personal data in code, a red suite at "done", code changed with no test that proves it.
- **Asks instead of guessing:** a number or rule nobody gave becomes a question, collected at the end.
- **Flaky tests:** a failing test is re-run and compared with the code before the change; an already-flaky test is flagged, not blamed.
- **`prove`:** judge finished work the guard never saw: honest · gamed · failed, with a one-page proof.
- **Plain report:** done · not done and why · what I need from you, plus a ready-to-paste fix list.
- **Runs locally and offline**, installed into the project; Claude Code one-click plugin.
- 2-day trial, then a signed license.
