import sys

class Racional(object):
    def __init__(self, divisor, dividendo):
        self._divisor = divisor
        self._dividendo = dividendo

    def getDivisor(self):
        return self._divisor

    def setDivisor(self, valor):
        self._divisor = valor

    divisor  = property(
            fget = getDivisor,
            fset = setDivisor)

    def getDividendo(self):
        return self._dividendo

    def setDividendo(self, valor):
        self._dividendo = valor

    dividendo = property(
            fget = getDividendo,
            fset = setDividendo)

    def __mul__(self, outro):
      divisor = self.divisor*outro.divisor
      dividendo = self.dividendo*outro.dividendo
      return Racional(divisor, dividendo)

    def __add__(self, outro):
      divisor = self.divisor * outro.dividendo + outro.divisor * self.dividendo
      dividendo = self.dividendo * outro.dividendo
      return Racional(divisor, dividendo)

    def __str__(self):
      return str(self.divisor) + '/' + str(self.dividendo)

    @staticmethod
    def main(*argv):
        # "Programa para o tesste do Racional"
        c = Racional(2, 3)
        print(c)

        c.divisor = 1
        c.divisor = 2
        print(c)

        c = Racional(1,2)
        d = Racional(3,4)
        print(c, d, c+d, c*d)
        return 0

print(__name__)
if __name__ == "__main__":
    sys.exit(Racional.main(*sys.argv))
