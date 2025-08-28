import numpy as np 


# Arrays  -- import NumPy library -- stand for: Numerical Python
# Arrays -- faster than lists[]

xarr = np.array([1, 6, 4, 3, 10, 15])

print(xarr)
print(type(xarr))
print(xarr[1])
print(xarr[1] + xarr[5])


# 2D - Array 
yarr = np.array([[1, 2, 3, 4, 5], [-1, -2, -3, -4, -5]])
print("The third element from this array is: ", yarr[0,2], yarr[1, 2])


# 3D Array

zarr = np.array([[[20, 30, 40], [15, 25, 35]],  [[120, 130, 140], [115, 125, 135]]])
print(zarr[1, 0, 0])



# OPP --- Object-Oriented Programming 

# Classes and Objects 
# Class -->  defines what an object should look like and Obj --> created based on that class
# class can be "fruits", and objects can be (Apple, Pear, Peach)


# We use "Classes" to define new type, these types can have different methods and attributes


class Cars:

    # Constructor
    def __init__(self, a, b):
        self.a = a # initializing obj
        self.b = b



    def move():
        print("move the car")

    def draw():
        print("draw the car")



""" 
car1 = Cars() # obj
car1.x = 10 # attributes
car1.y = 20
print(car1.x)
# car1.draw()  # figure out


car2 = Cars()
# print(car2.x) 
car2.z = 30
print(car2.z)
"""



# Constructors -- There's a way to print x,y without giving it attributes,
#  with the help of Constructors

myCar = Cars(10, 20)
print(myCar.b)
myCar.a = 5
print(myCar.a)


# exercise:  create a class type name weather
# weather should have "type" attribute 
# and "clothing" method

class Weather:
    def __init__(self, temp):
        self.temp = temp


    def clothing(self):
        print(f"Wear short-sleeves today. its {self.temp} outside")


summer = Weather("89 degrees")
winter = Weather("12 degree")
summer.clothing()
winter.clothing()
