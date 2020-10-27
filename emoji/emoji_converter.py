emojis = {
    ":)": "😊",
    "B)": "😎",
    ":P": "😋"
}


def emoji_converter(text):
    words = text.split(' ')
    result = words.map
    for word in words:
        result += emojis.get(word, word) + " "
    return result


def emoji_converter2(text):
    words = text.split(' ')
    result = map(lambda word: emojis.get(word, word), words)
    return " ".join(list(result))


if __name__ == "__main__":
    text = input("Digite uma frase: ")
    print(emoji_converter2(text))
