import math 

# number 
x = 1
x = 2.2 
x = 1 + 2j 

# arithmetic oparators 
print(10 + 8)
print(10 - 8)
print(10 / 8)
print(10 // 8) # floor, will return a int without decimals
print(10 % 8) # modules, will return the remainder of a divison
print(10 ** 8) # exponent, 10 to the power of 8

x = 10 
x = 10 + 8
x += 8  # shorter form 


# useful funtions for int
print(round(15.3600089))
print(abs(-12.99)) 

print(math.ceil(9.3)) 

# alwsys use input() to ask user something
x = input("age:")
y = int(x) + 1 # converting to int 
print(f"my X: {x}, my Y: {y}")



# if/ else statements


temp = 29 
if temp > 76: 
    print(f"Its hot today. \nStay hydrated") # \n is used to print on the next line
elif temp > 30:
    print(f"woo, its warm today.")
else: 
    print(f"its cold")


age = 30
if age >= 18:
    print("is eligible")
else: 
    print(f"not eligible")


# Shorter form of if/else statemnets 
message = "is eligible" if age >=18 else "Not eligible"


# logical operator and/or/not 

high_income = True
good_credit = False

if high_income and good_credit:
    print(f"Eligable for loan")
else:
    print(f"Not eligible")


degree = False 
exp = False 
current_student = True

if degree or exp:
    print(f"Good candidate for the job")
else:
    print(f"bad candidate")



if not current_student:
    print(f"Candidate still needs to finish college")
else:
    print(f"Candiadate is ready")


if (not current_student and degree) or exp:
    print("candidate with experience can apply")
else: 
    print("Can't apply yet")


# Compasion operators 

# example

if 10 == "10": 
    print("a")
elif "bag" > "apple" and "bag" > "cat": # in ASCII value 
    print("b")
else: 
    print("c")








