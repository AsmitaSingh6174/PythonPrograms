                                                                  #Class Method

''' Class methods are little diffrent from ordinary methods :
   1. they are called by a class (not by instence of the class) , and the second of the
   2. first argument of class method is cls , not the self
    class Methods are widely used for factory methods which instantiate an instance of a class using diffrent
    parameter from those usually passed to the class constructor. '''

class Rectangle:
    def __init__(self,length,breath):
        self.length=length
        self.breath=breath
    def area(self):
        return self.length*self.breath
    @classmethod
    def square(cls,side):
        return cls(side,side)
s=Rectangle.square(10)
print("Area = ",s.area())
