from Compiler.Syntax.SyntaxKind import SyntaxKind
from Compiler.Syntax.SyntaxToken import SyntaxToken


class Lexer(SyntaxKind):
    def __init__(self, text=""):
        self._text = text
        self._pos = 0
        self._diagnostics = []

    def set_text(self, text):
        self._text = text

    def _next(self, offset=1):
        self._pos += offset
        return self._pos - offset

    def _get_current_char(self):
        return self._peek(0)

    def _peek(self, offset):
        if self._pos + offset >= len(self._text):
            return '\0'
        return self._text[self._pos + offset]

    @staticmethod
    def _is_number(text):
        if text in "1234567890":
            return True
        return False

    @staticmethod
    def _is_letter(text):
        if text in "abcdefghijklmnopqrstuvxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_":
            return True
        return False

    @property
    def _next_token(self):
        # end of file
        if self._get_current_char() == '\0':
            return SyntaxToken(SyntaxKind.end_of_file_token, '\0', self._pos)
        # int, float
        if self._is_number(self._get_current_char()):
            i_num = 0
            start = self._pos

            while self._is_number(self._get_current_char()):
                i_num = int(i_num * 10 + int(self._get_current_char()))
                self._next()

            if self._get_current_char() == '.':
                f_num = float(i_num)
                self._next()
                decimal_place = 10
                decimal_count = 0
                while self._is_number(self._get_current_char()):
                    f_num += float(self._get_current_char()) / float(decimal_place)
                    self._next()
                    decimal_place *= 10
                    decimal_count += 1
                f_num = round(f_num, decimal_count)
                return SyntaxToken(SyntaxKind.float_token, f_num, start)
            return SyntaxToken(SyntaxKind.int_token, i_num, start)
        # char
        if self._get_current_char() == '\'':
            start = self._next()
            while self._get_current_char() != '\'':
                self._next()
                if self._get_current_char() == "\0":
                    self._diagnostics.append("ERROR: Character not closed")
                    break
            value = self._text[start + 1:self._next()]
            if len(value) == 0:
                self._diagnostics.append("ERROR: Empty character")
            if len(value) > 1:
                self._diagnostics.append("ERROR: Invalid character size")
            return SyntaxToken(SyntaxKind.char_token, value, start)
        # keywords, identifier
        if self._is_letter(self._get_current_char()):
            start = self._pos
            while self._is_letter(self._get_current_char()) or self._is_number(self._get_current_char()):
                self._next()
            text = self._text[start:self._pos]
            kind = SyntaxKind.get_keyword_kind(text)
            return SyntaxToken(kind, text, start)
        # string
        if self._get_current_char() == '"':
            start = self._next()
            while self._get_current_char() != '"':
                self._next()
                if self._get_current_char() == "\0":
                    self._diagnostics.append(f"ERROR: String not closed")
                    break
            value = self._text[start + 1:self._next()]
            return SyntaxToken(SyntaxKind.string_token, value, start)
        # keywords, identifier
        if self._is_letter(self._get_current_char()):
            start = self._pos
            while self._is_letter(self._get_current_char()) or self._is_number(self._get_current_char()):
                self._next()
            text = self._text[start:self._pos]
            kind = SyntaxKind.get_keyword_kind(text)
            return SyntaxToken(kind, text, start)
        # plus
        if self._get_current_char() == '+':
            return SyntaxToken(SyntaxKind.plus_token, '+', self._next())
        # minus
        if self._get_current_char() == '-':
            return SyntaxToken(SyntaxKind.minus_token, '-', self._next())
        # star, double star
        if self._get_current_char() == '*':
            if self._peek(1) == '*':
                return SyntaxToken(SyntaxKind.double_star_token, "**", self._next(2))
            return SyntaxToken(SyntaxKind.star_token, '*', self._next())
        # slash, double slash
        if self._get_current_char() == '/':
            if self._peek(1) == '/':
                return SyntaxToken(SyntaxKind.double_slash_token, "//", self._next(2))
            return SyntaxToken(SyntaxKind.slash_token, '/', self._next())
        # open parenthesis
        if self._get_current_char() == '(':
            return SyntaxToken(SyntaxKind.open_parenthesis_token, '(', self._next())
        # close parenthesis
        if self._get_current_char() == ')':
            return SyntaxToken(SyntaxKind.close_parenthesis_token, ')', self._next())
        # whitespace
        if self._get_current_char() == ' ':
            value = ""
            start = self._pos
            while self._get_current_char() == ' ':
                value += self._get_current_char()
                self._next()
            return SyntaxToken(SyntaxKind.white_space_token, value, start)
        # bang_token
        if self._get_current_char() == '!':
            return SyntaxToken(SyntaxKind.bang_token, self._get_current_char(), self._next())
        # double_ampersand_token
        if self._get_current_char() == '&':
            if self._peek(1) == '&':
                return SyntaxToken(SyntaxKind.double_ampersand_token, "&&", self._next(2))
        # double_pipe_token
        if self._get_current_char() == '|':
            if self._peek(1) == '|':
                return SyntaxToken(SyntaxKind.double_pipe_token, "||", self._next(2))
        # double_equals_token
        if self._get_current_char() == '=':
            if self._peek(1) == '=':
                return SyntaxToken(SyntaxKind.double_equals_token, "==", self._next(2))
        # double_equals_token
        if self._get_current_char() == '<':
            if self._peek(1) == '=':
                return SyntaxToken(SyntaxKind.double_equals_token, "<=", self._next(2))
        # double_equals_token
        if self._get_current_char() == '>':
            if self._peek(1) == '=':
                return SyntaxToken(SyntaxKind.double_equals_token, ">=", self._next(2))
        # less_than
        if self._get_current_char() == '<':
            return SyntaxToken(SyntaxKind.less_than_token, self._get_current_char(), self._next())
        # greater_than
        if self._get_current_char() == '>':
            return SyntaxToken(SyntaxKind.greater_than_token, self._get_current_char(), self._next())
        # invalid_char
        self._diagnostics.append(f"ERROR: Invalid character input '{self._get_current_char()}'")
        return SyntaxToken(SyntaxKind.invalid_char_token, self._get_current_char(), self._next())

    def label(self, include_whitespace=True):
        self._pos = 0
        self._diagnostics = []

        token_list = []

        while self._get_current_char() != '\0':
            current = self._next_token
            if not include_whitespace and current.get_kind() == SyntaxKind.white_space_token:
                current = self._next_token
            token_list.append(current)
        token_list.append(SyntaxToken(SyntaxKind.end_of_file_token, '\0', self._pos))
        return token_list

    def get_diagnostics(self):
        return self._diagnostics