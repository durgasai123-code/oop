# area of square

class Areas:
    
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
        
    def square(self):
        print(self.length*self.length)
            
    def triangle(self):
        self.height = 10
        print(((1/2)*self.length*self.height))
                
    def rectangle(self):
        print(self.length*self.breadth)
                
    def circle(self):
        self.radius = 10
        print(3.142*self.radius*self.radius)
        
        
    def show(self, user):
        self.user = user
        if self.user == 1:
            Areas.square(self)
            
        elif self.user == 2:
            Areas.triangle(self)
                
        elif self.user == 3:
            Areas.rectangle(self)
                
        elif self.user == 4:
            Areas.circle(self)
                
        else:
            print("invalid")
            
s = Areas(20, 30)
print("1.square")
print("2.triangle")
print("3.rectangle")
print("4.circle")
s.show(int(input("enter the option:")))

