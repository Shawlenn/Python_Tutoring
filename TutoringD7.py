import MyModule

# OPP - Inheritance 
# Parent Class -- Class being inharited from
# Child class --- class that inherits from another class 

# Parent Class 
class Cities:

    def __init__(self, name, population):
        self.name = name
        self.population = population


    def printCityname(abc):
        print(abc.name, abc.population)



# parent Class objects
CityNames = [               # List[] of cities
    Cities("Philly", 12000), 
    Cities("Media", 6000), 
    Cities("Allentown", 4000) 
]  


# Print city names and populationa from the list 
for city in CityNames:
    city.printCityname()



# Child Class 

class Township(Cities):


    def __init__(self, name, population, fname, lname):
        super().__init__(name, population)
        self.fname = fname
        self.lname = lname 


# child class objecrs 
x = Township("Egg harbor", 2000, "Serena" , "Williams")
x.printCityname()
print(x.fname, x.lname)


# Module

MyModule.greeting("Amy")

graduationY = MyModule.students["gradYrr"]
print(graduationY)



# try & except -- Eroor Handling 

try:
    print(age)
except:
    print("An exception occured.")
else: 
    print("Nothing went wrong")
finally:
    print("will be executed regardless.")

# Since the try block raises an error, the except block will be executed


# file handling
# Open() funtion --- take "filename", "mode"
# mode: r, w, a, c

# open a file for writing 
file = open("myFile.txt", "w")
file.write("First Text")




# Problem from last class

def myCityFunction(state, county, zipcodes):
    # Print the state
    print("My state is " + state)
    
    # Print the second zipcode from the list
    print("The second zipcode is " + zipcodes[1])


# Call the function
myCityFunction(
    state="PA",
    county="Delaware",
    zipcodes=["19040", "19111", "19116"]
)





