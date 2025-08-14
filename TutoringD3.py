
# For loop 

successful = True 

for number in range(3):
    print(f"for loop attempt", number)
    if successful:
        print("Attempt successful")
    else:
        print("Attempted 3 times,but failed.")


# Nested loop 

for x in range(5):
    for y in range(3):
        print(f"{x},{y}")


# example 

for everyStu in range(1, 4):
    print(f"This is student number ", everyStu)


# example: Print all even numbers between (1-10)

count = 0
for num in range(1, 10):
    if num % 2 == 0:
        count = count + 1  # Every time you find an even number, you add 1 to the total you already had
        print(num)
print(f"We have {count} even numbers.")



# List[]

citis = ["NYC", "Philly", "Media", "Delaware"]
pop = [11000, 5000, 3000, 12000]


for city in citis:
    print(city)
    if city == "Philly":
        print("This is my city")
        break
else:
    print("All the citie i've visited.")




for city, pop in zip(citis, pop):   # using zip() to print city and population together
    print(f"{city}, {pop}")



# useful methods to use with list[]

numbers = [4, 8, 9, 9, 19, 22, 40]
print(f"The original set is: {numbers}" )

numbers.pop() # taking last number away
print(f"List using pop() funtion: {numbers}" )

numbers.append(20) # adding a number to the list, which will add at the end
print(f"List using append() funtion: {numbers}" )

numbers.insert(2, 33) # insering number before
print(f"List after inserting number in certain place: {numbers}" )

numbers.remove(19)
print(f"List after removing a number: {numbers}" )

print(numbers.index(8)) # Asking what place is 8 in
print(80 in numbers) # Asking if 80 isin the list
print(numbers.count(9)) # Asking to count how many times 9 repeated in the list


num = numbers.copy()   # Copying the set (after doing all the methods) to a new variable called num
num.append(10)  # Adding a new number to num list
print(f"Num list is: {num}") 




