print("Esta é a calculadora de impostos")

imposto = True
while imposto:

  valor_produto = float(input("Qual o valor do produto?\n"))
  quantidade_produto = float(input("Quantos produtos são?\n"))
  valor_imposto = float(input("Qual é o valor do imposto?\n"))
  valor_puro = valor_produto * quantidade_produto
  valor_acrescentado = valor_puro * (valor_imposto / 100)
  valor_total = valor_puro + valor_acrescentado
  
  # valor_total = valor_produto * quantidade_produto * (1 + valor_imposto / 100)
  
  print(f"O valor total da compra é de R${valor_total}0.")
  
  pergunta = input("Desejas comprar mais alguma coisa?\n")
  if pergunta == "não" or pergunta == "n":
      print("Até mais.")
      imposto = False
  else:
     print("Não entendi.")