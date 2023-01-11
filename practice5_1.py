

class Fraction:
    def __init__(self, s, m):
        self.soorat = s
        self.makhraj = m


    def show(self):
        print(self.soorat, "/", self.makhraj)


    def mul(self, f2):
        result = Fraction(None, None)
        result.soorat = self.soorat * f2.soorat
        result.makhraj = self.makhraj * f2.makhraj
        return result

    def sum(self, f2):
        result = Fraction(None, None)
        result.soorat = self.soorat * f2.makhraj + f2.soorat * self.makhraj
        result.makhraj = self.makhraj * f2.makhraj
        return result


    def minus(self, f2):
        result = Fraction(None, None)
        result.soorat = self.soorat * f2.makhraj - f2.soorat * self.makhraj
        result.makhraj = self.makhraj * f2.makhraj
        return result


    def div(self, f2):
        result = Fraction(None, None)
        result.soorat = self.soorat * f2.makhraj
        result.makhraj = self.makhraj * f2.soorat
        return result


fraction1 = Fraction(2, 3)
print("\nFirst Fraction is: ")
fraction1.show()

fraction2 = Fraction(3, 4)
print("\nSecond Fraction is: ")
fraction2.show()

mul = fraction2.mul(fraction1)
print("\nMultiplication is: ")
mul.show()

sum = fraction2.sum(fraction1)
print("\nSum is: ")
sum.show()

minus = fraction2.minus(fraction1)
print("\nMinus is: ")
minus.show()

division = fraction2.div(fraction1)
print("\nDivision is: ")
division.show()