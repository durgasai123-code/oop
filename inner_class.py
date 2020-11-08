class Student:
    
    def __init__(self, name, age, section):
        self.name = name
        self.age = age
        self.section = section
        self.lap = self.Laptop()
    
    def show(self):
        print(self.name, self.age, self.section)
        self.lap.show()
        
    class Laptop:
        
        def __init__(self):
            self.brand = "HP"
            self.cpu = "i5"
            self.ram = 8
           
        def show(self):
            print(self.brand, self.cpu, self.ram)
      

s1 = Student("durga", 23, "A")
s1.show()
