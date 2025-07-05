#Constructor : for storing default value , Garbage value.

''' The _ _init()_ _ method is automatically executed , when an object of a class is created .
    The method is useful to initialize the variables of the class objects. '''

class ABC():
    def __init__(self,var):
        print("In class Method..")
        self.var=var
        print("The value is : ",var)
obj=ABC(10)        

