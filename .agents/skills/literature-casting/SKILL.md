---
name: literature-casting
description: >-
  Find the language your buyer actually uses, by casting them as fictional characters and then
  mining where they talk online without your vocabulary. Runs the full four-stage chain from AI
  Strategy Exchange Class 01: cast five characters from literature who share your buyer's inner
  life, build one ordinary Tuesday around the closest match, map the adjacent communities and
  books where that person shows up, mine one source for raw verbatim quotes, then cross-check the
  fiction against the real language to surface the misdiagnosis. Use when writing a headline,
  hook, subject lines or content angles and the copy sounds like everyone else's; when you have an
  avatar doc that has stopped telling you anything new; when entering a market with no direct
  competitor to mine; or when someone says "cast my buyer", "literature casting", "run the
  fiction thing", "find my buyer's real words", or "what does my buyer actually say". Do not use
  for post-purchase review analysis, for competitor content teardowns, or when you already hold a
  bank of real customer quotes and just need them synthesised.
---

# Literature Casting

Your buyer has already been written. Someone spent four hundred pages inside the head of a person
who shares their ambition, their fear and their daily grind, and got it right, because getting it
right was the whole job.

The catch used to be cost. To use that insight you had to read the books. This runs the chain in
about fifteen minutes instead.

## Before you start

**Run it manually once first.** This skill compresses a class that was taught prompt by prompt on
purpose. If you have never watched the sequence work, the shortcut teaches you nothing about what
is happening underneath, and you will not know when the output is lying to you. The individual
prompts live at https://aistrategyexchange.com/reading-room.

**Web search must be on.** Stages 3 and 4 go looking for real posts. Without live access the model
will invent plausible communities and plausible quotes and will not always tell you it did. In
Claude, check the `+` menu in the chat. If the toggle is greyed out it is disabled at the
organisation level in account settings, not in the chat.

**Ask the user for their avatar doc.** Whatever they have. An ICP, a persona sheet, a positioning
doc, rough notes. If they have nothing, run `references/prompts.md` → Casting Call first, which
interviews them and writes one.

## The chain

Run these in order, in one conversation, feeding each output into the next. Full prompt text is in
`references/prompts.md`. Do not paraphrase the prompts; they are load-bearing.

### Stage 1. Literature Casting and the Tuesday

Two halves with a human decision in the middle.

1. **Before anything else**, have the model read the avatar doc and describe the ordinary Tuesday
   that doc implies, without improving it. This is a before-picture. If the doc is thin, that
   Tuesday comes out thin, and the model should say so plainly. Do not skip this and do not let
   the model flatter the doc. Capture it, then move on.
2. **Cast five characters** who share the buyer's inner life, matched on interior experience
   rather than job title. Supporting characters usually beat protagonists, because the
   protagonist gets the arc and the minor character gets the unguarded moment.
3. **STOP.** The model names the one character it would bet on and asks the user to choose. Wait
   for a real answer. Do not choose on their behalf and do not continue past this point
   unprompted.
4. **Then** write one forgettable Tuesday around the chosen character, and compare it against the
   Tuesday from step 1.

**Why the stop matters.** Casting is divergent, the day is convergent. Without the gate the model
writes the Tuesday while holding all five characters and averages them into a composite human,
which is exactly the mush this exercise exists to avoid. The stop is also the moment the user
stops reading output and starts recognising someone.

The stage ends with ten phrases in the buyer's own words, as one numbered block. That block is the
input to stage 2, so it has to survive a single copy.

### Stage 2. Adjacent Territories

Map where this person discusses the problem without using the seller's vocabulary. Communities,
books, shows, emotional searches, failed solutions.

Push for the surprising ones. If every source returned is an obvious industry forum, the problem
statement is too vague; sharpen it and rerun. Real results from the class included Kitchen
Confidential, *The Bear*, and the "sibling got the business" corner of r/AmITheAsshole for a buyer
who was nothing to do with restaurants or family business.

### Stage 3. The Mining Sprint

Pick **one** source. Extract at least eight verbatim quotes with their typos and bad grammar
intact, tagged by where they would be used.

If the quotes read like marketing copy, the wrong layer is being mined. Push toward comments,
one-star reviews and 2am vent posts. If the model reports it cannot reach Reddit or Fishbowl, do
not accept remembered quotes; switch to a model with live access or pick a different source, and
tell the user which you did.

### Stage 4. The Cross-Check

Hold the mined quotes against the character insight, plus what the user believed before starting.

The output that matters is the misdiagnosis: what the buyer thinks the problem is, what it
actually is, and why they miss it. Where the timeless want from the fiction and this week's
language from the mining agree, that overlap is the message.

## Then produce something

Do not stop at insight. Insight is not an artifact. Close by producing one finished thing:

- a headline
- an opening hook
- three subject lines
- three content angles

Use the buyer's words, then make it sound like the user. If it still reads like the model wrote
it, it is not finished.

## Rules

- **Never invent a line.** If quoting a novel or play, quote exactly and mark it as a quote. If
  unsure of the wording, paraphrase and say so. Someone will check.
- **Mark anything invented.** At the end of stage 1, flag every element not supported by what the
  user provided. The output is persuasive enough to feel like research, and someone will carry it
  into a sales call. This line is what keeps it a thinking tool.
- **Push past the first abstraction.** "They want to be seen" is not a common thread. Keep going
  until you reach something specific enough that it would be wrong for a different buyer.
- **Do not average the five characters.** One person, chosen by the user.
- **Say what the user should stop saying.** The half of the takeaway that does real work is the
  one naming something they are doing right now.

## Notes

- Sonnet handles this fine. Larger models are slower here without being better.
- Agents make this much faster than a browser chat, because the stages can run in parallel where
  they do not depend on each other. The class ran in a browser and spent half its time waiting.
- Two audiences? Run the whole chain twice, once each, then look at the overlap. The overlap is
  usually the content.
- Feed anything good back into a master context file for that buyer, or it gets buried.

Source: AI Strategy Exchange Class 01, 2026-08-07. Prompts: https://aistrategyexchange.com/reading-room
