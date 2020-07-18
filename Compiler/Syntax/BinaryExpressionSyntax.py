from Compiler.Binding.BoundKind import BoundKind
from Compiler.Syntax.ExpressionSyntax import ExpressionSyntax
from Compiler.Syntax.SyntaxKind import SyntaxKind
from Compiler.Syntax.SyntaxToken import SyntaxToken


class BinaryExpressionSyntax(ExpressionSyntax):
    def __init__(self, left: ExpressionSyntax, operator_token: SyntaxToken, right: ExpressionSyntax):
        self._left = left
        self._operator_token = operator_token
        self._right = right

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"{SyntaxKind.str(SyntaxKind.binary_expression)}: '{self._operator_token.get_value()}'"

    def get_left(self):
        return self._left

    def get_operator_token(self):
        return self._operator_token

    def get_right(self):
        return self._right

    def get_kind(self):
        return SyntaxKind.binary_expression

    def get_children(self):
        return [self._left, self._operator_token, self._right]
