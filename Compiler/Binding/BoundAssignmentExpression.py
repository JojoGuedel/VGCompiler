from Compiler.Binding.BoundKind import BoundKind


class BoundAssignmentExpression:
    def __init__(self, variable_name, expression):
        self._variable_name = variable_name
        self._expression = expression

    def get_variable_name(self):
        return self._variable_name

    def get_expression(self):
        return self._expression

    def get_type(self):
        return self._expression.get_type()

    @staticmethod
    def get_kind():
        return BoundKind.variable_assignment_expression
