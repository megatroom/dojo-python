class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return 3.14 * (self.radius ** 2)

    def get_circumference(self):
        return self.radius * 2 * 3.14


radius = float(input("Digite o radius: "))

c = Circle(radius)
print(f"Área = {c.get_area()}")
print(f"Circunferência = {c.get_circumference()}")
