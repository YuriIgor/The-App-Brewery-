print("Este é o Kart do Miguel!")
height = int(input("Qual é a sua altura em cm? "))
bill = 0 

if height >= 120:
  print("Muito bem, tens altura o bastante para o Kart.")
  
  age = int(input("Quantos anos você tem? "))
  if age >= 18:
    print("O preço para adultos é R$, 50,00")
    bill = 50
  elif age >= 12:
    print("O preço para adolescentes é R$ 30,00")
    bill = 30
  elif age < 12:
    print("O preço para crianças é R$ 20,00")
    bill = 20 

  photo = input("Quer fotos? Digite 'sim' ou 'não'.").lower()
  if photo == "sim":
    bill += 5
    print(f"O preço total é R${bill},00.\nObrigado e boa corrida!")
  else:
    print(f"O preço total é R${bill},00.\nObrigado e boa corrida!")

else:
  print("Infelizmente, não tens altura o bastante para o Kart.")