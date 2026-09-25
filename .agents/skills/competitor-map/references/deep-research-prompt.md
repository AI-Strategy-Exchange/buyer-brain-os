# Deep research prompt

Fill every bracket from `brief.md` and the mined buyer mentions. Use the buyer's words, not the
seller's category name. Delete a section only if you have nothing for it. Hand the user the
filled prompt, and only the filled prompt, in one fenced block.

Filling notes:

- **[THE JOB]**: the job line from step 1, in the buyer's words. If there are several buyer
  patterns, list each on its own line.
- **[BUYER QUOTES]**: 3 to 6 short exact quotes where buyers describe the problem or name an
  alternative. No names of people or companies from the calls.
- **[ALREADY NAMED]**: everything buyers and the seller named, one per line, with a few words
  on what happened ("tried and dropped", "compared on a call", "lost a deal to").
- **[WHERE THEY ARE]**: country or region, and online or local.

---

```text
I need to understand who I really compete with, from my buyer's point of view, not from my
industry's point of view.

WHAT I SELL
[One sentence from the brief: what the seller does and who pays.]

MY BUYER
[The one buyer from the brief: role, size of business, situation.] They are in [WHERE THEY ARE].

THE JOB THEY ARE TRYING TO GET DONE, IN THEIR WORDS
[THE JOB]

HOW THEY TALK ABOUT IT
[BUYER QUOTES]

ALTERNATIVES I ALREADY KNOW ABOUT
[ALREADY NAMED]

WHAT I WANT YOU TO FIND
If I disappeared today, what would this buyer do instead? Find everything they might choose to get this job done. Think like the
buyer, not like a market analyst. Include all of these kinds of options:

1. Software or apps they could buy or already have.
2. Companies, agencies, consultants, or firms that do this for businesses like theirs.
3. Freelancers or contractors, including on marketplaces like Upwork or Fiverr.
4. Hiring someone, part-time or full-time. What role would they post, and what does it pay?
5. Doing it themselves: with ChatGPT or other AI tools, templates, courses, or YouTube.
6. Doing nothing and living with the problem. What does that cost them?

Search the way this buyer would search: use their words from above, look at Reddit, forums,
Facebook groups, review sites, and "best way to..." articles. Do not just list the biggest
names in my industry. A famous company that sells to a different kind of buyer does not count.

FOR EACH OPTION YOU KEEP, GIVE ME
- Name
- Kind (software, agency, freelancer, hire, do it yourself, do nothing)
- Website link, or a link to an example (a job posting, a freelancer listing, a tutorial)
- Why this buyer would pick it instead of me, in one or two sentences
- Price, if it is public
- Where you found evidence that buyers like mine actually use or consider it (link)

Then, separately:
- One to three bigger, well-known companies whose promises show what is table stakes for this job. Not rivals, a reference point.
- The options you looked at and left out, with one line on why.

Keep it to the 8 to 12 options that matter most for this buyer. Order them from the one this
buyer is most likely to pick instead of me to the least likely.
```
