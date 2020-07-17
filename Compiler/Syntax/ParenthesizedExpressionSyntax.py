from Compiler.Syntax.ExpressionSyntax import ExpressionSyntax
from Compiler.Syntax.SyntaxKind import SyntaxKind


class ParenthesizedExpressionSyntax(ExpressionSyntax):
    def __init__(self, open_parenthesis_token, expression, close_parenthesis_token):
        self._open_parenthesis_token = open_parenthesis_token
        self._expression = expression
        self._close_parenthesis_token = close_parenthesis_token

    def get_open_parenthesis_token(self):
        return self._open_parenthesis_token

    def get_expression(self):
        return self._expression

    def get_close_parenthesis_token(self):
        return self._close_parenthesis_token

    def get_kind(self):
        return SyntaxKind.parenthesized_expression

    def get_children(self):
        return [self._open_parenthesis_token, self._expression, self._close_parenthesis_token]
