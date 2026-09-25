---
name: competitor-map
description: >-
  Find and map the seller's real competitors from the buyer's seat: what each one actually sells,
  whether it does the same job for these buyers, the angle it takes, the words it uses, and how it
  reaches people. Keeps only true competitors (including doing nothing and doing it themselves) and
  drops look-alikes with the reason. Use after buyer-brain and before competitor-read, or when
  someone says "find my competitors", "map my competitors", "who am I really up against", or
  "my competitor list is too obvious".
---

# Competitor Map

The question: if this seller disappeared today, what would these buyers do instead? The answer is
rarely the companies in the seller's category. It is the spreadsheet, the owner answering every
question, ChatGPT in a tab, a freelancer, a coach, an agency, or living with it.

A name is only a competitor if these buyers would pick it instead of the seller to get the same
job done. Software is usually not a competitor: the seller builds with it or on it, and a buyer who
buys it still needs someone to make it work. Software counts only as the do-it-yourself option (the
buyer buys a tool and does the work themselves), and then as one row, not one row per product.

Read `brief.md` ("What I sell" and "My current positioning") and `cards/<buyer>.md`. If there is no
card, run `buyer-brain` first, or Literature Casting if there are no calls.

## 1. Know the seller's offer and approach first

Before looking at anyone else, write down what the seller actually sells and how they do it
differently, from `brief.md` ("What I sell", "My current positioning"), the seller's site, and how
they pitch on calls (the "What was offered, and how they reacted" sections of `outputs/clues/`):
what they deliver, how they work, what they demonstrate, and what buyers reacted to. One short
paragraph. This is the yardstick for every match.

## 2. Mine what buyers said

From the card, the clue files, and the transcripts (`rg --no-ignore`), pull every time a buyer
names or describes something other than the seller: tools, vendors, agencies, consultants, people
they hired or would hire, doing it themselves, waiting or living with it. Keep the quote and the
file.

Write the job each buyer pattern is trying to get done, in the buyer's words. That line drives the
search and the match test.

## 3. Look outward

Search two ways.

**Direct competitors:** firms that sell what the seller sells, the way the seller sells it. Follow
`references/direct-search.md`: design the queries by the seller's approach in plain words, never
the category name, then follow each close candidate to the next until the search saturates. Keep
as many as pass the match test. If the time runs short, record where the frontier stopped. The
search can be resumed or widened any time later from that record; offer it, do not block on it.

**Same-job alternatives:** go pattern by pattern, and cover every pattern on the card. For each buyer pattern, ask what that person hires or buys when the pain
peaks, by name: the method, coach, or fractional executive; the agency or consultant who would take
the job; the platform that promises to fix it without anyone.

Search with your web tools, in the buyer's words and job, never the seller's category name. Look
where these buyers talk: forums, Reddit, Facebook groups, reviews.

Then offer an optional wider sweep: fill `references/deep-research-prompt.md` and give the user the
finished prompt in one fenced block, with: "Optional: paste this into ChatGPT, Claude, or Gemini
with deep research on for a wider sweep, then paste the answer back here." Merge what it adds. If
you have no web tools, this prompt is how the outward search happens.

## 4. Map each candidate

Open each candidate's site and fill one row:

- **What they actually sell:** the service or product, in plain words.
- **Who it is for:** size, role, situation.
- **The job it does:** in the buyer's terms.
- **Match:** does it do the same job for these buyers as the seller does?
  - **Direct:** sells what the seller sells, the way the seller sells it, to these buyers.
    Compare against the approach paragraph from step 1, not just the category.
  - **Direct for one pattern:** direct only for a buyer who has already narrowed the job (for
    example, one who already knows they need a technical connection). Name the pattern.
  - **Same job, different service:** a coach, a tool, a platform, or a hire that solves the same
    problem another way.
  - **Status quo or do-it-yourself:** what they keep doing.
  - **No match:** a different job, a different buyer, or software the seller would build on. Drop it.
  - **Gone:** no longer sold (shut down, discontinued, a course that stopped running). Check each
    candidate is on sale today. A gone option a buyer named is buyer history: keep it in the
    card's "what they tried", not in the map.
  - A service that comes bundled with software (a payroll company with HR advisors, a platform
    with done-for-you setup) is judged on the service: if it does the job for these buyers, it is
    a same-job alternative.
- **Their angle:** what they lead with and why they say a buyer should pick them.
- **Their words:** the headline and main promise, quoted exactly, with the URL.
- **How they reach people:** the main call to action, price if visible, proof, and the channel
  they sell through (referral, content, ads, marketplace, directory).

Every buyer pattern needs at least one searched competitor or an explicit "searched, found
nothing" note with the queries you ran. Keep 5 to 8 that match overall, plus doing nothing and one do-it-yourself option unless nothing
supports them. Rank by how close each is to what these buyers already do.

Separately, pick one to three bigger names these buyers actually see, at their size and in their
world, as the **reference set**: the firm their peers hire, the name their industry or community
recommends, a name that came up on the calls. For each, say which buyer pattern sees it and why. A
global consultancy these buyers would never call is not a reference. Their words show what is table
stakes.

## 5. Hand off

Write `outputs/competitor-map.md`:

```markdown
# Competitor map for <buyer>

**What the seller sells and how:** <the approach paragraph from step 1>

**The job, in the buyer's words:** <one line per pattern>

| Competitor | What they sell | Match | Their angle | Their words | How they reach people |
| --- | --- | --- | --- | --- | --- |

## Why each one is here
### <name> (<direct | direct for <pattern> | same job, different service | status quo | do-it-yourself>)
- **Open:** <URL, or the stand-in>
- **Why these buyers would pick it:** <one sentence>
- **Came from:** <buyer quote and file | search, with URL>

## Reference set (table stakes)
- <name>, <URL>: <their words>. Seen by: <pattern>, because <why>

## Dropped, and why
- <name>: <different job or different buyer>
```

Replace "Competitors to read" in `brief.md` with the kept list and the reference set.

## Gotchas

- Doing it themselves and doing nothing have no website. Give competitor-read a stand-in: for
  do-it-yourself, the product page plus a popular tutorial the buyer would find; for a freelancer,
  a real listing for the buyer's job; for a hire, a real job posting; for doing nothing, the
  buyers' own words on what it costs them.
- A tool a buyer already uses (their CRM, workspace, accounting software) is where the seller's
  work lands, not a competitor. Put it under "Dropped, and why".
- Deep research returns long, confident lists of category players. Most fail the match test.
- Small independent sellers have no G2 page. Read reviews only where they exist; transcripts come
  first.
- No em dashes.
