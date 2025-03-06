print("Welcome to \"The Hobbit Gauge\"!")

checker = True
while checker == True:

    height = int(input("What is your height in cm?\n(Type 0 to exit.)\n"))

    if height > 0:
        if height > 60 and height <= 125:
            print("You may be a hobbit!")
            print("Now, let's see how long you have lived.")
            age = int(input("How old are you? Type the number:\n"))

            if age > 0 and age <= 20:
                print(f"{age} years old? You are a very young hobbit!")
            elif age > 20 and age <= 50:
                print("You can already be on an adventure!")
            elif age > 50 and age <= 100:
                print("You've certainly lived a life.")
            elif age > 100 and age <= 160:
                print("Death may be near, my friend.")
            elif age > 160:
                print("You're either lying now or you're no hobbit; therefore, you lied earlier.")
            else: 
                if age == 0:
                    print("I understand, bye.")
                else:
                    print("Invalid data.")
                checker = False
                break
                
        else:
            print("Don't be sad, you may be another creature.")
            checker = False
            break

    else:  
        print("Ok, bye.")
        checker = False
        break
        
        

    breakfast = int(input("The final question is: How many breakfasts grace your belly?\n"))
    if breakfast == 2:
        print("You are a hobbit indeed!")
    elif breakfast == 1: 
        print("I assume you may be a human.\nA peculiar human, but a human nonetheless.")
    elif breakfast == 3:
        print("Hungry fella!")
    elif breakfast > 3:
        print("Seek help, my friend.")
    elif breakfast == 0:
        print("No breakfast, I see. Bye.")
        checker = False
    else: 
        print("Invalid data.")
    
    checker = False