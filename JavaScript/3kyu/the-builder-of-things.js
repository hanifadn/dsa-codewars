/**
 * Title: The builder of things
 * Link: https://www.codewars.com/kata/5571d9fc11526780a000011a
 * Difficulty: 3 kyu
 *
 * Sentence-like DSL (is_a, is_the, has/having, each, can, …). See Codewars for examples.
 */

const BARE = Symbol('thingBare');

const EACH_GLOBAL_KEYS = ['having', 'being_the', 'and_the'];

function bareOf(x) {
  return x && x[BARE] ? x[BARE] : x;
}

function defGet(obj, key, get, enumerable = false) {
  Object.defineProperty(obj, key, { get, enumerable, configurable: true });
}

function emptyProxy(handlers) {
  return new Proxy({}, handlers);
}

function singularFromAttr(attr, count) {
  return count > 1 && attr.endsWith('s') ? attr.slice(0, -1) : attr;
}

function invokeCanHandler(self, fn, callArgs) {
  const g = typeof globalThis !== 'undefined' ? globalThis : {};
  const prev = g.name;
  g.name = self.name;
  try {
    return fn.apply(self, callArgs);
  } finally {
    g.name = prev;
  }
}

function eachOnArray(arr) {
  return (callback) => {
    const g = typeof globalThis !== 'undefined' ? globalThis : global;
    const saved = Object.fromEntries(EACH_GLOBAL_KEYS.map((k) => [k, g[k]]));
    try {
      for (const item of arr) {
        g.having = (n) => item.has(n);
        g.being_the = item.being_the;
        g.and_the = item.and_the;
        callback(item);
      }
    } finally {
      EACH_GLOBAL_KEYS.forEach((k) => {
        g[k] = saved[k];
      });
    }
  };
}

function canProxy(rawSelf) {
  const self = bareOf(rawSelf);
  return emptyProxy({
    get(_, verb) {
      return (...args) => {
        const last = args[args.length - 1];
        const fn = typeof last === 'function' ? last : null;
        const archives = fn ? args.slice(0, -1) : [];
        const history = archives.length ? [] : null;

        archives.forEach((archiveName) => {
          defGet(self, archiveName, () => history, true);
        });

        const method = function (...callArgs) {
          if (!fn) return undefined;
          const out = invokeCanHandler(self, fn, callArgs);
          if (history) history.push(out);
          return out;
        };

        Object.defineProperty(self, verb, {
          value: method,
          writable: true,
          enumerable: true,
          configurable: true,
        });
      };
    },
  });
}

function Thing(name) {
  const bare = Object.create(Thing.prototype);
  bare.name = name;
  return createThingProxy(bare);
}

function createThingProxy(self) {
  self[BARE] = self;

  const booleanMode = (truth) =>
    emptyProxy({
      get(_, noun) {
        defGet(self, `is_a_${noun}`, () => truth);
        defGet(self, `is_not_a_${noun}`, () => !truth);
        return createThingProxy(self);
      },
    });

  const propertyWithValue = (rawTarget = self) => {
    const target = bareOf(rawTarget);
    return emptyProxy({
      get(cache, propName) {
        if (!Object.prototype.hasOwnProperty.call(cache, propName)) {
          cache[propName] = emptyProxy({
            get(_, valueName) {
              defGet(target, propName, () => valueName, true);
              return emptyProxy({
                get(__, next) {
                  if (next === 'and_the') return propertyWithValue(target);
                  return createThingProxy(target)[next];
                },
              });
            },
          });
        }
        return cache[propName];
      },
    });
  };

  const makeHas = (rawOwner) => {
    const owner = bareOf(rawOwner);
    return (count) =>
      emptyProxy({
        get(_, attr) {
          const childBase = singularFromAttr(attr, count);

          const makeChild = () => {
            const child = new Thing(childBase);
            defGet(child, 'with', () => child.having, true);
            defGet(child, 'being_the', () => propertyWithValue(child), true);
            defGet(child, 'is_the', () => propertyWithValue(child), true);
            defGet(child, 'and_the', () => propertyWithValue(child), true);
            defGet(child, 'having', () => makeHas(child), true);
            defGet(child, 'has', () => makeHas(child), true);
            defGet(child, 'can', () => canProxy(child), true);
            return child;
          };

          if (count > 1) {
            const items = Array.from({ length: count }, makeChild);
            defGet(items, 'each', () => eachOnArray(items), false);
            owner[attr] = items;
            return items;
          }

          const one = makeChild();
          owner[attr] = one;
          return one;
        },
      });
  };

  defGet(self, 'is_a', () => booleanMode(true));
  defGet(self, 'is_not_a', () => booleanMode(false));
  defGet(self, 'is_the', () => propertyWithValue(self));
  defGet(self, 'being_the', () => propertyWithValue(self));
  defGet(self, 'and_the', () => propertyWithValue(self));
  defGet(self, 'has', () => makeHas(self));
  defGet(self, 'having', () => makeHas(self));
  defGet(self, 'can', () => canProxy(self));

  const proxy = new Proxy(self, {
    get(target, prop, receiver) {
      if (prop === 'name') return target.name;
      return Reflect.get(target, prop, receiver);
    },
    set(target, prop, value, receiver) {
      return Reflect.set(target, prop, value, receiver);
    },
  });
  proxy[BARE] = self;
  return proxy;
}

module.exports = Thing;
