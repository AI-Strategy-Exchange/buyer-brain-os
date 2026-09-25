---
name: cross-check
description: >-
  Map the gaps between the seller's buyers and their competitors: what buyers need versus what
  competitors offer, the angles competitors take, the words they use versus the words buyers use,
  how they try to reach people versus how these buyers actually buy, and what they assume moves a
  buyer versus what does. Ends in the takeaways, the only-we lines, and what to stop saying. Use
  after competitor-read, or when someone says "run the cross-check", "map my gaps", or "what
  should I say that nobody else does".
---

# Cross-Check

Start from the buyers' own words. Competitors are the backdrop.

The core of this is the buyer's mind, not only their voice: how they decide, what they trust, what
they are afraid of being seen as, and the hesitation right before they buy. Pain phrases are common
ground; the mind is where the openings are. Read every competitor, and the seller, against it.

## Inputs

- `cards/<buyer>.md`
- `outputs/competitor-map.md`
- `outputs/competitors/*.md`
- `outputs/baseline.md`
- `outputs/clues/`, all of them: how each buyer got to the call, what set it off, what was offered
  and how they reacted, and their words

## The gap map

One row per competitor, plus the reference set and the seller's baseline:

| | What they sell | Match | Their angle | Their words | How they reach people | What they assume moves a buyer |

Drop any competitor the read showed does not do the same job for these buyers, and say why.

Then map the gaps, each against the buyer patterns on the card:

1. **Offering gap:** what these buyers need that nobody offers, and what competitors offer that
   these buyers do not need.
2. **Approach gap:** the angles everyone takes (where they crowd), and the angles nobody takes
   (where nobody stands). Which buyer pattern each competitor is really selling to, and which
   patterns nobody sells to.
3. **Language gap:** their words next to the buyers' words, both ways.
   - **Opening:** what buyers say that no competitor claims. Yours to take.
   - **Hollow:** what every competitor claims that buyers never say. Stop saying it.
   - **The logo test:** remove the names; which pages could you tell apart?
4. **Reach gap:** how competitors try to reach people (channel, call to action, price, proof)
   against how these buyers actually came to buy and what proof moved them on the calls.
5. **Mind gap:** what each competitor assumes moves a buyer, against what actually moved these
   buyers. The hardest gap to copy, because closing it means rewriting a whole voice.

Claim "nobody sells to this buyer" only when the competitor map searched that pattern and found
nothing; if it was not searched, say so and search it first. What the seller brings has to rest on
something that happened: a call, a demonstration, a build, the site. If nothing supports it, it is
a claim, not an angle.

Also hold the baseline up to all of it: where the seller sits on the map, which openings it
misses, which hollow lines it repeats.

## Output: `outputs/gaps.md`

Title the file, then write in this order:

1. **Takeaways:** the short answer first. Who the seller is really up against, the gap that
   matters most, and what to do about it, in plain words.
2. **The gap map table.**
3. **The five gaps,** each with buyer quotes (verbatim, file and line) and competitor quotes with
   URLs.
4. **Your positioning against the map.**
5. **Only-we lines:** one per line that passes three tests: the buyers say it (quote), no competitor
   claims it (the map), and the seller can prove it (name what happened that proves it).
   Write it in the buyers' words, then make it sound like the seller. A line that fails the proof
   test is a claim, not a position; say what proof would earn it.
6. **Stop saying:** the hollow lines in the seller's current positioning.

## Last: the synthesis, `outputs/synthesis.md`

The comprehensive report the seller reads first: everything the card, the map, the reads, and the
gaps found, brought together into what it means and what to do.

Write it as a strategist reading patterns across many calls, not as an audit trail. This is
meta-analysis: most of what matters is a read across calls and will not sit on any one line, so say
it plainly and with conviction. Quote buyers where their words carry the point. Competitor quotes
get their URL. Proof gets a short footnote at most. Never turn a read into a list of sources.

In this order:

1. **The short version:** who the buyers are, what the alternatives each fix, and what the seller
   brings that none of them does. Lead with the seller's approach, not the market.
2. **Your buyers, pattern by pattern.** For each: who they are, what they carry, what they feel,
   and the psychology from `references/method.md` in buyer-brain: the forces (push, pull,
   anxiety, habit), which kind of stuck, what they protect, their walls, what counts as proof, the
   reason they would repeat to someone else. Their words throughout.
3. **Who they are up against.** For each competitor: what they sell, their angle in their own
   words, how they reach people, what they assume moves a buyer, which buyer pattern they really
   sell to, and where they fall short. Then what was dropped and why.
4. **What the seller brings that they don't:** from the baseline and the calls (site, pitch,
   demonstrations, what buyers reacted to). Each point names the competitor gap it answers and
   what happened that proves it.
5. **The gaps:** offering, approach, language (opening and hollow), reach, mind, and any buyer
   pattern nobody sells to (only if that pattern was searched).
6. **Angles to take.** Work each buyer pattern through its psychology before writing any angle: read the pattern's forces, stuck, protect, walls, proof, and retell on the card, then ask which lever the seller's approach pulls that no competitor does. Built on buyer psychology: for each angle, the buyer pattern, the lever it
   pulls (which force it calms or strengthens, which stuck it answers, what it protects), what
   competitors pull instead, and the seller's proof. Look for the angle no one is using and
   the one most specific to this seller.
7. **Say this, not that:** buyer words against category words.
8. **How to reach them,** from the card's "How they found you" and the clue files, not generic
   advice: the routes that actually brought these buyers (who introduced them, which people and
   communities send work), the moments that set off each call, the one sentence a referrer can
   repeat, the first offer, and the proof asset to carry. Name the specific routes and moments.
9. **Lines to test,** each passing the three tests.
10. **What to change first:** the concrete next moves on the site, the pitch, and the offer.

Open with one line on what this rests on: how many buyer calls, how many were summaries only, any written buyer words, and whether the card is a Literature Casting hypothesis. Then no more about method.

No em dashes. The only-we lines belong in the user's brand guide, if they keep one.
