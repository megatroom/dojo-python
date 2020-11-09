size = int(input("Total: "))

for row in range(1, size + 1):
    print("* " * row)

for row in range(size - 1, 0, -1):
    print("* " * row)
