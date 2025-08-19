class ComplexNumber:
    def __init__(self, real, imaginary):
        # Initialize real and imaginary parts
        self.real = real
        self.imaginary = imaginary

    def add(self, other):
        # Add another ComplexNumber object
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)

    def subtract(self, other):
        # Subtract another ComplexNumber object
        return ComplexNumber(self.real - other.real, self.imaginary - other.imaginary)

    def multiply(self, other):
        # Multiply by another ComplexNumber object
        real_part = self.real * other.real - self.imaginary * other.imaginary
        img_part = self.real * other.imaginary + self.imaginary * other.real
        return ComplexNumber(real_part, img_part)

    def __eq__(self, other):
        # Compare two ComplexNumber objects
        return self.real == other.real and self.imaginary == other.imaginary

    def __str__(self):
        # Return string representation of the complex number
        # return f"{self.real} + {self.imaginary}i"
        if self.imaginary >= 0:
            return f"{self.real} + {self.imaginary}i"
        else:
            return f"{self.real} - {-self.imaginary}i"

