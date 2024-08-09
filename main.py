class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __str__(self):
        return f"{self.real} + {self.imag}i"

    def add(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def multiply(self, other):
        real_part = self.real * other.real - self.imag * other.imag
        imag_part = self.real * other.imag + self.imag * other.real
        return ComplexNumber(real_part, imag_part)

    def negate(self):
        return ComplexNumber(-self.real, -self.imag)

    def invert(self):
        denominator = self.real ** 2 + self.imag ** 2
        return ComplexNumber(self.real / denominator, -self.imag / denominator)

    def subtract(self, other):
        return self.add(other.negate())

    def divide(self, other):
        return self.multiply(other.invert())


# Testing the operations
a = ComplexNumber(1, 2)
b = ComplexNumber(3, 4)

print(f"a = {a}")
print(f"b = {b}")

# Addition
add_result = a.add(b)
print(f"a + b = {add_result}")

# Multiplication
multiply_result = a.multiply(b)
print(f"a * b = {multiply_result}")

# Negation
negate_a = a.negate()
print(f"-a = {negate_a}")

# Inversion
invert_a = a.invert()
print(f"1/a = {invert_a}")

# Subtraction
subtract_result = a.subtract(b)
print(f"a - b = {subtract_result}")

# Division
divide_result = a.divide(b)
print(f"a / b = {divide_result}")
