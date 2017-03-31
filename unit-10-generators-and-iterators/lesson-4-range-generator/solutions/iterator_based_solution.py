class RmotrRange(object):
    def __init__(self, start, end, step=1):
        self.start = start
        self.end = end
        self.step = step
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration()

        num = self.current
        self.current += self.step
        return num

    next = __next__

rmotr_range = RmotrRange
