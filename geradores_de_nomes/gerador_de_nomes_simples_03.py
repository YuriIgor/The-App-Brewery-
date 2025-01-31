import random

print("Generate a name!\n")

name = True
while name:

  word_one = input("Enter a word: ").title()
  word_two = input("Enter a word: ").title()
  word_three = input("Enter another word: ").title()
  word_four = input("Enter another word: ").title()

  words = [word_one, word_two, word_three, word_four]
  word_choice_one = random.choice(words)
  word_choice_two = random.choice(words)

  print(
      f"The name could be \"{word_choice_one} {word_choice_two}\", or \"{word_choice_two} {word_choice_one}\"."
  )

  question = input("Generate another name? ").lower()
  if question == "no":
    name = False
  elif question == "yes":
    print("Roger that!\n")
    name = True
  else:
    print("Invalid answer.")
    break