from Compiler.Binding.BoundExpression import BoundExpression
from Compiler.Binding.BoundKind import BoundKind


class Evaluator:
    def __init__(self, root=None):
        self._root: BoundExpression = root

    def set_root(self, root: BoundExpression):
        self._root = root

    def evaluate(self):
        return self.evaluate_expression(self._root)

    def evaluate_expression(self, root):        # BoundExpression
        if root.get_kind() == BoundKind.literal_expression:
            return root.get_value()
        elif root.get_kind() == BoundKind.unary_expression:
            operand = self.evaluate_expression(root.get_operand())

            if root.get_operator_kind() == BoundKind.identity:
                return operand
            elif root.get_operator_kind() == BoundKind.negation:
                return -operand
            elif root.get_operator_kind() == BoundKind.logical_not:
                return not operand
            else:
                raise Exception(f"Unexpected unary operator: '{BoundKind.str(root.get_operator_kind())}'")
        elif root.get_kind() == BoundKind.binary_expression:
            left = self.evaluate_expression(root.get_left())
            right = self.evaluate_expression(root.get_right())

            if root.get_operator_kind() == BoundKind.addition:
                return left + right
            elif root.get_operator_kind() == BoundKind.subtraction:
                return left - right
            elif root.get_operator_kind() == BoundKind.multiplication:
                return left * right
            elif root.get_operator_kind() == BoundKind.division:
                return left / right
            elif root.get_operator_kind() == BoundKind.power:
                return left ** right
            elif root.get_operator_kind() == BoundKind.root:
                return left ** (1.0 / right)
            elif root.get_operator_kind() == BoundKind.logical_and:
                return left and right
            elif root.get_operator_kind() == BoundKind.logical_or:
                return left or right
            elif root.get_operator_kind() == BoundKind.double_equals:
                return left == right
            elif root.get_operator_kind() == BoundKind.double_equals:
                return left != right
            elif root.get_operator_kind() == BoundKind.less_or_equals:
                return left <= right
            elif root.get_operator_kind() == BoundKind.greater_or_equals:
                return left >= right
            elif root.get_operator_kind() == BoundKind.less_than:
                return left < right
            elif root.get_operator_kind() == BoundKind.greater_than:
                return left > right
            else:
                raise Exception(f"Unexpected binary operator: '{BoundKind.str(root.get_operator_kind())}'")
        else:
            raise Exception(f"Evaluator fail '")
