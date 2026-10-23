# Badge Math

Event badge pack, lanyard, cost and time arithmetic. The 240 attendees at 25 badges a pack take 10 packs, the last pack holding 15 badges.

## Named constants

None. Every number is the owner's own entry.

## What it computes

- **The packs truth** - the attendees (1 to 1000000) divided by the badges a pack (1 to 1000), rounded up, with what the last pack holds.
- **The lanyards truth** - the attendees divided by the lanyards a bag (1 to 1000), rounded up, with the lanyards left spare.
- **The cost truth** - the packs (1 to 100000) times the pack price ($0.01 to $999.99) to the cent, and spread over the attendees, half rounded up.
- **The time truth** - the badges divided by the badges printed a minute (1 to 100), rounded up, in minutes and in hours and minutes.

## Boundary

Arithmetic only. Counting applied as written. It has not seen any badge, pack or printer and does not know whether badges will really arrive on time, a printer will jam or a price will hold, and it gives no verdict that a pack is worth its price or a badge is right for an event. Every number is the owner's own entry.

## Files

- `index.html` - landing page with the boundary and starting examples.
- `app.html` - the calculator; every box recomputes on each keystroke.
- `engine.js` - the four truths, shared by the page and the tests.
- `oracle.py` - an independent Python re-implementation; writes `expected.json`.
- `test.js` - runs the engine against `expected.json` (98 cases, 20 error cases).

## Tests

```
python3 oracle.py
node test.js
```
