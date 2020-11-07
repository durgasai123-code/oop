# here object address stored in heap memory of a computer
# evrey time u run the code the address changed to new None
# sizwe of object depends upon no of variables we have
# but who responsible to caliculate and assign that memory
# constrctor is responsible for that.
# self is reference variable it refers the object
class heap:
    pass

c1 = heap()
c2 = heap()
print(id(c1))
print(id(c2))
