from math import sqrt

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

delta = b ** 2 - 4 * a * c
x1 = (-b + sqrt(delta)) / 2 * a
x2 = (-b - sqrt(delta)) / 2 * a

print(f"x' = {x1}")
print(f"x'' = {x2}")
