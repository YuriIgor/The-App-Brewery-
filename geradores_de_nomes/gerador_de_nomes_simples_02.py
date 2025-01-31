print("This is a name generator.")

name = True
while name:

  adjective = input("Enter an adjective: ").title()
  noun = input("Enter a noun: ").title()
  city = input("Enter the name of a city: ").title()
  namegen_one = adjective + " " + noun + " " + "of" + " " + city
  namegen_two = noun + " " + adjective

  print(f"The name could be \"{namegen_one}\" or \"{namegen_two}\".")

  the_question = True
  while the_question:
      question = input("Do you want to generate another name? ").lower()
      if question == "no":
        print("Ok, bye.")
        name = False
        the_question = False
      elif question == "yes":
        print("All right.")
        name = True
        the_question = False
      else:
        print("Invalid answer.")
        continue