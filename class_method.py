                                                       #Class Method and Self Argument

''' Class methods must have the first argument named as " self " , you do not pass a value for this parameter
    then you call method. Pyhton provides its value automatically , if you have a method which have no
    arguments then you still have to define the method if you have a method which takes no argumets then
    you still have to define the method to have a self argument. '''

                                                      #Class Variables and Object Variables

''' Class Variables are usually used to keep account of a number of objects created from a class. '''

class ABC():
    class_var=0               #class variable
    def __init__(self,var):
        ABC.class_var+=1
        self.var=var                   #Object Variable
        print("The object value is : ",var)
        print("The value of class variable is : ",ABC.class_var)
obj1=ABC(10)
obj2=ABC(20)
obj3=ABC(30)

#WAP that uses class to store the name and marks of students use list to store the marks in 3 subject.
class students():
    def __init__(self,name):
        self.name=name
        self.marks=[ ]
    def enter_marks(self):
        for i in range(3):
            m=int(input("\n Enter the Marks of %s in subject  %d : "%(self.name,i+1)))
            self.marks.append(m)
    def display(self):
        print(self.name,"Scored",self.marks)
S1=students("Shreya")
S1.enter_marks()
S1.display()
S2=students("Asmita")
S2.enter_marks()
S2.display()
S3=students("Sushmita")
S3.enter_marks()
S3.display()






















