import random

game = True
while game:

    head_tails = random.randint(1, 1000)
    print(head_tails)

    if head_tails % 2 == 0:
        print("Heads")
    else: 
        print("Tails")
    
    ask = input("Go again? ").lower()
    if ask == "y" or ask == "yes":
        print("All right!")
    else:
        game = False
        exit()
