class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        self.value = self.numerator / self.denominator

    def simplify(self, fraction):
        for number in range(fraction.numerator, 1, -1):
            if fraction.numerator % number == 0 and fraction.denominator % number == 0:
                fraction.numerator = fraction.numerator // number
                fraction.denominator = fraction.denominator // number
        return fraction

    def __lt__(self, fraction_a, fraction_b):
        return fraction_a.value < fraction_b.value

    def __gt__(self, fraction_a, fraction_b):
        return fraction_a.value > fraction_b.value

    def __add__(self, fraction_a, fraction_b):
        result = ()
        if fraction_a.denominator == fraction_b.denominator:
            result = (fraction_a.numerator + fraction_b.numerator, fraction_a.denominator)
        else:
            result = (fraction_a.numerator * fraction_b.denominator + fraction_a.denominator * fraction_b.numerator, fraction_a.denominator * fraction_b.denominator)
        return self.simplify(result)

    def __sub__(self, fraction_a, fraction_b):
        result = ()
        if fraction_a.denominator == fraction_b.denominator:
            result = (fraction_a.numerator - fraction_b.numerator, fraction_a.denominator)
        else:
            result = (fraction_a.numerator * fraction_b.denominator - fraction_a.denominator * fraction_b.numerator, fraction_a.denominator * fraction_b.denominator)
        return self.simplify(result)

    def __eq__(self, fraction_a, fraction_b):
        if fraction_a.numerator == fraction_b.numerator and fraction_a.denominator == fraction_b.denominator:
            return True
        else:
            return False
