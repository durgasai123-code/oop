# here we creating class name as Human
class Human:
    # here we declering __init__ fun to give instructions
    # self is reference variable to refrence the object
    # name, age, color are attributes
    def __init__(self, name, age, color):
        # self is used to link attributes with class
        self.name = name
        self.age = age
        self.color = color
    
    # details is the method which means action   
    # self is mandatory to refer the object
    def details(self):
        print("my name is:",self.name)
        print("my age is:",self.age)
        print("my color is:",self.color)

# we create object named as a
a = Human("durga", 23, "white")
a.details()
print(a.name)
