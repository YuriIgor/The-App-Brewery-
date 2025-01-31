print("Gere um nome ao seu cachorro!\n")

name = True
while name: 

    comida = input("\nDigite o nome de uma comida: ").title()
    adjetivo = input("Digite um adjetivo: ").title()

    print(f"O nome do seu animal pode ser \"{comida} {adjetivo}\"!")
    prosseguir = input("\nGerar outro nome?\n").lower()

    if (prosseguir == "não" or prosseguir == "n"):
        name = False
        print("Entendido, até mais!")
    else:
        continue