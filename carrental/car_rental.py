days = int(input("Dias alugados: "))
km = float(input("Km rodados: "))

total = (days * 100) + (km * 0.15)

print(f"Total a pagar: R$ {total:.2f}")
