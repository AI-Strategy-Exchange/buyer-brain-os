# Buyer Brain OS

Buyer Brain reads your sales and discovery calls to find who your buyers really are: the problems
they carry, in their own words, and what they need to hear. It finds several buyer patterns, not
one averaged persona. Then it maps your real competitors, reads their sites through your buyers'
eyes, and maps the gaps: what your buyers need that nobody offers, the angles everyone takes, the
words nobody uses, and the line only you can say.

It runs in Claude Code, the Claude desktop app, Cowork, or the Codex tab in ChatGPT. Any model
works; Claude gives the best buyer card and synthesis. Everything lives in this folder.

## Setup (10 minutes)

1. Download this folder and open it in Claude Code, the Claude desktop app, Cowork, or Codex.
2. Say "set me up". The intake asks what buyer material you have (calls, summaries, reviews,
   emails) and sorts it into `inputs/`, asks what the calls cannot tell it, records what you
   believe about your buyer today, and checks that your agent can drive your Chrome (Claude in
   Chrome with `claude --chrome`, or the Chrome plugin in Codex). No calls is fine: it runs Max's
   Literature Casting and treats the result as a hypothesis.

## Run it

Tell your agent, in order:

1. "Run buyer brain." Builds `cards/<buyer>.md` from your calls.
   No transcripts? "Run literature casting" first (Max Bernstein's buyer casting from AI Strategy
   Exchange Class 01), then "run buyer brain in hypothesis mode".
2. "Map my competitors." Finds who your buyers would actually pick instead of you, and what each
   one sells, says, and how it reaches people. Drops look-alikes that do a different job.
3. "Read my competitors." Clicks through each site in your Chrome as each buyer pattern.
4. "Run the cross-check." Maps the gaps and ends in the takeaways, your only-we lines, and what
   to stop saying.
5. Optional: "Watch." Goes where your buyers talk to keep their language fresh, and flags
   competitor changes.

Anytime: `python3 scripts/render_report.py` puts everything so far in one page, `outputs/report.html`.

## What you get

- Buyer patterns read across every call: what they carry, fear, tried, and want, in their words
- A map of your real competitors: what they sell, their angle, their words, how they reach people
- A read of every competitor site in your buyers' voice
- The gaps, the takeaways, positioning lines in your buyers' words, and what to stop saying

## The method

Built on decision psychology, buying research, and conversation analysis. How it reads a buyer is in `.agents/skills/buyer-brain/references/method.md`.
