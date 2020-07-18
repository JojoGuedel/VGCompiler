from Compiler.Type import Type
from Compiler.Diagnostic import Diagnostic
from Compiler.DiagnosticBag import DiagnosticBag
from Compiler.Binding.BoundKind import BoundKind
from Compiler.Syntax.SyntaxTree import SyntaxTree
from Compiler.Syntax.SyntaxKind import SyntaxKind
from Compiler.Binding.BoundUnaryExpression import BoundUnaryExpression
from Compiler.Syntax.UnaryExpressionSyntax import UnaryExpressionSyntax
from Compiler.Binding.BoundBinaryExpression import BoundBinaryExpression
from Compiler.Syntax.BinaryExpressionSyntax import BinaryExpressionSyntax
from Compiler.Binding.BoundLiteralExpression import BoundLiteralExpression
from Compiler.Syntax.AssignmentExpression import AssignmentExpressionSyntax
from Compiler.Syntax.LiteralExpressionSyntax import LiteralExpressionSyntax
from Compiler.Binding.BoundVariableExpression import BoundVariableExpression
from Compiler.Syntax.VariableExpressionSyntax import VariableExpressionSyntax
from Compiler.Binding.BoundAssignmentExpression import BoundAssignmentExpression


class Binder:
    def __init__(self):
        self._variables = None
        self._syntax_tree = None
        self._diagnostics = DiagnosticBag()
        self._syntax = None

    def set_syntax_tree(self, syntax_tree: SyntaxTree):
        self._syntax_tree = syntax_tree
        self._syntax = syntax_tree.get_expression()

    def set_variable(self, variables):
        self._variables = variables

    def get_diagnostics(self):
        return self._diagnostics

    def bind(self):
        self._diagnostics = self._syntax_tree.get_diagnostics()
        return self._bind_expression(self._syntax)

    def _bind_expression(self, syntax):
        if syntax.get_kind() == SyntaxKind.literal_expression:
            return self._bind_literal_expression(syntax)
        elif syntax.get_kind() == SyntaxKind.unary_expression:
            return self._bind_unary_expression(syntax)
        elif syntax.get_kind() == SyntaxKind.binary_expression:
            return self._bind_binary_expression(syntax)
        elif syntax.get_kind() == SyntaxKind.parenthesized_expression:
            return self._bind_expression(syntax.get_expression())
        elif syntax.get_kind() == SyntaxKind.variable_expression:
            return self._bind_variable_expression(syntax)
        elif syntax.get_kind() == SyntaxKind.assignment_expression:
            return self._bind_assignment_expression(syntax)
        else:
            raise Exception(f"Unexpected syntax: '{SyntaxKind.str(self._syntax.get_kind())}'")

    @staticmethod
    def _bind_literal_expression(syntax: LiteralExpressionSyntax):
        return BoundLiteralExpression(Type.get_type(syntax.get_literal_token().get_kind()),
                                      syntax.get_literal_token().get_value())

    def _bind_unary_expression(self, syntax: UnaryExpressionSyntax):
        bound_operand = self._bind_expression(syntax.get_operand())  # BoundExpression
        bound_operator_kind: BoundKind = self._bind_unary_operator_kind(syntax.get_operator_token().get_kind())
        result_type = BoundKind.resolve_unary_type(bound_operand.get_type(), bound_operator_kind)
        if result_type is None:
            self._diagnostics.append(Diagnostic(syntax.get_operator_token().get_pos(), DiagnosticBag.Prefix.Error,
                                                DiagnosticBag.Message.operation_illegal_unary,
                                                [BoundKind.str(bound_operator_kind), Type.str(bound_operand.get_type())]))
        return BoundUnaryExpression(bound_operator_kind, bound_operand, result_type)

    def _bind_binary_expression(self, syntax: BinaryExpressionSyntax):
        bound_left = self._bind_expression(syntax.get_left())  # BoundExpression
        bound_right = self._bind_expression(syntax.get_right())  # BoundExpression
        bound_operator_kind = self._bind_binary_operator_kind(syntax.get_operator_token().get_kind())
        result_type = BoundKind.resolve_binary_type(bound_left.get_type(), bound_operator_kind, bound_right.get_type())
        if result_type is None:
            self._diagnostics.append(Diagnostic(syntax.get_operator_token().get_pos(), DiagnosticBag.Prefix.Error,
                                                DiagnosticBag.Message.operation_illegal_binary,
                                                [BoundKind.str(bound_operator_kind), Type.str(bound_left.get_type()),
                                                Type.str(bound_right.get_type())]))
        return BoundBinaryExpression(bound_left, bound_operator_kind, bound_right, result_type)

    def _bind_variable_expression(self, syntax: VariableExpressionSyntax):
        name = syntax.get_identifier_token().get_value()

        if not name in self._variables:
            self._diagnostics.append(
                Diagnostic(syntax.get_identifier_token().get_pos(), DiagnosticBag.Prefix.Error, DiagnosticBag.Message.variable_not_defined, name))
            return BoundLiteralExpression(Type.none_type, 0)

        variable_type = Type.none_type
        if isinstance(self._variables[name], int):
            variable_type = Type.int_type
        if isinstance(self._variables[name], float):
            variable_type = Type.float_type
        if isinstance(self._variables[name], str):
            variable_type = Type.string_type
            if len(self._variables[name]) == 1:
                variable_type = Type.char_type
        if isinstance(self._variables[name], bool):
            variable_type = Type.boolean_type
        if self._variables[name] is None:
            variable_type = Type.any_type
        return BoundVariableExpression(name, variable_type)

    def _bind_assignment_expression(self, syntax: AssignmentExpressionSyntax):
        variable_name = syntax.get_identifier_token().get_value()
        expression = self._bind_expression(syntax.get_expression())
        return BoundAssignmentExpression(variable_name, expression)

    @staticmethod
    def _bind_unary_operator_kind(kind):
        if kind == SyntaxKind.plus_token:
            return BoundKind.identity
        elif kind == SyntaxKind.minus_token:
            return BoundKind.negation
        elif kind == SyntaxKind.bang_token:
            return BoundKind.logical_not
        else:
            raise Exception(f"Unexpected unary operator: '{SyntaxKind.str(kind)}'")

    @staticmethod
    def _bind_binary_operator_kind(kind):
        if kind == SyntaxKind.plus_token:
            return BoundKind.addition
        elif kind == SyntaxKind.minus_token:
            return BoundKind.subtraction
        elif kind == SyntaxKind.star_token:
            return BoundKind.multiplication
        elif kind == SyntaxKind.slash_token:
            return BoundKind.division
        elif kind == SyntaxKind.double_star_token:
            return BoundKind.power
        elif kind == SyntaxKind.double_slash_token:
            return BoundKind.root
        elif kind == SyntaxKind.double_ampersand_token:
            return BoundKind.logical_and
        elif kind == SyntaxKind.double_pipe_token:
            return BoundKind.logical_or
        elif kind == SyntaxKind.double_equals_token:
            return BoundKind.double_equals
        elif kind == SyntaxKind.less_or_equals_token:
            return BoundKind.less_or_equals
        elif kind == SyntaxKind.greater_or_equals_token:
            return BoundKind.greater_or_equals
        elif kind == SyntaxKind.less_than_token:
            return BoundKind.less_than
        elif kind == SyntaxKind.greater_than_token:
            return BoundKind.greater_than
        else:
            raise Exception(f"Unexpected binary operator: '{SyntaxKind.str(kind)}'")
