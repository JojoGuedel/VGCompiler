import colorama
from pynput import keyboard

from Compiler.Binding.Binder import Binder
from Compiler.Syntax.Lexer import Lexer
from Compiler.Syntax.Parser import Parser
from Compiler.Evaluator import Evaluator

colorama.init()

run = True

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
    expression = parser.parse()
    expression.print()
    binder.set_syntax_tree(expression)
    evaluator.set_root(binder.bind())
    if not expression.get_diagnostics():
        print(evaluator.evaluate())
    else:
        for i in binder.get_diagnostics():
            print(colorama.Fore.RED + i + colorama.Fore.RESET)
