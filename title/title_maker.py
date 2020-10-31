
title = input("Digite um título: ").strip().title()
title = f"** {title} **"

border = "-=" * len(title)
border = border[0: len(title)]

print(border)
print(title)
print(border)
