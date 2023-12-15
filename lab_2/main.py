class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        self._reduce()

    def _reduce(self):
        g = self._gcd(self.numerator, self.denominator)
        self.numerator //= g
        self.denominator //= g

    def _gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def __add__(self, other):
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __sub__(self, other):
        new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __mul__(self, other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __truediv__(self, other):
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return Fraction(new_numerator, new_denominator)

    def __str__(self):
        return f'{self.numerator}/{self.denominator}'


f1 = Fraction(1, 2)
f2 = Fraction(3, 4)

addition = f1 + f2
subtraction = f1 - f2
multiplication = f1 * f2
division = f1 / f2

print(f'Operations on fractions: {f1} and {f2}')
print('Addition: ', str(addition))
print('Subtraction: ', str(subtraction))
print('Multiplication: ', str(multiplication))
print('Division: ', str(division))