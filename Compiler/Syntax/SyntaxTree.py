import colorama

from Compiler.Syntax.SyntaxKind import SyntaxKind
from Compiler.Syntax.SyntaxToken import SyntaxToken


class SyntaxTree:
    def __init__(self, expression, _diagnostics):
        self._expression = expression
        self._diagnostics = _diagnostics

    def get_expression(self):
        return self._expression

    def get_diagnostics(self):
        return self._diagnostics

    def print(self):
        self._print(self._expression)

    def _print(self, node, indent="", is_last=True):
        if is_last:
            maker = "└──"
        else:
            maker = "├──"

        print(indent, end='')
        print(maker, end='')
        print(SyntaxKind.str(node.get_kind()), end='')

        if isinstance(node, SyntaxToken) and node.get_value() is not None:
            print(f": {node.get_value()}")
        else:
            print()

        if is_last:
            indent += "   "
        else:
            indent += "│  "

        last_child = self._last_or_default(node.get_children())

        for child in node.get_children():
            self._print(child, indent, child == last_child)

    @staticmethod
    def _last_or_default(lst):
        default = None
        for j in lst:
            default = j
        return default