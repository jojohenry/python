name = input("What is your name? ")
color = input("What is your favorite color? ")
age = int(input("How old are you? "))
food = input("What is your favorite food? ")
vacation = input("What's your favorite place to travel to? ")

print(name, end=" ")
print("is " + str(age) + " years old", end=" ")
print("and loves the color " + color + ".", end= " ")
print(name + " also enjoys traveling to " + vacation + " and their favorite food is " + food + ".", end=" " )
