class Human:
    
    # here self is required variable
    # assignment also like below:
    # if you not give any arguments in constructor, dnt give any argument data at the time of object creation like c1 = Human("durga", 23), it gives error
    # the assignment must like shown in below
    """ 
    def __init__(self):
        self.name = "durga"
        self. age = 23
    """
    
    def __init__(self, name, age):
        self.name = name
        self. age = age
        
    def update(self):
        self.age = 25
        
    def compare(self, other):
        if self.age == other.age and self.name == other.name:
            return True
        else:
            return False

c1 = Human("durga", 23)

c2 = Human("huu", 22)
print("my name is:",c1.name, "and age is:", c1.age)
print("my name is:",c2.name, "and age is:", c2.age)
c1.update()
print("my name is:",c1.name, "and age is:", c1.age)
print("my name is:",c2.name, "and age is:", c2.age)
if c1.compare(c2):
    print("same")
else:
    print("not same")
    
