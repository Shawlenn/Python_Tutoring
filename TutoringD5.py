
# Dictionary 


zipCode = input("Enter your zip code: ")
digits_maping = {
    "0" : "Zero",
    "1" : "One",
    "2" : "Two",
    "3" : "Three",
    "4" : "Four",
    "5" : "Five",
    "6" : "Six",
    "7" : "Seven",
    "8" : "Eight"
}

words = " "

for zip in zipCode:
    num = digits_maping.get(zip, "Null")
    words = words + num + " "

print(words)



message = input(">")
words = message.split(' ')
emojis = {
    ":)" : "😊",
    ":(" : "🥺"
}



output = " "

for word in words:
    output = output + emojis.get(word, word) + " "

print(output)



# funtions 

# Arbitrary Arguments, *args
# If you do not know how many arguments that will be passed into your function, 
# add a * before the parameter name in the function definition.


def my_function(*student):
    print(f"My student's age is:  {student[5]} and his name is {student[2]}")


my_function("Amy", "Jason", "Robin", "Sarah", 19, 22, 34, 10)




# **kwargs
# add two asterisk: ** before the parameter name in the function
# function will receive a "dictionary" of arguments, and can access the items accordingly

def myCityFuntion(**city):
    print("My state and zipcode is "+ city["state"] + " and " + city["zipCode"])

myCityFuntion(zipCode = "19040", state = "PA", county = "Delaware")   ## figure out





# Lambda funtion -- small, anonymous function
# They can only contain one expression, which is the "return" value of the function
# Syntax -->  lambda arguments: expression 


# adding two numbers

add = lambda a, b: a + b
print(add(8, 2))


multiply = lambda a, b, c: a * b * c
print(multiply(8, 2, 4))



    
