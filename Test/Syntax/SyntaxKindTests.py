import traceback

from Compiler.Syntax.SyntaxKind import SyntaxKind
from Compiler.Syntax.SyntaxTree import SyntaxTree


class SyntaxKindTests:
    def __init__(self):
        self._test_count = 0
        self._failed_test_count = 0

    def get_test_count(self):
        return self._test_count

    def get_failed_test_count(self):
        return self._failed_test_count

    def get_succeeded_test_count(self):
        return self._test_count - self._failed_test_count

    def test_syntax_kind(self):
        for i in SyntaxKind.str:
            self._syntax_kind_str_round_trips(i)

    def _syntax_kind_str_round_trips(self, kind):
        text = SyntaxKind.value_exists(kind)

        if text is None:
            return

        tokens = SyntaxTree.parse_token(text)
        token = tokens[0]

        try:
            self._test_count += 1
            assert (len(tokens) == 2), f"Wrong amount of arguments: '{tokens}'"
        except:
            self._failed_test_count += 1
            traceback.print_exc()

        try:
            self._test_count += 1
            assert (kind == token.get_kind()), f"Unexpected kind <{SyntaxKind.kind_exists(token.get_kind())}>," \
                                               f" expected <{SyntaxKind.kind_exists(kind)}>"
        except:
            self._failed_test_count += 1
            traceback.print_exc()

        try:
            self._test_count += 1
            assert (text == token.get_value()), f"Unexpected value '{token.get_value()}', expected '{text}'"
        except:
            self._failed_test_count += 1
            traceback.print_exc()
