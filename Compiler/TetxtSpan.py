class TextSpan:
    def __init__(self, start, end, line=""):
        self._start = start
        self._end = end
        self._length = end - start
        self._line = line

    def get_start(self):
        return self._start

    def get_end(self):
        return self._end

    def get_length(self):
        return self._length

    def get_line(self):
        return self._line
