#Abstract Classes 
'''In oops language it is possible to create a class which cannot be instantiated this means that you cannot create object of that class
such class couldonly be inherited and then an object of the derived class was used to access the features of the base class ,
such a class was known as abstact classes.'''

#program to illustrate the concept of abstract class
class fruit:                                           #object class
    def taste(self):
        raise NotImplementedError()     #in python we use NotImplementedError to restrict the instantiation of the class.
    def rich_in(self):
        raise NotImplementedError()
    def color(self):
        raise NotImplementedError()
class mango(fruit):
    def taste(self):
        return "Sweet"
    def rich_in(self):
        return "Vitamin A"
    def color(self):
        return "Yellow"
class Orange(fruit):
    def taste(self):
        return "Sour"
    def rich_in(self):
        return "Vitamin C"
    def color(self):
        return "Orange"
mango1=mango()
print(mango1.taste(),mango1.rich_in(),mango1.color())
Orange1=Orange()
print(Orange1.taste(),Orange1.rich_in(),Orange1.color())
