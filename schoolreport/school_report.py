
def student_average(n1, n2, n3, n4):
    total = (n1 + n2 + n3 + n4) / 4
    return total, "reprovado" if total < 7 else "aprovado"


if __name__ == "__main__":
    n1 = input("Digite a 1ª nota: ")
    n2 = input("Digite a 2ª nota: ")
    n3 = input("Digite a 3ª nota: ")
    n4 = input("Digite a 4ª nota: ")
    average, result = student_average(int(n1), int(n2), int(n3), int(n4))
    print(f'{result} com a nota {average}')
