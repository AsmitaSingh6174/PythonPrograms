                                                                 #Public and Private Variables
''' A public variables are those variables that are defined in the class and can be accessed from
   anywhere in the program . on the other hand private variables are those variables that are defined in the class
   with the double score prefix . These variables can be accessed only from within the class and from nowhere
   outside the class. '''
#WAP to illustrate the diffrence between public and private variables.
class ABC():
    def __init__(self,var1,var2):
        self.objvar1=var1                    #Public Variable
        self.__objvar2=var2              #Private Variable
    def display(self):
        print("From class method , objvar1 ",self.objvar1)
        print("From class method , objvar2 ",self.__objvar2)
    def __display(self):
        print("From the class private method objvar2=",self.__objvar2)
obj=ABC(10,30)
obj.display()
print("From main module , objvar1 ",obj.objvar1)
print("From main module , objvar2 ",obj._ABC__objvar2)
obj._ABC__display()
