/**
 * Title: Simple Interactive Interpreter
 * Link: https://www.codewars.com/kata/52ffcfa4aff455b3c2000750
 * Difficulty: 1 kyu
 *
 * ## Description
 *
 * You will create an interpreter which takes inputs described below and produces outputs,
 * storing state in between each input.
 *
 * If you're not sure where to start with this kata, check out the "Simpler Interactive Interpreter"
 * kata, which greatly simplifies the interpreter by removing functions.
 *
 * > **Note**: The `eval` command has been disabled.
 *
 * ## Concepts
 *
 * The interpreter will take inputs in the language described under the language header below.
 * This section will give an overview of the language constructs.
 *
 * ### Variables
 *
 * Any identifier which is not a keyword or a function name will be treated as a variable.
 * If the identifier is on the left hand side of an assignment operator, the result of the
 * right hand side will be stored in the variable. If a variable occurs as part of an expression,
 * the value held in the variable will be substituted when the expression is evaluated.
 *
 * Variables are implicitly declared the first time they are assigned to.
 *
 * **Example**: Initializing a variable and using it:
 * ```
 * > x = 7
 *   7
 * > x + 6
 *   13
 * ```
 *
 * Referencing a non-existent variable will cause the interpreter to throw an error.
 * The interpreter should be able to continue accepting input even after throwing.
 *
 * **Example**: Referencing a non-existent variable:
 * ```
 * > y + 7
 *   ERROR: Invalid identifier. No variable with name 'y' was found.
 * ```
 *
 * ### Assignments
 *
 * An assignment is an expression that has an identifier on the left side of an `=` operator,
 * and any expression on the right. Such expressions should store the value of the right hand
 * side in the specified variable and return the result.
 *
 * **Example**: Assigning a constant to a variable:
 * ```
 * x = 7
 *   7
 * ```
 *
 * Assignments are right-associative and can be chained or nested.
 *
 * **Example**: Chained assignments:
 * ```
 * x = y = 7
 *   7
 * ```
 *
 * **Example**: Nested assignments:
 * ```
 * x = 13 + (y = 3)
 *   16
 * ```
 *
 * ### Operator Precedence
 *
 * Operator precedence follows the common order.
 *
 * ### Functions
 *
 * Functions are declared by the `fn` keyword followed by a name, an optional argument list,
 * the `=>` operator, and finally an expression.
 *
 * All function variables are local to the function. References to variables not found in the
 * argument list should result in an error when the function is defined.
 *
 * **Example**: Average of two variables:
 * ```
 * > fn avg x y => (x + y) / 2
 * > a = 2
 *   2
 * > b = 4
 *   4
 * > avg a b
 *   3
 * ```
 *
 * **Example**: Chain method calls (function calls are right-associative):
 * ```
 * > fn echo x => x
 * > fn add x y => x + y
 * > add echo 4 echo 3
 *   7
 * ```
 *
 * ### Name Conflicts
 *
 * If a variable is declared, a subsequent function with the same name results in an error.
 * Overwriting an existing function name with a new definition is allowed.
 *
 * ## Language Grammar (EBNF)
 *
 * ```ebnf
 * whitespace      ::= ' ' { whitespace }
 * function        ::= 'fn'  whitespace  fn-name { whitespace identifier } '=>' expression
 * fn-name         ::= identifier
 * expression      ::= factor | expression operator expression
 * factor          ::= number | identifier | assignment | '(' expression ')' | function-call
 * assignment      ::= identifier '=' expression
 * function-call   ::= fn-name { whitespace expression }
 * operator        ::= '+' | '-' | '*' | '/' | '%'
 * identifier      ::= (letter | '_') { identifier-char }
 * identifier-char ::= '_' | letter | digit
 * number          ::= { digit } '.' digit { digit } | digit { digit } ['.']
 * letter          ::= 'a' | 'b' | ... | 'z' | 'A' | 'B' | ... | 'Z'
 * digit           ::= '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'
 * ```
 *
 * ## Operator Precedence
 *
 * | Category       | Operators    |
 * |----------------|--------------|
 * | Multiplicative | *, /, %      |
 * | Additive       | +, -         |
 * | Assignment     | =            |
 * | Function       | =>           |
 *
 * Division should be float division.
 */

var NUMBER_RE = /^\d+(\.\d+)?$/;
var IDENT_START_RE = /^[A-Za-z_]/;
var IDENT_RE = /^[A-Za-z_][A-Za-z0-9_]*$/;

var FN = 'fn';
var ARROW = '=>';

var ADDITIVE_OPS = new Set(['+', '-']);
var MULTIPLICATIVE_OPS = new Set(['*', '/', '%']);

function applyBinary(operator, left, right) {
    switch (operator) {
        case '*':
            return left * right;
        case '/':
            return left / right;
        case '%':
            return left % right;
        case '+':
            return left + right;
        case '-':
            return left - right;
        default:
            throw new Error('Unsupported operator: ' + operator);
    }
}

function hasOwn(obj, key) {
    return Object.prototype.hasOwnProperty.call(obj, key);
}

function ExpressionParser(interpreter, tokens, localVars) {
    this.interpreter = interpreter;
    this.tokens = tokens;
    this.localVars = localVars;
    this.pos = 0;
}

ExpressionParser.prototype.parse = function () {
    var result = this.parseAssignment();
    if (this.pos !== this.tokens.length) {
        throw new Error('ERROR: Invalid syntax!');
    }
    return result;
};

ExpressionParser.prototype.peek = function () {
    return this.pos < this.tokens.length ? this.tokens[this.pos] : null;
};

ExpressionParser.prototype._atAssignmentInfix = function () {
    if (this.pos + 1 >= this.tokens.length) {
        return false;
    }
    if (this.tokens[this.pos + 1] !== '=') {
        return false;
    }
    return IDENT_RE.test(this.tokens[this.pos]);
};

ExpressionParser.prototype.parseAssignment = function () {
    if (!this._atAssignmentInfix()) {
        return this.parseAdditive();
    }
    var name = this.tokens[this.pos];
    if (hasOwn(this.interpreter.functions, name)) {
        throw new Error('Cannot overwrite function with variable!');
    }
    this.pos += 2;
    var value = this.parseAssignment();
    this.interpreter.vars[name] = value;
    return value;
};

ExpressionParser.prototype.parseAdditive = function () {
    var left = this.parseMultiplicative();
    while (ADDITIVE_OPS.has(this.peek())) {
        var operator = this.tokens[this.pos];
        this.pos += 1;
        var right = this.parseMultiplicative();
        left = applyBinary(operator, left, right);
    }
    return left;
};

ExpressionParser.prototype.parseMultiplicative = function () {
    var left = this.parsePrimary();
    while (MULTIPLICATIVE_OPS.has(this.peek())) {
        var operator = this.tokens[this.pos];
        this.pos += 1;
        var right = this.parsePrimary();
        left = applyBinary(operator, left, right);
    }
    return left;
};

ExpressionParser.prototype.parsePrimary = function () {
    if (this.pos >= this.tokens.length) {
        throw new Error('ERROR: Invalid syntax!');
    }
    var token = this.tokens[this.pos];
    if (NUMBER_RE.test(token)) {
        return this._consumeNumericLiteral(token);
    }
    if (token === '(') {
        return this._consumeParenthesizedExpression();
    }
    if (!IDENT_RE.test(token)) {
        throw new Error('ERROR: Invalid syntax!');
    }
    return this._resolveIdentifier(token);
};

ExpressionParser.prototype._consumeNumericLiteral = function (token) {
    this.pos += 1;
    return token.indexOf('.') !== -1 ? parseFloat(token) : parseInt(token, 10);
};

ExpressionParser.prototype._consumeParenthesizedExpression = function () {
    this.pos += 1;
    var value = this.parseAssignment();
    if (this.peek() !== ')') {
        throw new Error("ERROR: Unmatched '(' in expression.");
    }
    this.pos += 1;
    return value;
};

ExpressionParser.prototype._resolveIdentifier = function (token) {
    if (hasOwn(this.localVars, token)) {
        this.pos += 1;
        return this.localVars[token];
    }
    if (hasOwn(this.interpreter.vars, token)) {
        this.pos += 1;
        return this.interpreter.vars[token];
    }
    if (hasOwn(this.interpreter.functions, token)) {
        return this._applyFunctionCall(token);
    }
    throw new Error("ERROR: Invalid identifier. No variable with name '" + token + "' was found.");
};

ExpressionParser.prototype._applyFunctionCall = function (name) {
    this.pos += 1;
    var functionDef = this.interpreter.functions[name];
    var argumentValues = [];
    var self = this;
    functionDef.argNames.forEach(function () {
        argumentValues.push(self.parseAssignment());
    });
    var boundLocals = {};
    for (var i = 0; i < functionDef.argNames.length; i++) {
        boundLocals[functionDef.argNames[i]] = argumentValues[i];
    }
    var inner = new ExpressionParser(
        this.interpreter,
        functionDef.body.slice(),
        boundLocals
    );
    return inner.parse();
};

function Interpreter() {
    this.vars = {};
    this.functions = {};
}

Interpreter.prototype.tokenize = function (program) {
    if (!program) return [];
    var regex = /=>|[-+*/%()=]|[A-Za-z_][A-Za-z0-9_]*|\d*\.?\d+/g;
    return program.match(regex) || [];
};

Interpreter.prototype.input = function (expr) {
    var tokens = this.tokenize(expr || '');
    if (tokens.length === 0) {
        return '';
    }
    if (tokens[0] === FN) {
        return this._defineFunction(tokens);
    }
    var parser = new ExpressionParser(this, tokens, {});
    return parser.parse();
};

Interpreter.prototype._defineFunction = function (tokens) {
    var parsed = this._parseFunctionDeclaration(tokens);
    this._validateFunctionBodyIdentifiers(parsed.body, parsed.argNames);
    this.functions[parsed.name] = {
        argNames: parsed.argNames,
        body: parsed.body,
    };
    return '';
};

Interpreter.prototype._parseFunctionDeclaration = function (tokens) {
    var arrowIdx = tokens.indexOf(ARROW);
    if (arrowIdx === -1) {
        throw new Error('Invalid function definition');
    }
    var name = tokens[1];
    if (hasOwn(this.vars, name)) {
        throw new Error('Cannot overwrite variable with function!');
    }
    var argNames = tokens.slice(2, arrowIdx);
    if (new Set(argNames).size !== argNames.length) {
        throw new Error('Duplicate parameters specified!');
    }
    var body = tokens.slice(arrowIdx + 1);
    return { name: name, argNames: argNames, body: body };
};

Interpreter.prototype._validateFunctionBodyIdentifiers = function (body, argNames) {
    var argSet = {};
    for (var i = 0; i < argNames.length; i++) {
        argSet[argNames[i]] = true;
    }
    for (var b = 0; b < body.length; b++) {
        var token = body[b];
        if (!IDENT_START_RE.test(token)) {
            continue;
        }
        if (argSet[token] || hasOwn(this.functions, token)) {
            continue;
        }
        throw new Error("ERROR: Invalid identifier '" + token + "' in function body.");
    }
};

module.exports = Interpreter;
module.exports.Interpreter = Interpreter;
module.exports.applyBinary = applyBinary;