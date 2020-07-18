from Compiler.Binding.BoundExpression import BoundExpression
from Compiler.Binding.BoundKind import BoundKind
from Compiler.Type import Type


class BoundVariableExpression(BoundExpression):
    def __init__(self, name: str, _type: Type):
        self._name = name
        self._type = _type

    def get_variable_name(self):
        return self._name

    def get_type(self):
        return self._type

    def get_kind(self):
        return BoundKind.variable_expression
