import colorama
import time

from Test.Syntax.LexerTexts import LexerTests

colorama.init()

test_count = 0
failed_test_count = 0
succeeded_test_count = 0

lexer_tests = LexerTests()

start_time = time.time()
lexer_tests.lexer_lex_token(lexer_tests.test_token_kind())
end_time = time.time()

test_count += lexer_tests.get_test_count()
failed_test_count += lexer_tests.get_failed_test_count()
succeeded_test_count += lexer_tests.get_succeeded_test_count()

time.sleep(0.1)
print(f"\nTested: {test_count}, "
      f"{colorama.Fore.GREEN}Succeeded: {colorama.Fore.RESET}{succeeded_test_count}, "
      f"{colorama.Fore.RED}Failed: {colorama.Fore.RESET}{failed_test_count}\n"
      f"Time Elapsed: %s sec" % (end_time - start_time))