class Employe:
    
    def __init__(self):
        print("employe created")
        
    """
     __del__ means destroctor, The destructor was called after the program ended or when all the references to object are deleted 
    i.e when the reference count becomes zero, not when object went out of scope.
    """
    
    def __del__(self):
        print("destroctor called")
        
def object_call():
    print("making object")
    objj = Employe()
    print("function end")
    return objj
    
obj = object_call()
print("program end")
