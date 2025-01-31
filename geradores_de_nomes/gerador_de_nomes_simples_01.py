print("Este é um gerador de nomes.")

name = True
while name:
    bicho = input("Digite o nome de um bicho: ").title()
    cidade = input("Digite o nome de um lugar: ").title()
    adjetivo = input("Digite um adjetivo: ").title()
    print(f"O nome do seu grupo pode ser {bicho} {adjetivo} de {cidade}")

    continuar = input("Deseja gerar outro nome? ").lower()
    if continuar == "não":
        print("Até mais.")
        name = False
    elif continuar == "sim":
        print("Sigamos.")
    else:
        print("Resposta inválida.")
        break