total = int(input("Digite o total de números: "))

for row in range(total, 0, -1):
    line = ""
    for column in range(row, 0, -1):
        line += f"{column} "
    print(line)
