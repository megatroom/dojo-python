from random import choice, randint

answers = ["sim", "não", "talvez", "claro", "com certeza", "quem sabe um dia"]

input("Entre com sua pergunta: ")
print(choice(answers))

index = randint(0, len(answers))
input("Entre com sua pergunta: ")
print(answers[index])
