import random

nome = True
while nome:

    print("\nForja o nome da tua espada!\n")

    substantivo_um = input("Digite um substantivo: ").title()
    substantivo_dois = input("Digite mais um substantivo: ").title()
    substantivo_terceiro = input("Digite o último substantivo: ").title()
    adjetivo_um = input("Digite um adjetivo: ").title()
    adjetivo_dois = input("Digite mais um adjetivo: ").title()
    adjetivo_terceiro = input("Digite o último adjetivo: ").title()
    palavra_aleat_um = input("Digite uma palavra aleatória: ").title()
    palavra_aleat_dois = input("Digite outra palavra aleatória: ").title()

    subadj = [substantivo_um, substantivo_dois, substantivo_terceiro,
               adjetivo_um, adjetivo_dois, adjetivo_terceiro,
               palavra_aleat_um, palavra_aleat_dois]
    subadj_choice_one = random.choice(subadj)
    subadj_choice_two = random.choice(subadj)

    print(f"\nEis o nome da tua espada: \"{subadj_choice_one} {subadj_choice_two}\"!")

    adiante = True
    while adiante:
        prosseguir = input("\nQueres outro nome?\n").lower()
        if (prosseguir == "sim" or prosseguir == "s"):
            adiante = False
            continue
        elif (prosseguir == "não" or prosseguir == "n"):
            adiante = False
            nome = False
            print("Perfeito, adeus.")
        else:
            print("Resposta inválida.")
