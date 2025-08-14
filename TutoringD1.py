

print("Hello World!" * 3)    # this is to print something 3 times
print(10-13)



age = 18   # variable type: int
name = "Jason"   # variable type: str
weight = 189     # variable type: int

print("name", "age", "weight")


# Calling all the variable
print(f"{name} is my friend, and he is {age} old, and he is {weight} pounds.")


student = 10 
did_pass = 7
enrolling_again = True   # boolean - true/false 


student_failed = (student - did_pass)
print(student_failed)

print(student, did_pass)
print(f"The studentn failed: {student_failed} perosn.")
print(f"Are they enrolling in the course again: {enrolling_again}")



# Global variable

# Ex -- Create a variable inside a function, with the same name as the global variable

x = "awsome"   # global v

def myfun():
  x = "fantastic"
  print(f"Python is {x}") # local v

myfun() 

print(x)


# using length() function 

country = "Iceland"
the_length = len(country)
character_index = country[4]
neg_character_index = country[-4]


print(the_length)
print(character_index)
print(neg_character_index)

print(country[0:6])
print(country[0:])
print(country[:5])
print(country[:])



# more useful Str methods 

course = "the economics"

print(course.upper())
print(course.lower())
print(course.title())
print(course.find("mi"))
print(course.replace("o", "k")) 
print("the" in course)  # boolean

# find out 
print("book" not in course)





    











