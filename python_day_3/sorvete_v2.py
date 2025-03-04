conta = 0

sorvete = True
while sorvete:
  

  print("Escolha seu sorvete!")
  sabor = input("Qual sabor? Temos morango, chocolate e baunilha.\n").lower()
  tamanho = input("Qual o tamanho? Temos pequeno, médio e grande.\n").lower()
  local = input("Vai tomar aqui ou levar?\n").lower()
  if (sabor == "morango" and tamanho == "pequeno" and local == "aqui"):
    conta += 15
  elif (sabor == "morango" and tamanho == "pequeno" and local == "levar"):
    conta += 17
  elif (sabor == "morango" and tamanho == "médio" and local == "aqui"):
    conta += 16
  elif (sabor == "morango" and tamanho == "médio" and local == "levar"):
    conta += 18
  elif (sabor == "morango" and tamanho == "grande" and local == "aqui"):
    conta += 20
  elif (sabor == "morango" and tamanho == "grande" and local == "levar"):
    conta += 22
  elif (sabor == "chocolate" and tamanho == "pequeno" and local == "aqui"):
    conta += 13
  elif (sabor == "chocolate" and tamanho == "pequeno" and local == "levar"):
    conta += 15
  elif (sabor == "chocolate" and tamanho == "médio" and local == "aqui"):
    conta += 14
  elif (sabor == "chocolate" and tamanho == "médio" and local == "levar"):
    conta += 16
  elif (sabor == "chocolate" and tamanho == "grande" and local == "aqui"):
    conta += 18
  elif (sabor == "chocolate" and tamanho == "grande" and local == "levar"):
    conta += 20
  elif (sabor == "baunilha" and tamanho == "pequeno" and local == "aqui"):
    conta += 17
  elif (sabor == "baunilha" and tamanho == "pequeno" and local == "levar"):
    conta += 19
  elif (sabor == "baunilha" and tamanho == "médio" and local == "aqui"):
    conta += 18
  elif (sabor == "baunilha" and tamanho == "médio" and local == "levar"):
    conta += 20
  elif (sabor == "baunilha" and tamanho == "grande" and local == "aqui"):
    conta += 22
  elif (sabor == "baunilha" and tamanho == "grande" and local == "levar"):
    conta += 24
  
  new_sabor = input("Quer mais algum sabor? Sim ou não?\n").lower()
  if new_sabor == "sim":
    sorvete = True
  elif new_sabor == "não":
    sorvete = False
    print(f"Muito bem, o valor da sua conta é de R${conta},00. Volte sempre.")
  else:
    print("Comando inválido.")