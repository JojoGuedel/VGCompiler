from Compiler.Syntax.SyntaxKind import SyntaxKind


class ExpressionSyntax(SyntaxKind):
    _kind = 0

    def get_kind(self):
        return self._kind
