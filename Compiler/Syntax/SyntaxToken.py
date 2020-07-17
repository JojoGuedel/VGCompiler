from Compiler.Syntax.SyntaxKind import SyntaxKind


class SyntaxToken:
    def __init__(self, kind, value, pos):
        self._kind = kind
        self._value = value
        self._pos = pos

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"{SyntaxKind.str(self._kind)}: '{self._value}' at {self._pos}"

    def get_kind(self):
        return self._kind

    def get_value(self):
        return self._value

    def get_pos(self):
        return self._pos

    @staticmethod
    def get_children():
        return []
