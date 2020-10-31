from random import choice

words = ['python', 'javascript', 'java', 'php', 'ruby', 'go']

word = choice(words)

hangman = ["_"] * len(word)

while "_" in hangman:
    print()
    print(" ".join(hangman))
    print()
    letter = input("Digite uma letra: ")
    if len(letter) != 1:
        print("Digite apenas uma letra!")
    else:
        if letter in word:
            for index, l in enumerate(word):
                if l == letter:
                    hangman[index] = letter

print()
print(" ".join(hangman))
print()
print("Você venceu!!!")
print()
