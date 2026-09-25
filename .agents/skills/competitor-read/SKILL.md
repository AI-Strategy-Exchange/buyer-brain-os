---
name: competitor-read
description: >-
  Open each mapped competitor's real website in the user's Chrome and read it as each buyer
  pattern on the buyer card: what they sell, the angle, their words, how they reach people, and
  what lands, what the buyer doubts, and where they would leave. Also captures the seller's own
  positioning as a baseline. Use after competitor-map, or when someone says "read my
  competitors" or "how would my buyer see this site".
---

# Competitor Read

Read each competitor's site as the buyer, out loud, clicking through like they would.

## Inputs

- `outputs/competitor-map.md` (the kept competitors, their rows, the reference set)
- `cards/<buyer>.md` (must exist)
- `brief.md` ("What I sell" and "My current positioning")

## How

Drive the user's own Chrome through the agent's Chrome connection: Codex's Chrome plugin (or
Codex computer use), or Claude in Chrome in Claude Code. Both reuse the user's logged-in sessions.
If neither is on, walk the user through intake's Chrome setup (step 4).

Click through the way the buyer would: homepage, then wherever the page leads them (pricing,
about, case studies, the contact or booking flow). Screenshot what you read into
`outputs/competitors/<name>/`. Add reviews and social mentions where they exist.

## For each competitor

Write `outputs/competitors/<name>.md`:

1. **What they sell and to whom,** confirmed on the site. If it turns out not to do the same job
   for these buyers, say so and stop; cross-check will drop it.
2. **Their angle:** what they lead with, and the reason they give a buyer to choose them.
3. **Their words:** headline, main promise, and the phrases they repeat, quoted with URLs.
4. **How they reach people:** call to action, price, proof (whose, how many, checkable or not),
   tone, and the channel. Note the privacy or data page and whether it matches the homepage.
5. **Read as each buyer pattern,** one section per pattern: "I'm reading this page. This lands.
   This I doubt. Here is where I'd leave." Quote the page line behind each reaction.
6. **The mind it sells to:** what the site assumes makes a buyer decide, against what the card
   says actually moves these buyers.

For the reference set, capture their words only, no buyer read.

## Baseline

Capture the seller's own positioning once in `outputs/baseline.md`, not audited: every offer in
"What I sell", every site in "My current positioning", and how the seller pitches on calls (the
"What was offered" sections of `outputs/clues/`). Same fields: what they sell, the angle, their
words, how they reach people. Each line with its source.

## Gotchas

- Some big sites block plain page fetching. Use the browser. If you fall back to a cached copy,
  say which quotes came from it.
- Pricing tables are often drawn by script. Check them in the browser before calling price "not
  visible".
- Check the privacy or data page against the homepage. Contradictions matter to buyers who check
  data first.
- A page can land for one buyer pattern and lose another on the same line. Say which pattern you
  are reading as.
- Every captured claim has a URL.
- Close cookie banners and pop-ups before a screenshot.
- A seller with no website still has a baseline: LinkedIn, a booking page, a directory listing,
  and how they pitch on calls. Capture whatever exists.
- No em dashes.
