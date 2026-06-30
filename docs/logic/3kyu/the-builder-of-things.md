# The builder of things

| Field | Value |
|-------|-------|
| Slug | the-builder-of-things |
| Kyu | 3 |
| Link | https://www.codewars.com/kata/5571d9fc11526780a000011a |
| Status | backfilled |
| Reference | languages/python/3kyu/the-builder-of-things.py |

## Summary

Implement a fluent DSL for constructing `Thing` objects via chained attribute access. Support boolean tagging (`is_a` / `is_not_a`), property assignment (`is_the` / `being_the` / `and_the`), owned sub-things (`has` / `having` / `with`), plural collections, iteration (`each`), and callable registration (`can` with optional archives).

## Input / Output

- **Input:** Chained method/property calls on `Thing(name)` instances (language-specific syntax).
- **Output:** Mutated `Thing` (or `ThingSequence`) with dynamic attributes reflecting the chain.
- **Constraints:** Method chaining returns the parent or child as specified below; `can` requires exactly one callable among its arguments.

## Examples

| Chain (conceptual) | Effect |
|--------------------|--------|
| `Thing("human").is_a.great.father` | Sets `is_a_great`, `is_a_father` true; `is_not_a_*` false |
| `Thing("human").has(2).arms` | Creates `ThingSequence` of 2 `Thing("arm")`, sets `is_arm` on each and parent |
| `thing.can.fly(lambda t: ...)` | Binds `fly` on thing; optional archive list stores call results |

## Edge Cases

- `is_not_a.X` sets `is_a_X` false and `is_not_a_X` true.
- Count 1 → single child `Thing`; count > 1 → `ThingSequence` iterable.
- Plural attribute name on parent; singular name for each child (`arms` → child type `arm`).
- `can.verb(fn, "archive")` appends return values to list at `archive`.
- `each(fn)` runs `fn` on every item in a sequence, returns the sequence.

## Approach

- **Algorithm:** `__getattr__` dispatch returns small chain objects (`_BoolChain`, `_BeingThe`, `_Has`, `_Can`) that set attributes via `object.__setattr__` and return `self` or children for chaining.
- **Time:** O(chain length + collection size)
- **Space:** O(number of created things)

## Behavioral Contract

- Dynamic attrs: `is_<noun>` bools from `is_a`/`is_not_a`; arbitrary property names from `being_the`; child attrs from `has`.
- `ThingSequence` supports `len`, indexing, iteration, and `each`.
- `can`: exactly one callable in args; strings name archive lists (empty list, append on each call).
- Chains are side-effecting on the thing; return value enables further chaining.

## Pseudocode

```text
CLASS Thing(name):
  ON unknown attr name:
    IF name IN {is_a, is_not_a}: RETURN BoolChain(self, truth)
    IF name IN {is_the, being_the, and_the}: RETURN BeingThe(self)
    IF name IN {has, having, with}: RETURN LAMBDA count: Has(self, count)
    IF name == can: RETURN Can(self)
    RAISE unknown attribute

CLASS BoolChain(thing, truth):
  ON noun attr:
    SET thing.is_a_<noun> = truth
    SET thing.is_not_a_<noun> = NOT truth
    RETURN thing

CLASS BeingThe(thing):
  ON propertyName: RETURN BeingTheValue(thing, propertyName)

CLASS BeingTheValue(thing, prop):
  ON valueName:
    SET thing[prop] = valueName
    RETURN thing

CLASS Has(thing, count):
  ON attrName:
  base = singular(attrName) if count>1 and attr ends with 's' else attrName
    IF count > 1:
      items = [Thing(base) with is_<base> tagged for _ in 1..count]
      seq = ThingSequence(attrName, items); tag seq.is_<attrName>
      SET thing[attrName] = seq; RETURN seq
    ELSE:
      child = Thing(base); tag child; SET thing[attrName] = child; RETURN child

CLASS Can(thing):
  ON verb:
    RETURN register(args):
      fn = exactly one callable in args
      archives = string names in args
      history = [] if archives else None
      bound = LAMBDA *a, **kw:
        out = fn(thing, *a, **kw)
        IF history: APPEND out TO history
        RETURN out
      SET thing[verb] = bound
      FOR name IN archives: SET thing[name] = history
      RETURN thing
```

## Walkthrough

`Thing("human").has(2).arms`:

1. `has(2)` → `_Has` with count 2.
2. `.arms` → create two `Thing("arm")`, tag `is_arm`, wrap in `ThingSequence("arms", items)`, set `human.arms = seq`, return seq.

## Codewars

| Language | Entry point | Notes |
|----------|-------------|-------|
| JavaScript | `Thing` | Dynamic `__getattr__` equivalent |
| Python | `Thing` | `__getattr__` chaining DSL |
