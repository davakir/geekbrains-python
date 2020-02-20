class ComplexNumber:
    def __init__(self, a, b):
        self.real_z = a
        self.imaginary_z = b

    def __str__(self):
        if self.imaginary_z < 0:
            sign = '-'
        else:
            sign = '+'

        self.imaginary_z = abs(self.imaginary_z)

        return f'{self.real_z} {sign} {self.imaginary_z}i'

    def __add__(self, other_complex):
        real = self.real_z + other_complex.real_z
        imaginary = self.imaginary_z + other_complex.imaginary_z

        return ComplexNumber(real, imaginary)


cn1 = ComplexNumber(-3.33, -8)
cn2 = ComplexNumber(90, 87.9999)
print(cn1 + cn2)
