from Compiler.Syntax.SyntaxKind import SyntaxKind


class AdditionalAssignmentExpression:
    def __init__(self, identifier_token, assignment_token, expression):
        self._identifier_token = identifier_token
        self._assignment_token = assignment_token
        self._expression = expression

    def get_identifier_token(self):
        return self._identifier_token

    def get_assignment_token(self):
        return self._assignment_token

    def get_expression(self):
        return self._expression

    @staticmethod
    def get_kind():
        return SyntaxKind.additional_assignment_expression

    def get_children(self):
        return [self._identifier_token, self._assignment_token, self._expression]