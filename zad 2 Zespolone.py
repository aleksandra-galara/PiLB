class ComplexNumber:
    def __init__(self, re, im):
        self.nRe = re
        self.nIm = im

    def __str__(self):
        return str(self.nRe) + "+" + str(self.nIm) + "i"

    def __add__(self, other):
        return ComplexNumber(other.nRe + self.nRe, other.nIm + self.nIm)

    def __sub__(self, other):
        return ComplexNumber(self.nRe - other.nRe, self.nIm - other.nIm)


x = ComplexNumber(2,4)
y = ComplexNumber(8,10)

print(x + y)
print(y - x)
