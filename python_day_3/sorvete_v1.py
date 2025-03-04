conta = 0

sorvete = True
while sorvete:
  
  print("Escolha seu sorvete!")
  sabor = input("Qual sabor? Temos morango, chocolate e baunilha.\n").lower()
  if sabor == "morango":
    conta += 10
  elif sabor == "chocolate":
    conta += 8
  elif sabor == "baunilha":
    conta += 12
  else:
    print("Não temos esse sabor")

  
  tamanho = input("Qual o tamanho? Temos pequeno, médio e grande.\n").lower()
  if tamanho == "pequeno":
    conta += 5
  elif tamanho == "médio":
    conta += 6
  elif tamanho == "grande":
    conta += 10
  else:
    print("Não temos esse tamanho.")
  
  local = input("Vai tomar aqui ou levar?\n").lower()
  if local == "aqui":
    conta += 0
  elif local == "levar":
    conta += 2
  else:
    print("Não temos esse local.")

  new_sabor = input("Quer mais algum sabor? Sim ou não?\n").lower()
  if new_sabor == "sim":
    sorvete = True
  elif new_sabor == "não":
    sorvete = False
    print(f"Muito bem, o valor da sua conta é de R${conta},00. Volte sempre.")
  else:
    print("Comando inválido.")