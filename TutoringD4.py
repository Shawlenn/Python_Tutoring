import random



# Exercise: Write a program to remove the duplicates in a list 

ages = [10, 12, 14, 6, 20, 12, 10, 6]
uniques = []

for age in ages:
    if age not in uniques:
        uniques.append(age)
print(uniques)




# There are two friends, John and Smith, and the parameters (variables) j_angry and s_angry to indicate if each is
# angry. You are in trouble if both of them are angry and not  if one/none of them is angry. ​



j_angry = False
s_angry = True

if not j_angry and s_angry:
    print("I'm not in trouble")
elif j_angry or s_angry:
      print("One of them is angry")
else: 
    print("I'm in trouble")





# Type funtion --- it tells u what type of obj ur variable is
v = "something" 
print(type(v))
print(type(10))
print(type(range(10))) # complex type




# while loop section 

num = 10 

while num > 0:
    print(num)
    num //= 2
   


commmand = " "
while commmand.lower() != "quit":
    commmand = input("Type here: ")
    print("Echo", commmand)



# exercise 3: Ask the user to roll a dice answering  in (y/n). If the user enters anything else other than y/n, print "Invalid
# choice!". If answered y, randomly generate 2 numbers. Only quit the program when users answers n. Print
# "Thanks for playing" message after user quit the program​



while True:
    choice = input("Roll the dice? (y/n) ").lower()

    if choice == "y": 
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(f"({die1}, {die2})")
    elif choice == "n":
        print("Thanks for playing!")
        break
    else: 
        print(f"Invalid choice")






# Funtion --- 2 types: 1. Performs a task  2. Return a value


def greet(first_name, last_name): 
    print(f"Hello, {first_name}, {last_name}")
    print("Welcome to my learning course.")

greet("Jason", "Moore")
greet("Allie", "Nelson")




def get_greetings(name):
    return f"Hi, {name}"


message = get_greetings("Soumia")
print(message)





def increment(number, by):
    return number + by 

result = increment (2, 1)
print(f"result is: {result}")

print(increment(2, 4))



# Tuples -- similar to lists[], but they're not changable like list[]
# Once they're created, they stay like that 

numbers = (1, 2, 3)
print(numbers[2])


def multiply(*numbers):    # tuple - similar to lists[]
    total = 1
    for number in numbers:
        total = total * number
    return total 

print(multiply(2, 7, 3, 6))




# unpacking 
coordinates = (1, 2, 3)
"""
x = coordinate[0]
y = coordinate[1]
z = coordinate[2]

"""


x, y, z = coordinates
print(x)



# Dictionaries -- allows to map a key to a value


pNum = input("Enter your number: ")
degits_mapping = {
    "0" : "Zero",
    "1" : "One",
    "2" : "Two",
    "3" : "Three",
    "4" : "Four",
    "6" : "Six",

}

output = ""

for character in pNum:
    output = output + degits_mapping.get(character, "!" ) + " "
print(output)







    


