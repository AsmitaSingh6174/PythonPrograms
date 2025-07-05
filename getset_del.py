#WAP to demostrate the use of getattr(),setattr() and delattr() function .

class ABC():
    def __init__(self,var):
        self.var1=var
    def display(self):
        print("var1 = ",self.var1)
obj=ABC(10)
obj.display()
print("Check if the object has attribute var1 ..... ",hasattr(obj,'var1'))
print(getattr(obj,'var1'))
setattr(obj,'var1',50)
print("After setting value, var1 is : ",obj.var1)
setattr(obj,'Mew',4)
print("New Variable Mew is Created and its value is : ",obj.Mew)

