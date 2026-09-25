---
name: intake
description: >-
  Set up Buyer Brain OS for a new buyer: find out what buyer material the user has (calls,
  summaries, reviews, emails), sort it, ask what the calls cannot supply (what they sell, how they
  work, how clients find them), seal what they believe about their buyer before any analysis
  runs, and check the Chrome connection. Writes brief.md. Use when someone opens the folder for
  the first time, says "set me up", "start", "run intake", "help me fill the brief", or when
  brief.md is missing or incomplete.
---

# Intake

Everything downstream is only as good as the brief. The user should never have to fill a form
alone: ask, suggest, and draft, then let them correct. Ask one question at a time and wait for
the answer. Keep questions concrete; a busy person answers "how did your last three clients find
you?" and stalls on "describe your positioning". Write `brief.md` from `templates/brief.md` as you
go.

## 1. What buyer material do they have?

Ask first, because it decides how much else you need to ask: "Do you have recordings,
transcripts, or notes from calls with buyers or clients? Sales calls, discovery calls, kickoffs,
check-ins all count."

If yes, help them get it in and sort it as it arrives:

- Where it usually lives: Zoom cloud recordings (VTT transcript), Fathom, Otter, Fireflies,
  Granola, Google Meet transcripts in Drive, Gong. Tell them how to export from whichever they
  use. Ask for the full transcript, not the AI summary; if a summary is all they have, take it.
- Sort each file as you receive it:
  - Full transcripts go in `inputs/transcripts/`, one folder per client if they can.
  - AI summaries and meeting notes go in `inputs/summaries/`. Their quotes are the tool's
    guesses, not the buyer's words.
  - Calls with no buyer on them (their accountant, a vendor, an internal meeting) stay out. Say
    why in one line.
- Ask what name they go by on the calls, so the seller's lines can be told apart from the
  buyer's.
- More calls is better. It is their own data. If they plan to share the outputs publicly, names
  come out first.

Then, calls or not, ask: "Do you have anything else in your clients' own words? Reviews,
testimonials, emails, DMs, intake-form answers, survey replies." These go in `inputs/written/`.
They are real buyer language and count as evidence. With no calls, they are the main evidence;
push gently for them.

## 2. Seal the belief (before any more questions)

The cross-check needs an honest before-picture: what the user believed about their buyer before
seeing any evidence, and before your questions start shaping their answer. Once they have seen a card, that belief cannot be recovered. Offer the ways
that fit and let them pick:

- **Import what they have.** An ICP, persona, positioning doc, sales notes, or a Literature
  Casting output they already made. Ask for the file or paste. Record its path or content and
  its date.
- **Write it now.** Ask: "In two or three sentences, who is your buyer and why do they buy from
  you?" Take the answer exactly as given. Do not improve it.
- **Run Max's Casting Call.** If they have nothing and no calls, run the Casting Call prompt from
  `.agents/skills/literature-casting/references/prompts.md`. It interviews them and writes a
  buyer brief. Its untouched "what I believed" statement is the sealed belief; do not ask for the
  belief a second time. It also starts the Literature Casting path they need without calls.

Write the belief into brief.md under "What I believe today" with the date and the source. Mark it
SEALED. No step may edit it afterward, and no card is shown to the user until it exists.

## 3. What the calls cannot tell you

Ask, one at a time. With calls, questions 1 and 2 can be skipped and mined from the calls later.
With no calls, they are required: nothing else will supply them.

1. **The offer.** "What do you sell, and who pays you? Paste a list, a link, a rough sentence,
   whatever you have." With calls, add: "Or skip it and I will pull what you offered from your
   calls." Record under "What I sell", with prices if given.
2. **How they work.** Not "what makes you different". Ask: "What do you do on every job that most
   people who sell this skip? How you start, how you deliver, what you refuse to do." If the answer
   is thin, follow up once: "What happens in your first week with a new client?" Record under "How
   I work". It is the yardstick competitor-map matches everyone against.
3. **How clients find them.** "How did your last three clients find you, and what was going on
   for them right before they reached out?" Record under "How clients find me". Ask this even
   with calls; calls rarely show the introduction.
4. **Who they think they compete with.** "Who do you think clients compare you to?" Record it
   under "Who I think I compete with". Competitor-map tests it; it does not steer it.
5. **One client they want more of.** "Think of one specific client who is exactly who you want
   more of. What was going on for them when they came to you?" Context only. The patterns come
   from all the evidence, not this one example.
6. **What they say today.** "Where do you describe what you do today? Your site, LinkedIn, a
   booking page, a pitch you give out loud. Paste or point to anything." No website is fine.
   Record under "My current positioning". It is the baseline the gaps get held against, not
   audited.
7. **Where their buyers are.** Country or region, and local or online. Record it under "Where my
   buyers are".

## 4. Check the Chrome connection

Competitor-read opens competitor sites in the user's own Chrome. Test it now: have the agent open
https://example.com and read back the heading. If it cannot, help them turn one on:

- **Claude:** install the Claude in Chrome extension and sign in with the same Claude account. In
  Claude Code, restart with `claude --chrome`.
- **Codex:** turn on the Chrome plugin or computer use (from a terminal:
  `codex plugin add chrome@openai-bundled`).

Then run step 1 of the `dispatch` skill to see whether both Claude and Codex are here.

## 5. Done

Show them brief.md, then tell them in one line what comes next:

- **Calls:** Buyer Brain reads them.
- **No calls, but written client words:** Literature Casting first, then Buyer Brain on the casting
  plus their written words. The card is a hypothesis, checked against the words they gave.
- **Nothing yet:** Literature Casting, and the card is a hypothesis until real words come in.
