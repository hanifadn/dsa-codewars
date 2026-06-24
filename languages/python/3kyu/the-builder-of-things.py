"""
Title: The builder of things
Link: https://www.codewars.com/kata/5571d9fc11526780a000011a
Difficulty: 3 kyu

Sentence-like DSL: is_a / is_not_a, is_the / being_the / and_the, has / having / with,
each, can (with optional archives). See the kata for full examples.
"""

from __future__ import annotations

from collections.abc import Callable, Iterator, Sequence


class Thing:
    def __init__(self, name: str) -> None:
        self.name = name

    def __getattr__(self, name: str) -> object:
        if name == "is_a":
            return _BoolChain(self, True)
        if name == "is_not_a":
            return _BoolChain(self, False)
        if name in ("is_the", "being_the", "and_the"):
            return _BeingThe(self)
        if name in ("has", "having", "with"):
            return lambda n: _Has(self, n)
        if name == "can":
            return _Can(self)
        raise AttributeError(name)


def _tag_is(thing: Thing, predicate: str, value: bool = True) -> None:
    object.__setattr__(thing, f"is_{predicate}", value)


def _singular_from_attr(attr: str, count: int) -> str:
    if count > 1 and attr.endswith("s"):
        return attr[:-1]
    return attr


class ThingSequence(Thing, Sequence):
    def __init__(self, name: str, items: list[Thing]) -> None:
        super().__init__(name)
        object.__setattr__(self, "_items", items)

    def __len__(self) -> int:
        return len(self._items)

    def __getitem__(self, index: int | slice) -> Thing | list[Thing]:
        return self._items[index]

    def __iter__(self) -> Iterator[Thing]:
        return iter(self._items)

    def each(self, fn: Callable[[Thing], None]) -> ThingSequence:
        for item in self._items:
            fn(item)
        return self


class _BoolChain:
    def __init__(self, thing: Thing, truth: bool) -> None:
        self._thing = thing
        self._truth = truth

    def __getattr__(self, noun: str) -> Thing:
        object.__setattr__(self._thing, f"is_a_{noun}", self._truth)
        object.__setattr__(self._thing, f"is_not_a_{noun}", not self._truth)
        return self._thing


class _BeingThe:
    def __init__(self, thing: Thing) -> None:
        self._thing = thing

    def __getattr__(self, prop_name: str) -> _BeingTheValue:
        return _BeingTheValue(self._thing, prop_name)


class _BeingTheValue:
    def __init__(self, thing: Thing, prop_name: str) -> None:
        self._thing = thing
        self._prop_name = prop_name

    def __getattr__(self, value_name: str) -> Thing:
        object.__setattr__(self._thing, self._prop_name, value_name)
        return self._thing


class _Has:
    def __init__(self, thing: Thing, count: int) -> None:
        self._thing = thing
        self._count = count

    def __getattr__(self, attr: str) -> Thing | ThingSequence:
        n = self._count
        base = _singular_from_attr(attr, n)

        if n > 1:
            items = []
            for _ in range(n):
                child = Thing(base)
                _tag_is(child, base)
                items.append(child)
            seq = ThingSequence(attr, items)
            _tag_is(seq, attr)
            object.__setattr__(self._thing, attr, seq)
            return seq

        child = Thing(base)
        _tag_is(child, base)
        object.__setattr__(self._thing, attr, child)
        return child


class _Can:
    def __init__(self, thing: Thing) -> None:
        self._thing = thing

    def __getattr__(self, verb: str) -> Callable[..., Thing]:
        def register(*args: object) -> Thing:
            callables = [a for a in args if callable(a)]
            if len(callables) != 1:
                raise TypeError("can.<verb> expects exactly one callable in its arguments")
            fn = callables[0]
            archives = [a for a in args if isinstance(a, str)]
            history: list[object] | None = [] if archives else None

            def bound(*call_args: object, **kwargs: object) -> object:
                out = fn(self._thing, *call_args, **kwargs)
                if history is not None:
                    history.append(out)
                return out

            object.__setattr__(self._thing, verb, bound)
            if history is not None:
                for archive_name in archives:
                    object.__setattr__(self._thing, archive_name, history)

            return self._thing

        return register
