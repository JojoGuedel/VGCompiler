from Compiler.Binding.BoundExpression import BoundExpression
from Compiler.Binding.BoundKind import BoundKind
from Compiler.Syntax.SyntaxKind import SyntaxKind


class BoundBinaryExpression(BoundExpression):
    def __init__(self, left_bound_expression, operator_kind: BoundKind, right_bound_expression, result_type):
        self._left_bound_expression = left_bound_expression
        self._operator_kind = operator_kind
        self._right_bound_expression = right_bound_expression
        self._result_type = result_type

    def get_kind(self):
        return BoundKind.binary_expression

    def get_type(self):
        return self._result_type

    def get_left(self):
        return self._left_bound_expression

    def get_operator_kind(self):
        return self._operator_kind

    def get_right(self):
        return self._right_bound_expression
