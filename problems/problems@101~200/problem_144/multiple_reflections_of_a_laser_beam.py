from fractions import Fraction
from mylib import gcd


class Slope:
    def __init__(self, a, b):
        a, b = a.numerator * b.denominator, b.numerator * a.denominator

        d = gcd(abs(a), abs(b))
        self.a = a // d
        self.b = b // d

    def reflection(self, k):
        x = self.a * k.a + self.b * k.b
        y = -self.a * k.b + self.b * k.a
        return Slope(x * k.a + y * k.b, x * k.b - y * k.a)

    def insection(self, x0, y0):
        s = 4 * self.a**2 + self.b**2
        x = (self.b**2 * x0 - 2 * self.a * self.b * y0 -
             4 * self.a**2 * x0) / s
        y = self.b * (x - x0) / self.a + y0
        return x, y


if __name__ == '__main__':
    k = Slope(-14, 197)
    x0, y0 = Fraction(7, 5), Fraction(-48, 5)

    hit = 0
    eps = Fraction(1, 100)
    while True:
        hit += 1
        k = k.reflection(Slope(4 * x0, y0))
        x0, y0 = k.insection(x0, y0)
        print(float(x0), len(str(x0)), hit)
        if abs(x0) <= eps:
            print(hit)
            break
