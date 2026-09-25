---
name: watch
description: >-
  Scheduled loop that goes where buyers talk to keep their language fresh, and flags when a
  competitor changes its promises, proof, or pricing. Use when someone says "watch my
  competitors", "set up the weekly check", or "keep this running".
---

# Watch

The loop that makes this a system instead of a one-time exercise.

1. Go where these buyers live: the communities, forums, groups, and social platforms the calls
   and discovery point to. Drive the user's Chrome (Codex's Chrome plugin or computer use, or Claude in Chrome in
   Claude Code) to read recent posts in the buyer's words. Add new
   lines to the card's voice-of-buyer bank with the URL, marked as found online.
2. Schedule a weekly run in your agent (Codex scheduled tasks or a Claude scheduled task) that
   runs `competitor-read` at medium depth on every competitor in `brief.md`.
3. Compare each new capture with the last one and write `outputs/watch/<date>.md`: changed
   promises, new proof, pricing changes, with before and after and the URL.
4. If new transcripts landed in `inputs/transcripts/`, rerun `buyer-brain` and note which
   patterns got stronger, which weakened, and anything new.
5. Every run writes its file, even when nothing changed, so you can see it ran.
