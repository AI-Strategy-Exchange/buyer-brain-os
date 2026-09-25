# Direct competitor search

The goal: every firm these buyers could hire that sells what the seller sells, the way the seller
sells it. Three queries find the loudest category players, who usually fail the match test. The
real direct competitors are small, named in plain words, and found by following one to the next.
Expect this to take a long time. Keep going.

## 1. Design the queries first

Write the set down before searching, in `outputs/competitors/direct-search.md`, so the next run
sees what was asked. Build it from the approach paragraph and the buyers' words, never from the
seller's category name alone. Several shapes:

- **The approach in plain words:** what the seller does and how, the way a buyer would describe it
  to a friend ("builds AI inside the tools we already use", "small pilot before the big build").
- **The buyer asking:** how someone with this problem would search for help, from each buyer
  pattern's seat ("stop being the bottleneck in my business", "team re-types everything twice").
- **The outcome without the category:** the result the buyer wants, with no industry words.
- **The shape of the offer:** the first step the seller sells (a paid pilot, a two-week build, a
  fixed-price first piece) plus the kind of buyer.
- **Where firms list themselves:** agency directories, marketplaces, partner lists, and
  "top firms for" pages, searched with the approach words.
- **Lookalikes of what you already have:** "<competitor> alternative", "companies like
  <competitor>", and each kept firm's own category words.
- **Control, run last:** the seller's category vocabulary. If it returns more matches than the
  other shapes, you are reading marketing, not finding the firms buyers meet.

Make each string searchable: keep the distinctive two to four words, drop the rest. A full
sentence matches almost nothing. A shape that returns nothing is more often a bad string than an
empty market: shorten it and run it again before recording the silence.

## 2. Work a frontier

A result list is a set of starting points. For each candidate that looks close, open its site and
test it against the approach paragraph (the Match rules in the skill). Then expand from it:

- Who it names as partners, peers, or "we are different from".
- Its directory or marketplace listing, and the similar firms listed beside it.
- Its founders' other places: podcast guests, newsletters, communities, and who else appears there.
- Its case-study clients: who else they hired or mention.
- New words it uses for the same approach: run them as their own queries.

Add each new lead to the frontier. Near misses count as leads: a firm that almost matches often
sits next to one that does.

## 3. Stop at saturation

A branch is one lead followed out from a firm you already opened: its partner page, the directory
page it sits on, a founder's podcast episode, a case-study client, a new phrase run as a query.
Opening the candidates themselves is not a branch, and neither is searching a firm's name or
"<firm> alternative". Keep expanding until five branches in a row turn
up no new firm that passes the match test. Record each branch and what it yielded. Do not stop at
a fixed count, and do not stop at the first good match.

## 4. Record the exploration

In `outputs/competitors/direct-search.md`: the query set, which leads were opened, which branches
were followed or abandoned and why, every candidate with its match verdict and URL, and where the
search saturated. The next run starts from there instead of repeating the first page.

Add each firm that passes to `outputs/competitor-map.md` with its row, then hand the new names to
competitor-read.
