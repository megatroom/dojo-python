from random import choice

friends = input("Digite o nome dos amigos: ").split(",")

friends_copy = friends.copy()

print("Sorteio:")

for friend in friends:
    secret_friend = choice(friends_copy)
    print(f"{friend:10} => {secret_friend}")
    friends_copy.remove(secret_friend)
