from Compiler.Syntax.UnaryExpressionSyntax import UnaryExpressionSyntax
from Compiler.Syntax.BinaryExpressionSyntax import BinaryExpressionSyntax
from Compiler.Syntax.LiteralExpressionSyntax import LiteralExpressionSyntax
from Compiler.Syntax.ParenthesizedExpressionSyntax import ParenthesizedExpressionSyntax
from Compiler.Syntax.SyntaxKind import SyntaxKind
from Compiler.Syntax.SyntaxToken import SyntaxToken
from Compiler.Syntax.SyntaxTree import SyntaxTree
from Compiler.Syntax.Lexer import Lexer


class Parser(SyntaxKind):
    def __init__(self, text=""):
        self._text = text
        self._tokens = []
        self._diagnostics = []
        self._pos = 0

    def set_text(self, text):
        self._text = text

    def _get_current_token(self):
        return self._peek(0)

    def _peek(self, offset):
        if self._pos + offset >= len(self._tokens):
            return self._tokens[len(self._tokens) - 1]
        return self._tokens[self._pos + offset]

    def _match_token(self, list_kind):
        error_text = ""
        if len(list_kind) == 0:
            return self._get_current_token()
        for i in list_kind:
            error_text += SyntaxKind.str(i) + "/"
            if self._get_current_token().get_kind() == i:
                return self._get_current_token()
        self._diagnostics.append(
            f"ERROR: Unexpected token kind <{SyntaxKind.str(self._get_current_token().get_kind())}> expected <" +
            error_text[0:-1] + ">")
        return SyntaxToken(list_kind[0], 0, self._get_current_token().get_pos())

    def _next_token(self):
        current = self._get_current_token()
        self._pos += 1
        return current

    def get_diagnostics(self):
        return self._diagnostics

    def parse(self):
        lexer = Lexer(self._text)
        self._pos = 0
        self._tokens = lexer.label(include_whitespace=False)
        self._diagnostics = lexer.get_diagnostics()

        return SyntaxTree(self._parse_expression(), self._diagnostics)

    def _parse_expression(self, parent_precedence=0):
        unary_operator_precedence = SyntaxKind.get_unary_operator_precedence(self._get_current_token().get_kind())
        if unary_operator_precedence != 0 and unary_operator_precedence >= parent_precedence:
            operator_token = self._next_token()
            operand = self._parse_expression(unary_operator_precedence)
            left = UnaryExpressionSyntax(operator_token, operand)
        else:
            left = self._parse_primary()

        while True:
            precedence = SyntaxKind.get_binary_operator_precedence(self._get_current_token().get_kind())

            if precedence == 0 or precedence <= parent_precedence:
                break

            operator_token = self._next_token()
            right = self._parse_expression(precedence)
            left = BinaryExpressionSyntax(left, operator_token, right)

        return left

    def _parse_primary(self):
        # parse parenthesis
        if self._get_current_token().get_kind() == SyntaxKind.open_parenthesis_token:
            left_parenthesis = self._next_token()
            expression = self._parse_expression()
            right_parenthesis = self._match_token([SyntaxKind.close_parenthesis_token])
            self._next_token()
            return ParenthesizedExpressionSyntax(left_parenthesis, expression, right_parenthesis)
        # boolean
        elif self._get_current_token().get_kind() == SyntaxKind.true_keyword or \
                self._get_current_token().get_kind() == SyntaxKind.false_keyword:
            value = self._get_current_token().get_kind() == SyntaxKind.true_keyword
            self._get_current_token()._value = value
            return LiteralExpressionSyntax(self._next_token())

        # parse numbers
        literal_token = self._match_token([SyntaxKind.int_token, SyntaxKind.float_token, SyntaxKind.string_token, SyntaxKind.char_token])
        self._pos += 1
        return LiteralExpressionSyntax(literal_token)
