def _render(width, length):
    return ('*' * width + '\n') * length

class RW_Rectangle(object):
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def __str__(self):
        return _render(self.width, self.length)

class RW_Square(object):
    def __init__(self, size):
        self.size = size

    def __str__(self):
        return _render(self.size, self.size)

if __name__ == '__main__':
    print(RW_Rectangle(4, 5))
    print()
    aSquare = RW_Square(4)
    aSquare.size = 17
    print(aSquare)
