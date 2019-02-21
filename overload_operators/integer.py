class Integer(int):

    def __add__(self, other):
        print('chegou!!!!')
        return 42

    def __sub__(self, other):
        return 42

    def __mul__(self, other):
        return 42

    def __floordiv__(self, other):
        return 42

    def __truediv__(self, other):
        return 42


class AnotherInteger(int):

    def __radd__(self, other):
        return 12

if __name__ == '__main__':
    print(Integer(2) + 2)
    print(Integer(2) - 2)
    print(Integer(2) * 2)
    print(Integer(2) / 2)

    print(2 + Integer(2))
    print(2 - Integer(2))
    print(2 * Integer(2))
    print(2 / Integer(2))

    print(Integer(4) + AnotherInteger(2))