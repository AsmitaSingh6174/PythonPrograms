'''                                class DerivedClass(BaseClass):
                                       body_of_DerivedClass                        '''
#Parent/Base  Class
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("Name : ",self.name)
        print("Age : ",self.age)
#Child/Derived Class
class Teacher(Person):
    def __init__(self,name,age,exp,r_area):
        Person.__init__(self,name,age)
        self.exp=exp
        self.r_area=r_area
    def displayData(self):
        Person.display(self)
        print("Experience : ",self.exp)
        print("Research area : ",self.r_area)
#Child/derived class
class student(Person):
    def __init__(self,name,age,course,marks):
        Person.__init__(self,name,age)
        self.course=course
        self.marks=marks
    def displayData(self):
        Person.display(self)
        print("Course : ",self.course)
        print("Marks : ",self.marks)

print("____________TEACHER________________")
t=Teacher("Om Sir",40,"M.tech","Data Science")
t.displayData()
print("____________STUDENT________________")
s=student("Asmita",20,"BCA","7.5")
s.displayData()
