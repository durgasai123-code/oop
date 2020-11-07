# here object address stored in heap memory of a computer
# evrey time u run the code the address changed to new None
# sizwe of object depends upon no of variables we have
# but who responsible to caliculate and assign that memory
# constrctor is responsible for that.
# Constructors are generally used for instantiating an object.The task of constructors is to initialize(assign values) to the data members of the class when an object of class is created.
# In Python the __init__() method is called the constructor and is always called when an object is created.
# self is reference variable it refers the object
class heap:
    pass

c1 = heap()
c2 = heap()
print(id(c1))
print(id(c2))
