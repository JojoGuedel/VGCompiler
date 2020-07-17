from Compiler.Binding.BoundKind import BoundKind
from Compiler.Binding import BoundLiteralExpression
from Compiler.Binding.BoundExpression import BoundExpression


class BoundUnaryExpression(BoundExpression):
    def __init__(self, operator_kind: BoundKind, operand: BoundLiteralExpression, result_type):
        self._operator_kind = operator_kind
        self._operand = operand
        self._result_type = result_type

    def get_kind(self):
        return BoundKind.unary_expression

    def get_type(self):
        return self._result_type

    def get_operator_kind(self):
        return self._operator_kind

    def get_operand(self):
        return self._operand
