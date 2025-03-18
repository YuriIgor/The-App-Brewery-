import random

random_integer_one = random.randint(1, 10)
print(random_integer_one)

random_float_one = random.random()
print(random_float_one)

another_random_float_one = random.uniform(1, 60)
print(another_random_float_one)

print("\nHere's a new round:\n")

random_integer_two = random.randint(2, 15)
random_float_two = random.random() * 5
another_random_float_two = random.uniform(22, 25)
print(random_integer_two)
print(random_float_two)
print(another_random_float_two)

print("\nHere's a new round:\n")

random_integer_three = random.randint(1, 1000)
random_float_three = random.random() * 10 - 2
another_random_float_three = random.uniform(12, 200)
print(random_integer_three)
print(random_float_three)
print(another_random_float_three)

print("\nHere's another round:\n")

random_integer_four = random.randint(1, 10000)
random_float_four = random.random() / 2
another_random_float_four = random.uniform(0.5, 0.8)
print(random_integer_four)
print(random_float_four)
print(another_random_float_four)

print("\nHere's the final round:\n")

random_integer_five = random.randint(0,500)
random_float_five = random.random() * 6
another_random_float_five = random.uniform(40, 256)
print(random_integer_five)
print(random_float_five)
print(another_random_float_five)