
def min_and_max(list):
    highest = list[0]
    lowest = list[0]
    for n in list:
        if not highest or n > highest:
            highest = n
        if not lowest or n < lowest:
            lowest = n
    return highest, lowest


if __name__ == "__main__":
    numbers = input("Digite os números separados por vírgula: ")
    list = [int(n) for n in numbers.split(",")]
    print(min_and_max(list))
