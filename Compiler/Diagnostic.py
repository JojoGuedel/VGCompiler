import colorama

from Compiler.Syntax.SyntaxKind import SyntaxKind
from Compiler.TetxtSpan import TextSpan


class Diagnostic:
    def __init__(self, span: TextSpan, prefix, message, *optional_arguments, line=""):
        self._span = span
        self._prefix = prefix
        self._message = message
        self._args = optional_arguments
        self._line = line

    def get_span(self):
        return self._span

    def get_prefix(self):
        return self._prefix

    def get_message(self):
        return self._message

    def get_args(self):
        return self._args

    def get_line(self):
        return self._line
