from random import randint

labels = ["", "Pedra", "Papel", "Tesoura"]

player1 = int(input("Pedra (1), Papel (2) ou Tesoura (3): "))
player2 = randint(1, 3)

print(f"Computador: {labels[player2]}")

if player1 == player2:
    print("Empate")
elif (player1 == 1 and player2 == 3) or (player1 == 2 and player2 == 1) or (player1 == 3 and player2 == 2):
    print("Você ganhou!")
else:
    print("O computador ganhou")
