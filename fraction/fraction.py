from math import gcd


class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

        if self.numerator == 0:
            self.denominator = 1
    
    def __str__(self):
        return f"{self.numerator} / {self.denominator}"
    
    def gcd(x, y):
        if x % y == 0:
            return y
        else:
            return gcd(x, x % y)
    def simplify_fraction(self):
        if self.numerator == 0:
            return self
        common_divisor = gcd(self.numerator, self.denominator)
        self.numerator = self.numerator // common_divisor
        self.denominator = self.denominator // common_divisor
        return self

    def __add__(self, y):
        resultant_numerator = self.numerator * y.denominator + y.numerator * self.denominator
        resultant_denominator = self.denominator * y.denominator
        return Fraction(resultant_numerator, resultant_denominator).simplify_fraction()

    def __sub__(self, y):
        resultant_numerator = self.numerator * y.denominator - y.numerator * self.denominator
        resultant_denominator = self.denominator * y.denominator
        return Fraction(resultant_numerator, resultant_denominator).simplify_fraction()

    def __mul__(self, y):
        resultant_numerator = self.numerator * y.numerator
        resultant_denominator = self.denominator * y.denominator
        return Fraction(resultant_numerator, resultant_denominator).simplify_fraction()

    def __truediv__(self, y):
        resultant_numerator = self.numerator * y.denominator
        resultant_denominator = self.denominator * y.numerator
        return Fraction(resultant_numerator, resultant_denominator).simplify_fraction()

    def __eq__(self, y):
        return (self - y).numerator == 0




x = Fraction(1, 10)
y = Fraction(1, 10)

print(x == y)