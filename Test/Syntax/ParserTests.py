import traceback

from Compiler.Syntax.SyntaxKind import SyntaxKind
from Compiler.Syntax.SyntaxTree import SyntaxTree


class ParserTests:
    def __init__(self):
        self._test_count = 0
        self._failed_test_count = 0

    def get_test_count(self):
        return self._test_count

    def get_failed_test_count(self):
        return self._failed_test_count

    def get_succeeded_test_count(self):
        return self._test_count - self._failed_test_count

    def test_unary_operators(self):
        for i in SyntaxKind.str:
            if SyntaxKind.get_unary_operator_precedence(i) > 0:
                pass

    def test_binary_operators(self):
        for i in SyntaxKind.str:
            if SyntaxKind.get_binary_operator_precedence(i) > 0:
                pass

    def _parser_test_binary_expression(self, op1, op2):
        pass
