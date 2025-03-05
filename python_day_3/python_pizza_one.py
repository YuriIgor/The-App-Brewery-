print("Hello, make your choices!")
size = input("What is the size of your pizza? Type S for Small, M for Medium and L for Large: ").upper()
add_pepperoni = input("Do you want pepperoni? Type Y for Yes, N for No: ").upper()
extra_cheese = input("Do you want extra cheese? Type Y for Yes, N for No: ").upper()

small_bill = 15
medium_bill = 20
large_bill = 25

if (size == "S" and add_pepperoni == "N" and extra_cheese == "N"):
  print("Thank you for choosing Python Pizza Deliveries!")
  print(f"Your final bill is: ${small_bill}.")
elif (size == "S" and add_pepperoni == "Y" and extra_cheese == "N"):
   small_bill += 2
   print("Thank you for choosing Python Pizza Deliveries!")
   print(f"Your final bill is: ${small_bill}.")
elif (size == "S" and add_pepperoni == "N" and extra_cheese == "Y"):
   small_bill += 1
   print("Thank you for choosing Python Pizza Deliveries!")
   print(f"Your final bill is: ${small_bill}.")
elif (size == "S" and add_pepperoni == "Y" and extra_cheese == "Y"):
   small_bill += 3
   print("Thank you for choosing Python Pizza Deliveries!")
   print(f"Your final bill is: ${small_bill}.")

if (size == "M" and add_pepperoni == "N" and extra_cheese == "N"):
   print("Thank you for choosing Python Pizza Deliveries!")
   print(f"Your final bill is: ${medium_bill}.")
elif (size == "M" and add_pepperoni == "Y" and extra_cheese == "N"):
   medium_bill += 2
   print("Thank you for choosing Python Pizza Deliveries!")
   print(f"Your final bill is: ${medium_bill}.")
elif (size == "M" and add_pepperoni == "N" and extra_cheese == "Y"):
   medium_bill += 1
   print("Thank you for choosing Python Pizza Deliveries!")
   print(f"Your final bill is: ${medium_bill}.")
elif (size == "M" and add_pepperoni == "Y" and extra_cheese == "Y"):
   medium_bill += 3
   print("Thank you for choosing Python Pizza Deliveries!")
   print(f"Your final bill is: ${medium_bill}.")

if (size == "L" and add_pepperoni == "N" and extra_cheese == "N"):
  print("Thank you for choosing Python Pizza Deliveries!") 
  print(f"Your final bill is: ${large_bill}.")
elif (size == "L" and add_pepperoni == "Y" and extra_cheese == "N"):
   large_bill += 3
   print("Thank you for choosing Python Pizza Deliveries!") 
   print(f"Your final bill is: ${large_bill}.")
elif (size == "L" and add_pepperoni == "N" and extra_cheese == "Y"):
   large_bill += 1
   print("Thank you for choosing Python Pizza Deliveries!") 
   print(f"Your final bill is: ${large_bill}.")
elif (size == "L" and add_pepperoni == "Y" and extra_cheese == "Y"):
   large_bill += 4
   print("Thank you for choosing Python Pizza Deliveries!") 
   print(f"Your final bill is: ${large_bill}.")