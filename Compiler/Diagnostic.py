import colorama

from Compiler.Syntax.SyntaxKind import SyntaxKind
from Compiler.TetxtSpan import TextSpan


class Diagnostic:
    def __init__(self, span: TextSpan, prefix, message, optional_arguments_list=None):
        self._span = span
        self._prefix = prefix
        self._message = message
        self._optional_arguments_list = optional_arguments_list

    def get_span(self):
        return self._span

    def get_prefix(self):
        return self._prefix

    def get_message(self):
        return self._message

    def get_optional_arguments(self):
        return self._optional_arguments_list
