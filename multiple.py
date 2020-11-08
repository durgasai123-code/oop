# inheritence: it is process of deriving another class from main class.
"""
main class is called super class and another class is called sub class.
there are two types of inheritence.
1.multilevel: deriving one to two and two to three.
2.multiple: derving one class from two main classes.
method resolution order(mro): which means if you have derived c class from a, b. it first prints left hand side data first.
we can also print methods of super class by using super()

"""
# multiple

class Human:
    
    def __init__(self):
        print("update1")
    
    def feat1(self):
        print("update2")
        
class Human2():
    
    def __init__(self):
        super().__init__()
        print("update3")
        
    def feat2(self):
        print("update4")
        
class Human3(Human, Human2):
    
    def __init__(self):
        """
        initily if __init__() not there in sub class, if we call subclass it points to super class init(). 
        if sub class __init__() it prints their own. in this case if you want to print super class init() we use special function
        named as super(). it is also used to print methods in ned function.
        Here super() follows one special thing is method resolution order(MRO) means it gives priority to the left side data.
        """
        super().__init__()
        print("update5")
        
    def feat3(self):
        print("update6")
        
    def feat4(self):
        super().feat2()
        
a2 = Human3()
a2.feat4()
