
total = float(input("Digite o total da compra: R$ "))

if total < 280:
    percentage = 5
elif total < 800:
    percentage = 10
elif total < 1200:
    percentage = 15
else:
    percentage = 18

discount = (percentage * total) / 100
result = total - discount

print(f"Desconto: R$ {discount:.2f}")
print(f"Porcentagem: {percentage}%")
print(f"Valor final: R$ {result:.2f}")
