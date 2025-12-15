import math
class Figura:
    def area(self):
        pass
    def perimetro(self):
        pass
class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def area(self):
        return self.base * self.altura
    def perimetro(self):
        return 2 * (self.base + self.altura)
class Triangulo(Figura):
    def __init__(self, base, altura, l1, l2, l3):
        self.base = base
        self.altura = altura
        self.l1 = l1
        self.l2 = l2
        self.l3 = l3
    def area(self):
        return (self.base * self.altura) / 2
    def perimetro(self):
        return self.l1 + self.l2 + self.l3
class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio
    def area(self):
        return math.pi * self.radio ** 2
    def perimetro(self):
        return 2 * math.pi * self.radio
figuras = []
b = float(input("Base rectangulo: "))
h = float(input("Altura rectangulo: "))
figuras.append(Rectangulo(b, h))
b = float(input("Base triangulo: "))
h = float(input("Altura triangulo: "))
l1 = float(input("Lado 1: "))
l2 = float(input("Lado 2: "))
l3 = float(input("Lado 3: "))
figuras.append(Triangulo(b, h, l1, l2, l3))
r = float(input("Radio circulo: "))
figuras.append(Circulo(r))
for f in figuras:
    print(type(f).__name__)
    print("Area: ", f.area())
    print("Perimetro: ", f.perimetro())