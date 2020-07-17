import colorama
from pynput import keyboard

from Compiler.Binding.Binder import Binder
from Compiler.Compilation import Compilation
from Compiler.Syntax.Lexer import Lexer
from Compiler.Syntax.Parser import Parser
from Compiler.Evaluator import Evaluator

colorama.init()

run = True

compilation = Compilation()
parser = Parser()
lexer = Lexer()
evaluator = Evaluator()
binder = Binder()

# def on_press(key):
#    if key == keyboard.Key.esc:
#        return False  # stop listener
#    try:
#        k = key.char  # single-char
#        print(key.char)
#    except:
#        k = key.name  # other keys
#
# listener = keyboard.Listener(on_press=on_press)
# listener.start()  # start to listen on a separate thread
# listener.join()  # remove if main thread is polling self.keys


while run:
    print(">", end='')
    text = input()

    parser.set_text(text)
    syntax_tree = parser.parse()

    compilation.set_syntax_tree(syntax_tree)
    result = compilation.evaluate()

    if not result.get_diagnostics().get_diagnostic():
        print(result.get_value())
    else:
        result.get_diagnostics().print()
