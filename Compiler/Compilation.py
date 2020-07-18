from Compiler.Binding.Binder import Binder
from Compiler.EvaluationResult import EvaluationResult
from Compiler.Evaluator import Evaluator
from Compiler.Syntax.SyntaxTree import SyntaxTree


class Compilation:
    def __init__(self):
        self._syntax_tree = None

    def set_syntax_tree(self, syntax_tree: SyntaxTree):
        self._syntax_tree = syntax_tree

    def evaluate(self, variables):
        binder = Binder()
        binder.set_syntax_tree(self._syntax_tree)
        binder.set_variable(variables)
        self._syntax_tree.print()
        bound_expression = binder.bind()

        diagnostics = self._syntax_tree.get_diagnostics()
        if len(diagnostics.get_diagnostic()) != 0:
            return EvaluationResult(diagnostics, None)

        evaluator = Evaluator()
        evaluator.set_root(bound_expression)
        evaluator.set_variables(variables)
        value = evaluator.evaluate()

        return EvaluationResult(diagnostics, value)
