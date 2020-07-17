from Compiler.Binding.BoundExpression import BoundExpression
from Compiler.Binding.BoundKind import BoundKind


class BoundLiteralExpression(BoundExpression):
    def __init__(self, t, value):
        self._type = t
        self._value = value

    def get_kind(self):
        return BoundKind.literal_expression

    def get_type(self):
        return self._type

    def get_value(self):
        return self._value
