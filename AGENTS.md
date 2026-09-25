# Buyer Brain OS

This folder reads a seller's sales and discovery calls to find who their buyers really are, maps
the competitors those buyers would pick instead, reads each competitor's site as those buyers, and
maps the gaps: what buyers need versus what competitors offer, their angles, their words, how they
reach people, and what they assume moves a buyer. It runs in Claude Code or Codex.
Skills live in `.agents/skills/` (Claude sees the same folder through `.claude/skills`).

## The pipeline

Run in order. Each step reads the files the previous step wrote. Before each step, the `dispatch`
skill decides who runs it: gathering raw data goes to Codex and the analysis that becomes the card
and the report goes to Claude when both are installed; otherwise the agent you are in runs
everything.

1. **intake**: interviews the user, seals what they believe about their buyer, gets transcripts
   in. Writes `brief.md`. Nothing else runs until it exists.
2. **buyer patterns**, one of two paths, both produce `cards/<buyer>.md`:
   - Have transcripts in `inputs/transcripts/`: run the `buyer-brain` skill.
   - No transcripts: run `literature-casting` first and save its full output, including the text
     it mined, to `outputs/literature-casting.md`. Hand it `brief.md` as the avatar doc; the belief
     is already sealed there, so do not run the Casting Call again. Then run `buyer-brain` in hypothesis mode on it
     plus `inputs/written/`. Replace hypotheses with call evidence as soon as you have calls.
3. **competitor-map**: finds who these buyers would pick instead, from the calls first, then
   search from each buyer pattern's seat. Maps what each one sells, whether it does the same job,
   its angle, its words, and how it reaches people. Keeps only real competitors. Writes
   `outputs/competitor-map.md` and the list in `brief.md`.
4. **competitor-read**: an agent opens each kept competitor's real site in the user's Chrome and
   reads it as each buyer pattern. Writes `outputs/competitors/<name>.md`. The seller's current
   positioning (every offer, site, and how they pitch on calls) is captured once as a baseline
   (`outputs/baseline.md`), not audited.
5. **cross-check**: maps the gaps: offering, approach, language, reach, and mind. Writes
   `outputs/gaps.md` (takeaways, the gap map, only-we lines, what to stop saying) and
   `outputs/synthesis.md`, the one page to read first: what buyers feel, who they are up against,
   what the seller brings, the angles to take, and the language to use.
6. **watch** (optional): a scheduled rerun that flags when a competitor changes its promises.

At any point, `python3 scripts/render_report.py` bundles everything written so far into
`outputs/report.html` for reading or presenting.

How to read a buyer is in `.agents/skills/buyer-brain/references/method.md`. Literature Casting is Max Bernstein's skill from
AI Strategy Exchange Class 01, included unchanged.

## Rules

- Never show the user buyer patterns until the brief's "What I believe today" is sealed.
- Transcripts are the user's own data. Remove names only if the outputs will be shared.
- Quote transcripts exactly. Never invent a buyer line.
- Keep several buyer patterns and outliers. Never average people into one persona.
- Interpret deeply. Buyer quotes are verbatim; the read of what is underneath them is the point.
- Competitor claims are captured with the URL they came from.
- No em dashes in anything you write for the user.
