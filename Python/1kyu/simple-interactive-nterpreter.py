"""
Title: Simple Interactive Interpreter
Link: https://www.codewars.com/kata/52ffcfa4aff455b3c2000750
Difficulty: 1 kyu

Description:
Task
You will create an interpreter which takes inputs described below and produces outputs, storing state in between each input.

If you're not sure where to start with this kata, check out my Simpler Interactive Interpreter kata, which greatly simplifies the interpreter by removing functions.

Note that the eval command has been disabled.

Concepts
The interpreter will take inputs in the language described under the language header below. This section will give an overview of the language constructs.

Variables
Any identifier which is not a keyword or a function name will be treated as a variable. If the identifier is on the left hand side of an assignment operator, the result of the right hand side will be stored in the variable. If a variable occurs as part of an expression, the value held in the variable will be substituted when the expression is evaluated.

Variables are implicitly declared the first time they are assigned to.

Example: Initializing a variable to a constant value and using the variable in another expression (Each line starting with a '>' indicates a separate call to the input method of the interpreter, other lines represent output)

>x = 7
    7
>x + 6
    13    
Referencing a non-existent variable will cause the interpreter to throw an error. The interpreter should be able to continue accepting input even after throwing.

Example: Referencing a non-existent variable

>y + 7
    ERROR: Invalid identifier. No variable with name 'y' was found."
Assignments
An assignment is an expression that has an identifier on left side of an = operator, and any expression on the right. Such expressions should store the value of the right hand side in the specified variable and return the result.

Example: Assigning a constant to a variable

x = 7
    7
You should also be able to chain and nest assignments. Note that the assignment operator is one of the few that is right associative.

Example: Chained assignments. The statement below should set both x and y to 7.

x = y = 7
    7
Example: Nested assignments. The statement below should set y to 3, but it only outputs the final result.

x = 13 + (y = 3)
    16
Operator Precedence
Operator precedence will follow the common order. There is a table in the Language section below that explicitly states the operators and their relative precedence.

Functions
Functions are declared by the fn keyword followed by a name, an optional arguments list, the => operator, and finally an expression. All function variables are local to the function. That is, the only variable names allowed in the function body are those declared by the arguments list. If a function has an argument called 'x', and there is also a global variable called 'x', the function should use the value of the supplied argument, not the value of the global variable, when evaluating the expression. References to variables not found in the argument list should result in an error when the function is defined.

Example: declare a function to calculate the average of two variables and call it. (Each line starting with a '>' indicates a separate call to the input method of the interpreter, other lines represent output)

>fn avg => (x + y) / 2
    ERROR: Unknown identifier 'x'
>fn avg x y => (x + y) / 2
>a = 2
    2
>b = 4
    4
>avg a b
    3 
Example: declare a function with an invalid variable name in the function body

>fn add x y => x + z
    ERROR: Invalid identifier 'z' in function body.
Example: chain method calls (hint: function calls are right associative!)

>fn echo x => x
>fn add x y => x + y
>add echo 4 echo 3
    7
Name conflicts
Because variable and function names share the same grammar, conflicts are possible. Precedence will be given to the first object declared. That is, if a variable is declared, then subsequent declaration of a function with the same name should result in an error. Likewise, declaration of a function followed by the initialization of a variable with the same name should result in an error.

Declaration of function with the same name as an existing function should overwrite the old function with the new one.

Example: Overwriting a function

>fn inc x => x + 1
>a = 0
    0
>a = inc a
    1
>fn inc x => x + 2
>a = inc a
    3
Input
Input will conform to either the function production or the expression production in the grammar below.

Output
Output for a valid function declaration will be an empty string (null in Java).
Output for a valid expression will be the result of the expression.
Output for input consisting entirely of whitespace will be an empty string (null in Java).
All other cases will throw an error.
-- In Haskell that is:
Right (Nothing, Interpreter)
Right (Just Double, Interpreter) 
Right (Nothing, Interpreter)
Left String
Language
Grammar
This section specifies the grammar for the interpreter language in EBNF syntax Whitespace (one or more) is required:

between the fn keyword and the function name in function definitions
to separate the function name from the parameter list in function definitions
to separate the parameters in function definitions
to separate the arguments in function calls
Whitespace (zero or more) is allowed:

at the start and end of the input
between operators (including =) and their operands
before and after => (start of the function body) in function definitions
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

letter          ::= 'a' | 'b' | ... | 'y' | 'z' | 'A' | 'B' | ... | 'Y' | 'Z'
digit           ::= '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'
Operator Precedence
The following table lists the language's operators grouped in order of precedence. Operators within each group have equal precedence.

Category	Operators
Multiplicative	*, /, %
Additive	+, -
Assignment	=
Function	=>
Division
You should use float division instead of integer division.
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