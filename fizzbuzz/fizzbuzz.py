
def fizz_buzz(size):
    result = []

    for n in range(1, size + 1):
        if n % 3 == 0 and n % 5 == 0:
            result.append("FizzBuzz")
        elif n % 3 == 0:
            result.append("Fizz")
        elif n % 5 == 0:
            result.append("Buzz")
        else:
            result.append(n)

    return result


if __name__ == "__main__":
    size = input("Digite o tamanho da lista: ")
    result = fizz_buzz(int(size))
    print(result)
