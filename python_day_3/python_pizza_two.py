print("Olá, esta é a Pizzaria Fabulosa.")
pronto = input("Está pronto para pedir? Digite sim ou não.\n").lower()

if pronto == "sim":
    print("Perfeito.")
elif pronto == "não":
    print("Tudo bem.")
    exit()
else:
    print("Comando inválido.")
    exit()

total = 0

categoria = input("Quer a pizza normal ou especial?\n").lower()
tamanho = input("Média ou grande?\n").lower()
extra = input("Queijo extra? Digite sim, ou não.\n").lower()

if (categoria == "normal" and tamanho == "média" and extra == "sim"):
    total += 22
    print(f"Sua refeição custará {total} reais. Obrigado e volte sempre.")
elif (categoria == "normal" and tamanho == "grande" and extra == "sim"):
    total += 27
    print(f"Sua refeição custará {total} reais. Obrigado e volte sempre.")
elif (categoria == "normal" and tamanho == "média" and extra == "não"):
    total += 20
    print(f"Sua refeição custará {total} reais. Obrigado e volte sempre.")
elif (categoria == "normal" and tamanho == "grande" and extra == "não"):
    total += 25
    print(f"Sua refeição custará {total} reais. Obrigado e volte sempre.")
elif (categoria == "especial" and tamanho == "média" and extra == "não"):
    total += 30
    print(f"Sua refeição custará {total} reais. Obrigado e volte sempre.")
elif (categoria == "especial" and tamanho == "grande" and extra == "não"):
    total += 35
    print(f"Sua refeição custará {total} reais. Obrigado e volte sempre.")
elif (categoria == "especial" and tamanho == "média" and extra == "sim"):
    total += 33
    print(f"Sua refeição custará {total} reais. Obrigado e volte sempre.")
elif (categoria == "especial" and tamanho == "grande" and extra == "sim"):
    total += 38
    print(f"Sua refeição custará {total} reais. Obrigado e volte sempre.")