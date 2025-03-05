print("Welcome to the jungle! You won't survive!")
way = input("Which way do you want to go?\nLeft\nRight\nBack\nAhead\n").lower()

if way == "left":
  print("You were attacked by communist monkeys. Game over.")
elif way == "right":
  print("You were crushed by a Starlink Satellite. Game over.")
elif way == "back":
  print("You got lost and starved to death. Game over.")
elif way == "ahead":
  print("You found the mythical giant sloth, and it killed you. Game over.")
elif way == "None" or "Nowhere": 
  print("You've waited for a while and the rescue team saved you. You won!")
else:
  print("Invalid option, restart the game.")