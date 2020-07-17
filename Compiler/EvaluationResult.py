class EvaluationResult:
    def __init__(self, diagnostics, value):
        self._diagnostics = diagnostics
        self._value = value

    def get_diagnostics(self):
        return self._diagnostics

    def get_value(self):
        return self._value