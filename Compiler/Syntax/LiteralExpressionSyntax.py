from Compiler.Syntax.ExpressionSyntax import ExpressionSyntax
from Compiler.Syntax.SyntaxKind import SyntaxKind
from Compiler.Syntax.SyntaxToken import SyntaxToken


class LiteralExpressionSyntax(ExpressionSyntax):
    def __init__(self, literal_token: SyntaxToken):
        self._literal_token = literal_token

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"{SyntaxKind.str(SyntaxKind.literal_expression)}: '{self._literal_token.get_value()}'"

    def get_literal_token(self):
        return self._literal_token

    def get_value(self):
        return self._literal_token.get_value()

    def get_kind(self):
        return SyntaxKind.literal_expression

    def get_children(self):
        return [self._literal_token]
