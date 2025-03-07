from assets import title, n64, scorpio

print(title)
print("\n")
print("Estás no corredor")
primeira_escolha = input("Há uma porta de cada lado. Escolha uma digitando \"direita\" ou \"esquerda\".\n\n").lower()

if primeira_escolha == "esquerda": 
  segunda_escolha = input("Há uma escadaria que leva para baixo. Descer ou esperar?\n").lower()
  if segunda_escolha == "descer":
    print("Você desce e chega diante de três baús,\num de ouro, um de ferro, e outro de barro.")
    terceira_escolha = input("Qual você abre? Digite \"ouro\", \"ferro\", ou \"barro\".\n").lower()
    if terceira_escolha == "ouro": 
      print("O baú está vazio. Ao menos você sente\nque pode voltar para casa.")
    elif terceira_escolha == "ferro":
      print("Nostalgia!")
      print(n64)
      print("Você pega o console e sai feliz da vida.")
    elif terceira_escolha == "barro":
      print("Você se depara com um agrupamento de escorpiões amarelos")
      print(scorpio)
      print("Fim de jogo.")
  else: 
    print("A porta fechou e o chão abriu sob seus pés. Fim de jogo.")
else:
  print("Você toca na maçaneta e leva um choque fatal, a morte vem em sacolejos brutais.\nFim de Jogo.")
  