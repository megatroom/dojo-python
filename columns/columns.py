total = int(input("Digite o total de números: "))

for row in range(1, total + 1):
    line = ""
    for column in range(1, row + 1):
        line += f"{column} "
    print(line)

# for row in range(1, total + 1):
#     for column in range(1, row + 1):
#         print(column, end=" ")
#     print()
