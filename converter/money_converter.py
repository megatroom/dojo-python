
def money_converter(value, currency):
    if currency == "R":
        return value * 6

    return value / 6


if __name__ == "__main__":
    value = float(input("Entre com o valor: "))
    currency = input("(R)eais ou (D)ollar? ").upper()
    print(money_converter(value, currency))
