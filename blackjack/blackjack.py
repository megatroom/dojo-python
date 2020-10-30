from random import randint


class Blackjack:
    def __init__(self, name):
        self.name = name
        self.cards = []

    def hit(self):
        new_card = randint(1, 10)
        self.cards.append(new_card)
        return new_card

    def total(self):
        result = 0
        for card in self.cards:
            result += card
        return result


players = [Blackjack("Player1"), Blackjack("Player2")]
winner = "Ninguém ganhou :/"
last_total = 0

for index, player in enumerate(players):
    option = ""

    if index == len(players) - 1 and last_total == 0:
        winner = f"Vencedor: {player.name}"
        break

    while option != "s":
        option = input(f"{player.name}: (M)ais um ou (S)air: ").lower()

        if option == "m":
            new_card = player.hit()
            total = player.total()
            print(f"{player.name}: Nova carta: {new_card} | Total: {total}")

            if total > 21:
                print(f"{player.name}: Você perdeu! :(")
                break
    else:
        current_total = player.total()
        if (current_total > last_total):
            winner = f"Vencedor: {player.name}"
            last_total = current_total

    print()

print(winner)
