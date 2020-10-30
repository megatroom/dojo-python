banknotes = [5, 10, 20, 50, 100, 200]

amount = float(input("Digite o valor do saque: "))

withdrawal = []
amount_left = amount
note = banknotes.pop()
while note:
    if amount_left >= note:
        withdrawal.append(note)
        amount_left -= note
    else:
        note = banknotes.pop() if len(banknotes) > 0 else None

if amount_left == 0:
    print(f"Notas: {withdrawal}")
else:
    print(f"Valor inválido, diferença de R$ {amount_left:.2f}")
