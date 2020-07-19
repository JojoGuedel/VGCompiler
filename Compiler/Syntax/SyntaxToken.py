from Compiler.Syntax.SyntaxKind import SyntaxKind
from Compiler.TetxtSpan import TextSpan


class SyntaxToken:
    def __init__(self, kind, value, text_span: TextSpan):
        self._kind = kind
        self._value = value
        self._text_span = text_span

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"{SyntaxKind.str(self._kind)}: '{self._value}' at {self._text_span.get_start()}"

    def get_kind(self):
        return self._kind

    def get_value(self):
        return self._value

    def get_text_span(self):
        return self._text_span

    @staticmethod
    def get_children():
        return []
