import traceback

from Compiler.Syntax.SyntaxKind import SyntaxKind
from Compiler.Syntax.SyntaxTree import SyntaxTree


class LexerTests:
    def __init__(self):
        self._test_count = 0
        self._failed_test_count = 0

    def get_test_count(self):
        return self._test_count

    def get_failed_test_count(self):
        return self._failed_test_count

    def get_succeeded_test_count(self):
        return self._test_count - self._failed_test_count

    def lexer_lex_token(self, kind, value):
        tokens = list(SyntaxTree.parse_token(value))

        try:
            self._test_count += 1
            assert (len(tokens) != 1), f"Wrong amount of tokens: {tokens}"

        except:
            self._failed_test_count += 1
            traceback.print_exc()

        try:
            self._test_count += 1
            assert (kind == tokens[0].get_kind()), f"Unexpected kind <{SyntaxKind.str(tokens[0].get_kind())}>, expected <{SyntaxKind.str(kind)}>"

        except:
            self._failed_test_count += 1
            traceback.print_exc()

    def test_token_kind(self):
        for t in self._get_token_test_expample():
            self.lexer_lex_token(t[0], t[1])

    @staticmethod
    def _get_token_test_expample():
        return [(SyntaxKind.white_space_token, " "),
                (SyntaxKind.white_space_token, "  "),
                (SyntaxKind.white_space_token, "\r"),
                (SyntaxKind.white_space_token, "\n"),
                (SyntaxKind.white_space_token, "\r\n"),
                (SyntaxKind.int_token, "1"),
                (SyntaxKind.int_token, "123"),
                (SyntaxKind.float_token, "1.1"),
                (SyntaxKind.float_token, "123.123"),
                (SyntaxKind.string_token, "\"a\""),
                (SyntaxKind.string_token, "\"abc\""),
                (SyntaxKind.identifier_token, "a"),
                (SyntaxKind.identifier_token, "abc"),

                (SyntaxKind.char_token, "'a'"),
                (SyntaxKind.plus_token, "+"),
                (SyntaxKind.minus_token, "-"),
                (SyntaxKind.star_token, "*"),
                (SyntaxKind.slash_token, "/"),
                (SyntaxKind.double_star_token, "**"),
                (SyntaxKind.double_slash_token, "//"),
                (SyntaxKind.open_parenthesis_token, "("),
                (SyntaxKind.close_parenthesis_token, ")"),
                (SyntaxKind.bang_token, "!"),
                (SyntaxKind.double_ampersand_token, "&&"),
                (SyntaxKind.double_pipe_token, "||"),
                (SyntaxKind.double_equals_token, "=="),
                (SyntaxKind.not_equals_token, "!="),
                (SyntaxKind.less_or_equals_token, "<="),
                (SyntaxKind.greater_or_equals_token, ">="),
                (SyntaxKind.plus_equals_token, "+="),
                (SyntaxKind.minus_equals_token, "-="),
                (SyntaxKind.star_equals_token, "*="),
                (SyntaxKind.slash_equals_token, "/="),
                (SyntaxKind.less_than_token, "<"),
                (SyntaxKind.greater_than_token, ">"),
                (SyntaxKind.equals_token, "="),
                (SyntaxKind.true_keyword, "true"),
                (SyntaxKind.false_keyword, "false"),]

