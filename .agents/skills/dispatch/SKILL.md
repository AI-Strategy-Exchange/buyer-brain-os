---
name: dispatch
description: >-
  Decide which agent runs each Buyer Brain OS step and hand work to the other agent when it is
  installed: gathering raw data (search, competitor sites, per-call notes, sweeps) to Codex, and
  the analysis that turns it into the buyer card, the gaps, and the final report to Claude. Falls
  back to running the step yourself when the other agent is not there. Use before running
  buyer-brain, competitor-map, competitor-read, cross-check, or watch, or when someone says "split
  this up", "use Codex", or "use Claude".
---

# Dispatch

The folder works with any one agent. When both Claude and Codex are on the machine, split the work
by kind: it gives better results.

| Work | Steps | Best on |
| --- | --- | --- |
| Gathering raw data: search, open sites, click through, capture words and screenshots, write one note per call | competitor-map (the search), competitor-read, buyer-brain (the clue files), watch | Codex |
| Analysis: read across all of it and decide what it means: the buyer card, the match test and final map, the gaps, the angles, the synthesis report | buyer-brain (the card), competitor-map (the final map), cross-check | Claude |

Intake always runs in whatever agent the user is talking to.

## 1. See what is here

```bash
command -v claude
command -v codex
```

Tell the user what you found in one line. Then:

- **Both installed:** hand each step to the agent it fits. Do the step yourself when it is yours.
- **Only you:** run every step yourself. Say nothing more about it.
- **ChatGPT's Codex tab, Cowork, or the Claude desktop app:** no shell to reach the other agent. Run
  every step yourself.

If a handoff fails (not logged in, no web access, no Chrome connection), run the step yourself and
tell the user in one line.

## 2. Hand off

The handoff prompt names the skill and the files, and nothing else. The skill carries the rules.
Do not add constraints, tool choices, or evidence requirements of your own; they crowd out the
analysis.

From Claude, gathering to Codex:

```bash
codex exec --skip-git-repo-check -C "$PWD" --dangerously-bypass-approvals-and-sandbox \
  "Run the direct competitor search in .agents/skills/competitor-map/references/direct-search.md." \
  < /dev/null > .work/<step>.log 2>&1 &
```

From Codex, analysis to Claude:

```bash
claude -p "Run the cross-check skill (.agents/skills/cross-check/SKILL.md)." \
  --model opus --dangerously-skip-permissions < /dev/null > .work/<step>.log 2>&1 &
```

Handoffs run with no sandbox and no approval prompts, so the worker can use its browser, Chrome
plugin, computer use, and shell without being blocked. A sandboxed or prompting run gets its tools
declined in the background and stops.

## 3. Split big steps

Writing one note per call is the slow part. Split the calls into shares of about ten and run one
worker per share, in parallel. Competitor reads split the same way, a few competitors per worker.
Give each worker its share by file or name. The card and the synthesis stay in one agent: they are
one read across everything.

## 4. Check what comes back

A worker finishing is not the step done. Before moving on:

- The output file exists for every item in the share.
- Clue files are real reads, not template text: run
  `python3 .agents/skills/buyer-brain/scripts/check_generic.py outputs/clues` and redo any call it
  flags.
- Read one or two outputs yourself. If they are thin or generic, redo them.

## Gotchas

- `mkdir -p .work` first. It is gitignored scratch space for logs.
- A worker killed mid-run can leave half-written files that look finished. Check timestamps against
  when the worker stopped, and redo anything it touched.
- The direct competitor search is long by design. Give Codex high reasoning effort for it
  (`-c model_reasoning_effort="high"`) and let it run; thirty minutes or more is normal.
- Analysis from a light model at low reasoning effort comes out thin. If Codex has to write the
  card or the synthesis, raise its reasoning effort (`-c model_reasoning_effort="high"`).
