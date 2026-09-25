---
name: buyer-brain
description: Get inside the buyer's head from sales and discovery call transcripts. Reads across every call to work out who the buyer really is, the several problems they carry, what they tried, what they fear, what they protect, what success means to them, and what they are really asking for underneath what they say. Produces buyer patterns that competitor-read and cross-check use to find positioning gaps. Use for "run buyer brain", buyer analysis, voice of the buyer, or pain points from calls. With no transcripts, runs on Literature Casting output.
---

# Buyer Brain

This is a meta-analysis of the buyer. Read across every call and work out what is going on inside these people: what they are really dealing with, why it matters to them, what they have not said out loud, and what would make them feel understood. The transcripts are the raw material; the insight is yours. Go deep, interpret, connect dots across calls, and commit to a read.

People are complicated. One buyer carries several problems at once, and they can pull against each other. Buyers from very different businesses and call types often circle the same few underlying problems. Find both.

The point of all of it: know the buyer well enough to read every competitor site through their eyes and see what nobody is saying to them.

Read `references/method.md` first. Read `brief.md`, then write `cards/<buyer>.md` from `templates/buyer-card.md`.

## Workflow

1. **Read every call and every written word.** Any call with a buyer in it counts, whatever the business or call type: `inputs/transcripts/` and `inputs/summaries/`. Read `inputs/written/` (reviews, emails, testimonials) too, one clue file per source. For each, write `outputs/clues/<call>.md` (`references/clue-file.md`): their switch story and the forces on it, every problem with its consequence, what they tried and do instead, what they protect, which kind of stuck they are in, their walls, the ask versus the need, who they answer to and the reason they would retell, what counts as proof, and for services what would make an outsider feel safe, plus what the seller offered and how they reacted. Then your read of what is underneath it all. Pull their best lines verbatim. Bad speaker labels (single mic, everyone "Speaker 1") are not a reason to skip: work out who is talking from what they say, mark it as likely, and keep going. Summaries and meeting notes count too; analyze them, but their quotes are the tool's wording, so never present them as the buyer's.
2. **Read across the calls.** Work out the underlying problems that keep showing up in different clothes. Name several buyer patterns if the calls hold several, by situation and what is at stake, not personality. One person can sit in several. Keep the outliers; one person saying something sharply that nobody else says can be the opening.
3. **Build the voice-of-buyer bank.** The phrases that recur, verbatim, grouped by pattern. The phrases buyers volunteered carry more weight than ones they echoed back from the seller.
4. **Write the card.** Who the buyer is, pattern by pattern. For each, what a competitor's page would have to say for this buyer to feel understood, in their words. That list is what competitor-read tests and cross-check turns into gaps. If "What I sell" in brief.md is empty, fill it from the "What was offered" sections, marked as mined from calls. Put anything only the seller could clear up (unresolved shorthand, who a name refers to) under open questions; do not stop to ask.

## Thin evidence

With fewer than about eight buyer calls, give each pattern the number of calls behind it and call
it a hypothesis to test on the next calls. A pattern resting on one person is still worth naming.

## Literature Casting mode

When there are no calls, run the same workflow on the Literature Casting output
(`outputs/literature-casting.md`) plus anything in `inputs/written/`. Written buyer words outrank
the fiction: where they disagree, the written words win. Mark the patterns as hypotheses to test on
real calls, and label cast lines as cast, not buyer quotes.

When the casting asks the user to pick one character, describe each character first as a person
in the buyer's world (their job, their week, what they would never admit), then the book. Most
users will not know the books.

## Keep straight

- Buyer quotes are verbatim. Your interpretation is yours; say it plainly and own it.
- Facts about the seller's business the calls do not contain (who signed, what was sent later) come from the seller, not from you.
- Two helpers catch mechanical slips; they judge nothing about the analysis. `scripts/check_quotes.py outputs/clues inputs` lists quoted lines not found verbatim, and marks ones found only in a summary. `scripts/check_generic.py outputs/clues` lists clue files that share sentences with other calls. A clue file that could describe any call describes none.
- No em dashes.
