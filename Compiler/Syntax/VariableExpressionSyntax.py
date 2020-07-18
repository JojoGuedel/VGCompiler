from Compiler.Binding.BoundKind import BoundKind
from Compiler.Syntax.SyntaxKind import SyntaxKind


class VariableExpressionSyntax:
    def __init__(self, identifier_token):
        self._identifier_token = identifier_token

    def get_identifier_token(self):
        return self._identifier_token

    @staticmethod
    def get_kind():
        return SyntaxKind.variable_expression

    def get_children(self):
        return [self._identifier_token]
