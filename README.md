# T-Shirt Math

Event t-shirt box, week, cost and time arithmetic. The 345 shirts at 25 shirts a box take 14 boxes, the last box holding 20 shirts.

## Named constants

None. Every number is the owner's own entry.

## What it computes

- **The boxes truth** - the shirts (1 to 1000000) divided by the shirts a box (1 to 1000), rounded up, with what the last box holds.
- **The weeks truth** - the shirts divided by the shirts used a week (1 to 100000), with the shirts left for the next week.
- **The cost truth** - the boxes (1 to 100000) times the box price ($0.01 to $999.99) to the cent, and spread over the shirts, half rounded up.
- **The time truth** - the shirts divided by the shirts shirted a minute (1 to 100), rounded up, in minutes and in hours and minutes.

## Boundary

Arithmetic only. Counting applied as written. It has not seen any shirt, box or folding table and does not know whether shirts will really arrive unwrinkled, sizes will run out or a price will hold, and it gives no verdict that a box is worth its price or a shirt is right for an event. Every number is the owner's own entry.

## Files

- `index.html` - landing page with the boundary and starting examples.
- `app.html` - the calculator; every box recomputes on each keystroke.
- `engine.js` - the four truths, shared by the page and the tests.
- `oracle.py` - an independent Python re-implementation; writes `expected.json`.
- `test.js` - runs the engine against `expected.json` (99 cases, 20 error cases).

## Tests

```
python3 oracle.py
node test.js
```
