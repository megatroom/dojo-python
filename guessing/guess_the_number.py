from random import randint


def guess_the_number():
    secret_number = 6
    attempts = 0
    while attempts < 3:
        number = int(input("Adivinhe: "))
        if number == secret_number:
            print("Você acertou!")
            break
        attempts += 1
    else:
        print("Você perdeu :(")


def guess_the_random_number():
    secret_number = randint(1, 10)
    attempts = 0
    while attempts < 3:
        number = int(input("Adivinhe: "))
        if number == secret_number:
            print("Você acertou!")
            break
        attempts += 1
    else:
        print("Você perdeu :(")


if __name__ == "__main__":
    guess_the_random_number()
