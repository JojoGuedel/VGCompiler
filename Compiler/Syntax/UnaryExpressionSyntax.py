from Compiler.Syntax.ExpressionSyntax import ExpressionSyntax
from Compiler.Syntax.SyntaxKind import SyntaxKind
from Compiler.Syntax.SyntaxToken import SyntaxToken


class UnaryExpressionSyntax(ExpressionSyntax):
    def __init__(self, operator_token: SyntaxToken, operand: ExpressionSyntax):
        self._operator_token = operator_token
        self._operand = operand

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"{SyntaxKind.str(SyntaxKind.unary_expression)}: '{self._operator_token.get_value()}'"

    def get_operator_token(self):
        return self._operator_token

    def get_operand(self):
        return self._operand

    def get_kind(self):
        return SyntaxKind.unary_expression

    def get_children(self):
        return [self._operator_token, self._operand]
