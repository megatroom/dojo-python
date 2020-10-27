vowels = "a", "e", "i", "o", "u"


def consonants(text):
    result = ""
    for x in text:
        if x not in vowels:
            result += x
    return result


if __name__ == "__main__":
    text = input("Entre com o texto: ")
    print(consonants(text))
