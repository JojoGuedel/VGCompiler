from Compiler.Binding.BoundExpression import BoundExpression
from Compiler.Binding.BoundKind import BoundKind
from Compiler.Binding.BoundUnaryExpression import BoundUnaryExpression


class Evaluator:
    def __init__(self):
        self._root = None
        self._variables = None

        self._value = None

    def set_root(self, root: BoundExpression):
        self._root = root

    def set_variables(self, variables):
        self._variables = variables

    def evaluate(self):
        return self._evaluate_expression(self._root)

    def _evaluate_expression(self, root):
        if root.get_kind() == BoundKind.literal_expression:
            self._value = root.get_value()

        elif root.get_kind() == BoundKind.unary_expression:
            self._evaluate_unary_expression(root)

        elif root.get_kind() == BoundKind.binary_expression:
            self._evaluate_binary_expression(root)

        elif root.get_kind() == BoundKind.variable_expression:
            self._value = self._variables[root.get_variable_name()]

        elif root.get_kind() == BoundKind.variable_assignment_expression:
            self._value = self._evaluate_expression(root.get_expression())
            self._variables[root.get_variable_name()] = self._value

        else:
            raise Exception(f"Evaluator fail: '{BoundKind.str(root.get_kind())}'")

        return self._value

    def _evaluate_unary_expression(self, root: BoundUnaryExpression):
        operand = self._evaluate_expression(root.get_operand())

        if root.get_operator_kind() == BoundKind.identity:
            self._value = operand

        elif root.get_operator_kind() == BoundKind.negation:
            self._value = -operand

        elif root.get_operator_kind() == BoundKind.logical_not:
            self._value = not operand

        else:
            raise Exception(f"Unexpected unary operator: '{BoundKind.str(root.get_operator_kind())}'")

    def _evaluate_binary_expression(self, root):
        left = self._evaluate_expression(root.get_left())
        right = self._evaluate_expression(root.get_right())

        if root.get_operator_kind() == BoundKind.addition:
            self._value = left + right

        elif root.get_operator_kind() == BoundKind.subtraction:
            self._value = left - right

        elif root.get_operator_kind() == BoundKind.multiplication:
            self._value = left * right

        elif root.get_operator_kind() == BoundKind.division:
            self._value = left / right

        elif root.get_operator_kind() == BoundKind.power:
            self._value = left ** right

        elif root.get_operator_kind() == BoundKind.root:
            self._value = left ** (1.0 / right)

        elif root.get_operator_kind() == BoundKind.logical_and:
            self._value = left and right

        elif root.get_operator_kind() == BoundKind.logical_or:
            self._value = left or right

        elif root.get_operator_kind() == BoundKind.double_equals:
            self._value = left == right

        elif root.get_operator_kind() == BoundKind.double_equals:
            self._value = left != right

        elif root.get_operator_kind() == BoundKind.less_or_equals:
            self._value = left <= right

        elif root.get_operator_kind() == BoundKind.greater_or_equals:
            self._value = left >= right

        elif root.get_operator_kind() == BoundKind.less_than:
            return left < right

        elif root.get_operator_kind() == BoundKind.greater_than:
            self._value = left > right

        else:
            raise Exception(f"Unexpected binary operator: '{BoundKind.str(root.get_operator_kind())}'")
