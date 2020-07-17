class TextSpan:
    def __init__(self, start, end):
        self._start = start
        self._end = end
        self._length = end - start

    def get_start(self):
        return self._start

    def get_end(self):
        return self._end

    def get_length(self):
        return self._length
