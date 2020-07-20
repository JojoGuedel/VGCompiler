import colorama
import time

from Compiler.Syntax.SyntaxKind import SyntaxKind
from Test.Syntax.LexerTexts import LexerTests
from Test.Syntax.ParserTests import ParserTests
from Test.Syntax.SyntaxKindTests import SyntaxKindTests

colorama.init()

test_count = 0
failed_test_count = 0
succeeded_test_count = 0

lexer_tests = LexerTests()
parser_tests = ParserTests()
syntax_kind_tests = SyntaxKindTests()

start_time = time.time()
lexer_tests.test_token_kind()
syntax_kind_tests.test_syntax_kind()
end_time = time.time()

test_count += lexer_tests.get_test_count()
failed_test_count += lexer_tests.get_failed_test_count()
succeeded_test_count += lexer_tests.get_succeeded_test_count()

test_count += parser_tests.get_test_count()
failed_test_count += parser_tests.get_failed_test_count()
succeeded_test_count += parser_tests.get_succeeded_test_count()

test_count += syntax_kind_tests.get_test_count()
failed_test_count += syntax_kind_tests.get_failed_test_count()
succeeded_test_count += syntax_kind_tests.get_succeeded_test_count()

time.sleep(0.1)
if failed_test_count == 0:
      print(f"\n{colorama.Fore.GREEN}Test run successful.{colorama.Fore.RESET}")
else:
      print(f"\n{colorama.Fore.Red}Test run failed.{colorama.Fore.RESET}")
print(f"Tested: {test_count}, "
      f"{colorama.Fore.GREEN}Succeeded: {colorama.Fore.RESET}{succeeded_test_count}, "
      f"{colorama.Fore.RED}Failed: {colorama.Fore.RESET}{failed_test_count}\n"
      f"Time Elapsed: %s sec" % (end_time - start_time))
