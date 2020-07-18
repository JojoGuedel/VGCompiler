from Compiler.Syntax.SyntaxKind import SyntaxKind


class AssignmentExpressionSyntax:
    def __init__(self, identifier_token, equals_token, expression):
        self._identifier_token = identifier_token
        self._equals_token = equals_token
        self._expression = expression

    def get_identifier_token(self):
        return self._identifier_token

    def get_equals_token(self):
        return self._equals_token

    def get_expression(self):
        return self._expression

    @staticmethod
    def get_kind():
        return SyntaxKind.assignment_expression

    def get_children(self):
        return [self._identifier_token, self._equals_token, self._expression]
