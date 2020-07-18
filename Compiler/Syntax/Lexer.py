from Compiler.Diagnostic import Diagnostic
from Compiler.DiagnosticBag import DiagnosticBag
from Compiler.Syntax.SyntaxKind import SyntaxKind
from Compiler.Syntax.SyntaxToken import SyntaxToken
from Compiler.TetxtSpan import TextSpan


class Lexer(SyntaxKind):
    def __init__(self, text=""):
        self._pos = 0
        self._text = text
        self._diagnostics = DiagnosticBag()

        self._start = None
        self._kind = None
        self._value = None
        self._text_span = None
        self._error_message = ""

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
        self._start = self._pos
        self._value = None
        self._kind = SyntaxKind.invalid_char_token
        self._text_span = TextSpan(self._start, self._pos)

        if self._is_number(self._get_current_char()):
            self._label_number()

        elif self._is_letter(self._get_current_char()):
            self._label_identifier()

        elif self._get_current_char() == '\'':
            self._label_char()

        elif self._get_current_char() == '"':
            self._label_string()

        elif self._get_current_char() == ' ':
            self._label_whitespace()

        elif self._get_current_char() == '*':
            self._label_double_token(['*', '='], [SyntaxKind.double_star_token, SyntaxKind.equals_token], SyntaxKind.star_token)

        elif self._get_current_char() == '/':
            self._label_double_token(['/'], [SyntaxKind.double_slash_token], SyntaxKind.slash_token)

        elif self._get_current_char() == '!':
            self._label_double_token(['='], [SyntaxKind.not_equals_token], SyntaxKind.bang_token)

        elif self._get_current_char() == '=':
            self._label_double_token(['='], [SyntaxKind.double_equals_token], SyntaxKind.equals_token)

        elif self._get_current_char() == '<':
            self._label_double_token(['='], [SyntaxKind.less_than_token], SyntaxKind.less_or_equals_token)

        elif self._get_current_char() == '>':
            self._label_double_token(['='], [SyntaxKind.greater_or_equals_token], SyntaxKind.greater_than_token)

        elif self._get_current_char() == '&':
            self._label_double_token(['&'], [SyntaxKind.double_ampersand_token])

        elif self._get_current_char() == '|':
            self._label_double_token(['|'], [SyntaxKind.double_pipe_token])

        elif self._get_current_char() == '+':
            self._kind = SyntaxKind.plus_token
            self._value = '+'
            self._text_span = TextSpan(self._start, self._next())

        elif self._get_current_char() == '-':
            self._kind = SyntaxKind.minus_token
            self._value = '-'
            self._text_span = TextSpan(self._start, self._next())

        elif self._get_current_char() == '(':
            self._kind = SyntaxKind.open_parenthesis_token
            self._value = '('
            self._text_span = TextSpan(self._start, self._next())

        elif self._get_current_char() == ')':
            self._kind = SyntaxKind.close_parenthesis_token
            self._value = ')'
            self._text_span = TextSpan(self._start, self._next())

        elif self._get_current_char() == '\0':
            self._kind = SyntaxKind.end_of_file_token
            self._value = '\0'
            self._text_span = TextSpan(self._start, self._pos)

        return SyntaxToken(self._kind, self._value, TextSpan(self._text_span.get_start(), self._text_span.get_end(), self._text))

    def _label_number(self):
        value = 0.0
        while self._is_number(self._get_current_char()):
            value = value * 10 + int(self._get_current_char())
            self._next()

        if self._get_current_char() == '.':
            decimal_place = 10.0
            self._next()

            while self._is_number(self._get_current_char()):
                value += float(self._get_current_char()) / decimal_place
                decimal_place *= 10.0
                self._next()

            self._kind = SyntaxKind.float_token
            self._value = value
            self._text_span = TextSpan(self._start, self._pos)
        else:
            self._kind = SyntaxKind.int_token
            self._value = int(value)
            self._text_span= TextSpan(self._start, self._pos)

    def _label_identifier(self):
        while self._is_letter(self._get_current_char()) or self._is_number(self._get_current_char()):
            self._next()

        self._kind = SyntaxKind.get_keyword_kind(self._value)
        self._value = self._text[self._start:self._pos]
        self._text_span = TextSpan(self._start, self._pos)

    def _label_char(self):
        self._next()

        while self._get_current_char() != '\'' and self._get_current_char() != "\0":
            self._next()

        if self._get_current_char() == "\0":
            self._report_error(DiagnosticBag.Message.char_literal_not_closed)

        if self._start - self._pos == 0:
            self._report_error(DiagnosticBag.Message.char_empty)

        if self._start - self._pos > 1:
            self._report_error(DiagnosticBag.Message.char_invalid_size)

        self._kind = SyntaxKind.char_token
        self._value = self._text[self._start + 1: self._next()]
        self._text_span = TextSpan(self._start + 1, self._pos - 1)

    def _label_string(self):
        self._next()

        while self._get_current_char() != '"' and self._get_current_char() != "\0":
            self._next()

        if self._get_current_char() == "\0":
            self._report_error(DiagnosticBag.Message.char_literal_not_closed)

        self._kind = SyntaxKind.string_token
        self._value = self._text[self._start + 1: self._pos - 1]
        self._text_span = TextSpan(self._start + 1, self._next())

    def _label_whitespace(self):
        while self._get_current_char() == ' ':
            self._next()

        self._kind = SyntaxKind.white_space_token
        self._value = self._text[self._start: self._pos]
        self._text_span = TextSpan(self._start, self._pos)

    def _label_double_token(self, char_2_list, kind_2_list, kind_1=None):
        if len(char_2_list) == len(kind_2_list):
            for i in range(len(char_2_list)):
                if self._peek(1) == char_2_list[i]:
                    self._kind = kind_2_list[i]
                    self._value = self._text[self._start: self._pos + 1]
                    self._text_span = TextSpan(self._start, self._next(2) + 1)

                else:
                    if kind_1 is not None:
                        self._kind = kind_1
                        self._value = self._get_current_char()
                        self._text_span = TextSpan(self._start, self._next())

                    else:
                        self._next()
                        self._start += 1
                        self._report_error(DiagnosticBag.Message.char_not_expected, [self._get_current_char(), char_2_list[i]])

        else:
            raise Exception("Invalid combination of arguments")

    def _report_error(self, error_message, optional_arguments_list=None):
        if optional_arguments_list is not None:
            self._diagnostics.append(
                Diagnostic(TextSpan(self._start, self._pos, line=self._text), DiagnosticBag.Prefix.Error, error_message,
                           optional_arguments_list))
        else:
            self._diagnostics.append(
                Diagnostic(TextSpan(self._start, self._pos, line=self._text), DiagnosticBag.Prefix.Error,
                           error_message))

    def label(self, include_whitespace=True):
        self._pos = 0
        self._diagnostics.clear()

        token_list = []

        while self._get_current_char() != '\0':
            current = self._next_token
            if not include_whitespace and current.get_kind() == SyntaxKind.white_space_token:
                current = self._next_token
            token_list.append(current)
        token_list.append(
            SyntaxToken(SyntaxKind.end_of_file_token, '\0', TextSpan(self._pos, self._pos, line=self._text)))
        return token_list

    def get_diagnostics(self):
        return self._diagnostics
