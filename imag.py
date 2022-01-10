import math
import cmath


class imag:
    def __init__(self, a, b):
        self.a = float(a)
        if math.fabs(self.a) < 0.00000000001:
            self.a = 0
        self.b = float(b)
        if math.fabs(self.b) < 0.00000000001:
            self.b = 0

    def __repr__(self):
        return f"imag({self.a}, {self.b})"

    def __str__(self):
        if self.a == 0:
            if self.b == 0:
                return "0"

            try:
                return f"{int(self.b)}i"
            except ValueError:
                return f"{self.b}i"

        if self.b == 0:
            try:
                return str(int(self.a))
            except ValueError:
                return str(self.a)

        if self.b > 0:
            if self.a < 0:
                try:
                    return f"{int(self.b)}i - {math.fabs(int(self.a))}"
                except ValueError:
                    return f"{self.b}i - {math.fabs(self.a)}"
            try:
                return f"{int(self.a)} + {int(self.b)}i"
            except ValueError:
                return f"{self.a} + {self.b}i"
        try:
            return f"{int(self.a)} - {math.fabs(int(self.b))}i"
        except ValueError:
            return f"{self.a} - {math.fabs(self.b)}i"

    def __add__(self, other):
        if isinstance(other, imag):
            return imag(self.a + other.a, self.b + other.b)

        if isinstance(other, int) or isinstance(other, float):
            return imag(self.a + float(other), self.b)

        raise NotImplementedError

    def __radd__(self, other):
        if isinstance(other, imag):
            return imag(self.a + other.a, self.b + other.b)

        if isinstance(other, int) or isinstance(other, float):
            return imag(self.a + float(other), self.b)

        raise NotImplementedError

    def __sub__(self, other):
        if isinstance(other, imag):
            return imag(self.a - other.a, self.b - other.b)

        if isinstance(other, int) or isinstance(other, float):
            return imag(self.a - float(other), self.b)

        raise NotImplementedError

    def __rsub__(self, other):
        if isinstance(other, imag):
            return imag(self.a - other.a, self.b - other.b)

        if isinstance(other, int) or isinstance(other, float):
            return imag(self.a - float(other), self.b)

        raise NotImplementedError

    def __mul__(self, other):
        if isinstance(other, imag):
            return imag(
                (self.a * other.a - self.b * other.b),
                (self.a * other.b + self.b * other.a),
            )

        if isinstance(other, int) or isinstance(other, float):
            return imag(float(other) * self.a, float(other) * self.b)

        raise NotImplementedError

    def __rmul__(self, other):
        if isinstance(other, imag):
            return imag(
                (self.a * other.a - self.b * other.b),
                (self.a * other.b + self.b * other.a),
            )

        if isinstance(other, int) or isinstance(other, float):
            return imag(float(other) * self.a, float(other) * self.b)

        raise NotImplementedError

    def __rpow__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            return imag(
                (other ** self.a) * math.cos(self.b * math.log(other)),
                math.sin(self.b * math.log(other)),
            )

        # Polar representation will need to be implemented for this, but I don't need that!
        raise NotImplementedError

    def __pow__(self, other):
        if isinstance(other, int) and other > 1:
            total = 1
            while other > 0:
                total = total * self
                other -= 1
            return total

        raise NotImplementedError


def main():
    print("e ** (i * pi):")
    print(cmath.e ** (imag(0, 1) * cmath.pi))
    print("(2 + 3i) ** 5:")
    print(imag(2, 3) ** 5)


if __name__ == "__main__":
    main()
