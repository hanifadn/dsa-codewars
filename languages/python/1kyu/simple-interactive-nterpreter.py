"""
Title: Simple Interactive Interpreter
Link: https://www.codewars.com/kata/52ffcfa4aff455b3c2000750
Difficulty: 1 kyu

## Description

You will create an interpreter which takes inputs described below and produces outputs, storing state in between each input.

If you're not sure where to start with this kata, check out the "Simpler Interactive Interpreter" kata, which greatly simplifies the interpreter by removing functions.

> **Note**: The `eval` command has been disabled.

## Concepts

The interpreter will take inputs in the language described under the language header below. This section will give an overview of the language constructs.

### Variables

Any identifier which is not a keyword or a function name will be treated as a variable. If the identifier is on the left hand side of an assignment operator, the result of the right hand side will be stored in the variable. If a variable occurs as part of an expression, the value held in the variable will be substituted when the expression is evaluated.

Variables are implicitly declared the first time they are assigned to.

**Example**: Initializing a variable and using it in another expression:
```text
> x = 7
    7
> x + 6
    13
```

Referencing a non-existent variable will cause the interpreter to throw an error. The interpreter should be able to continue accepting input even after throwing.

**Example**: Referencing a non-existent variable:
```text
> y + 7
    ERROR: Invalid identifier. No variable with name 'y' was found.
```

### Assignments

An assignment is an expression that has an identifier on the left side of an `=` operator, and any expression on the right. Such expressions should store the value of the right hand side in the specified variable and return the result.

**Example**: Assigning a constant to a variable:
```text
x = 7
    7
```

Assignments are right-associative and can be chained or nested.

**Example**: Chained assignments:
```text
x = y = 7
    7
```

**Example**: Nested assignments:
```text
x = 13 + (y = 3)
    16
```

### Operator Precedence

Operator precedence follows the common order.

### Functions

Functions are declared by the `fn` keyword followed by a name, an optional argument list, the `=>` operator, and finally an expression.

All function variables are local to the function. References to variables not found in the argument list should result in an error when the function is defined.

**Example**: Average of two variables:
```text
> fn avg x y => (x + y) / 2
> a = 2
    2
> b = 4
    4
> avg a b
    3
```

**Example**: Chain method calls (function calls are right-associative):
```text
> fn echo x => x
> fn add x y => x + y
> add echo 4 echo 3
    7
```

### Name Conflicts

If a variable is declared, a subsequent function with the same name results in an error. Overwriting an existing function name with a new definition is allowed.

## Language Grammar (EBNF)

```ebnf
whitespace      ::= ' ' { whitespace }
function        ::= 'fn'  whitespace  fn-name { whitespace identifier } '=>' expression
fn-name         ::= identifier
expression      ::= factor | expression operator expression
factor          ::= number | identifier | assignment | '(' expression ')' | function-call
assignment      ::= identifier '=' expression
function-call   ::= fn-name { whitespace expression }
operator        ::= '+' | '-' | '*' | '/' | '%'
identifier      ::= (letter | '_') { identifier-char }
identifier-char ::= '_' | letter | digit
number          ::= { digit } '.' digit { digit } | digit { digit } ['.']
letter          ::= 'a' | 'b' | ... | 'z' | 'A' | 'B' | ... | 'Z'
digit           ::= '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'
```

## Operator Precedence

| Category       | Operators    |
|----------------|--------------|
| Multiplicative | *, /, %      |
| Additive       | +, -         |
| Assignment     | =            |
| Function       | =>           |

Division should be float division.
"""

from __future__ import annotations

import re
from typing import Any, NamedTuple

_TOKEN_RE = re.compile(
    r"\s*(=>|[-+*/%=(\)]|[A-Za-z_][A-Za-z0-9_]*|[0-9]*\.?[0-9]+)\s*"
)
_NUMBER_RE = re.compile(r"^\d+(\.\d+)?$")
_IDENT_START_RE = re.compile(r"[A-Za-z_]")
_IDENT_RE = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")

_FN = "fn"
_ARROW = "=>"


def tokenize(expression: str) -> list[str]:
    if not expression:
        return []
    return list(_TOKEN_RE.findall(expression))


def _apply_binary(operator: str, left: Any, right: Any) -> Any:
    if operator == "*":
        return left * right
    if operator == "/":
        return left / right
    if operator == "%":
        return left % right
    if operator == "+":
        return left + right
    if operator == "-":
        return left - right
    raise ValueError(f"Unsupported operator: {operator!r}")


class _FunctionDef(NamedTuple):
    arg_names: tuple[str, ...]
    body: list[str]


class _ExpressionParser:
    """Recursive-descent parser: assignment (right-assoc) → additive → multiplicative → primary."""

    def __init__(
        self,
        interpreter: Interpreter,
        tokens: list[str],
        local_vars: dict[str, Any],
    ) -> None:
        self.interpreter = interpreter
        self.tokens = tokens
        self.local_vars = local_vars
        self.pos = 0

    def parse(self) -> Any:
        result = self.parse_assignment()
        if self.pos != len(self.tokens):
            raise Exception("ERROR: Invalid syntax!")
        return result

    def peek(self) -> str | None:
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def _at_assignment_infix(self) -> bool:
        if self.pos + 1 >= len(self.tokens):
            return False
        if self.tokens[self.pos + 1] != "=":
            return False
        return bool(_IDENT_RE.match(self.tokens[self.pos]))

    def parse_assignment(self) -> Any:
        if not self._at_assignment_infix():
            return self.parse_additive()
        name = self.tokens[self.pos]
        if name in self.interpreter.functions:
            raise Exception("Cannot overwrite function with variable!")
        self.pos += 2
        value = self.parse_assignment()
        self.interpreter.vars[name] = value
        return value

    def parse_additive(self) -> Any:
        left = self.parse_multiplicative()
        while self.peek() in ("+", "-"):
            operator = self.tokens[self.pos]
            self.pos += 1
            right = self.parse_multiplicative()
            left = _apply_binary(operator, left, right)
        return left

    def parse_multiplicative(self) -> Any:
        left = self.parse_primary()
        while self.peek() in ("*", "/", "%"):
            operator = self.tokens[self.pos]
            self.pos += 1
            right = self.parse_primary()
            left = _apply_binary(operator, left, right)
        return left

    def parse_primary(self) -> Any:
        if self.pos >= len(self.tokens):
            raise Exception("ERROR: Invalid syntax!")
        token = self.tokens[self.pos]
        if _NUMBER_RE.match(token):
            return self._consume_numeric_literal(token)
        if token == "(":
            return self._consume_parenthesized_expression()
        if not _IDENT_RE.match(token):
            raise Exception("ERROR: Invalid syntax!")
        return self._resolve_identifier(token)

    def _consume_numeric_literal(self, token: str) -> Any:
        self.pos += 1
        return float(token) if "." in token else int(token)

    def _consume_parenthesized_expression(self) -> Any:
        self.pos += 1
        value = self.parse_assignment()
        if self.peek() != ")":
            raise Exception("ERROR: Unmatched '(' in expression.")
        self.pos += 1
        return value

    def _resolve_identifier(self, token: str) -> Any:
        if token in self.local_vars:
            self.pos += 1
            return self.local_vars[token]
        if token in self.interpreter.vars:
            self.pos += 1
            return self.interpreter.vars[token]
        if token in self.interpreter.functions:
            return self._apply_function_call(token)
        raise Exception(f"ERROR: Invalid identifier. No variable with name '{token}' was found.")

    def _apply_function_call(self, name: str) -> Any:
        self.pos += 1
        function_def = self.interpreter.functions[name]
        argument_values = [self.parse_assignment() for _ in function_def.arg_names]
        bound_locals = dict(zip(function_def.arg_names, argument_values, strict=True))
        inner = _ExpressionParser(self.interpreter, list(function_def.body), bound_locals)
        return inner.parse()


class Interpreter:
    def __init__(self) -> None:
        self.vars: dict[str, Any] = {}
        self.functions: dict[str, _FunctionDef] = {}

    def input(self, expression: str) -> str | Any:
        tokens = tokenize(expression)
        if not tokens:
            return ""

        if tokens[0] == _FN:
            return self._define_function(tokens)

        parser = _ExpressionParser(self, tokens, {})
        return parser.parse()

    def _define_function(self, tokens: list[str]) -> str:
        name, arg_names, body = self._parse_function_declaration(tokens)
        self._validate_function_body_identifiers(body, arg_names)
        self.functions[name] = _FunctionDef(arg_names, body)
        return ""

    def _parse_function_declaration(
        self, tokens: list[str]
    ) -> tuple[str, tuple[str, ...], list[str]]:
        if _ARROW not in tokens:
            raise Exception("Invalid function definition")
        arrow_idx = tokens.index(_ARROW)
        name = tokens[1]
        if name in self.vars:
            raise Exception("Cannot overwrite variable with function!")
        arg_names = tuple(tokens[2:arrow_idx])
        if len(arg_names) != len(set(arg_names)):
            raise Exception("Duplicate parameters specified!")
        body = tokens[arrow_idx + 1 :]
        return name, arg_names, body

    def _validate_function_body_identifiers(
        self, body: list[str], arg_names: tuple[str, ...]
    ) -> None:
        for token in body:
            if not _IDENT_START_RE.match(token):
                continue
            if token in arg_names or token in self.functions:
                continue
            raise Exception(f"ERROR: Invalid identifier '{token}' in function body.")