import colorama

from Compiler.Diagnostic import Diagnostic


class DiagnosticBag:
    def __init__(self):
        self._diagnostic = []

    def get_diagnostic(self):
        return self._diagnostic

    def append(self, diagnostic: Diagnostic):
        self._diagnostic.append(diagnostic)

    def clear(self):
        self._diagnostic.clear()

    def print_fast_diagnostic(self):
        for i in self._diagnostic:
            self._print_fast(i.get_span(), i.get_prefix(), i.get_message(), i.get_args())

    def print(self):
        for i in self._diagnostic:
            if i.get_line() != "":
                self._print(i.get_span(), i.get_prefix(), i.get_message(), i.get_args(), i.get_line())
            else:
                self._print_fast(i.get_span(), i.get_prefix(), i.get_message(), i.get_args())

    def _print_fast(self, span, prefix, message, args):
        position = f"{span.get_start()}"
        if span.get_start() != span.get_end():
            position = f"{span.get_start()}:{span.get_end()}"
        prefix = self._format(prefix, [position])
        message = self._format(message, args)
        diagnostic_message = f"{prefix}{message}{colorama.Fore.RESET}"
        print(diagnostic_message)

    def _print(self, span, prefix, message, args, line):
        self._print_fast(span, prefix, message, args)
        print(colorama.Fore.RED + "└──" + "ErrorLine: " + line)
        if span.get_length() == 0:
            print(" " * 14 + " " * span.get_start() + "^" + colorama.Fore.RESET)
        else:
            print(" " * 14 + " " * span.get_start() + "^" + "~" * (span.get_length() - 2) + "^" + colorama.Fore.RESET)

    @staticmethod
    def _format(text: str, args):
        value = ""
        sub_text = text.split("{}")
        for i in range(len(sub_text) - 1):
            value += sub_text[i] + str(args[i])
        value += sub_text[len(sub_text)-1]
        return value

    class Prefix:
        Error = colorama.Fore.RED + "Error({}): "
        Warning = colorama.Fore.YELLOW + "Warning({}): "

    class Message:
        char_invalid_input = "Invalid character input: '{}'."

        char_literal_not_closed = "Character literal not closed."
        char_empty = "Empty character."
        char_invalid_size = "Invalid character size."

        str_literal_not_closed = "String literal not closed."

        token_unexpected_kind = "Unexpected token kind <{}>, expected <{}>."

        operation_illegal_unary = "Illegal unary operation '{}' for <{}>."
        operation_illegal_binary = "Illegal binary operation '{}' for <{}> and <{}>."

        variable_not_defined = "Variable '{}' does not exist."
