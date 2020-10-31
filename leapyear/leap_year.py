from datetime import date

year = input("Digite o ano ou deixe em branco para o ano atual: ")

if not year:
    year = date.today().year
else:
    year = int(year)

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print(f"O ano {year} é bissexto")
else:
    print(f"O ano {year} não é bissexto")
