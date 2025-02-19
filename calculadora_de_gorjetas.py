print("Está é a calculadora de gorjetas.")
conta = float(input("Qual o valor da conta?\nR$"))
gorjeta = int(input("Qual a porcentavem da gorjeta?\n" + "%"))
pessoas = int(input("Quantas pessoas dividirão a conta? "))
#pagamento = round(conta * (gorjeta / 100 + 1) / pessoas)
pagamento = round((gorjeta / 100 * conta + conta) / pessoas, 2)

print(f"Cada pessoa arcará com R${pagamento}.")