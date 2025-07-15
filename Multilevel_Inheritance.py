                                                                     #Multilevel Inheritance
'''      The Technique of deriving a class from an already derived class is called Multilevel Inheritance.
                      Base Class                            Syntax :   class Base:                   
                            ⬆️                                                     Pass
                    Derived Class 1                                       class Derived 1(Base):
                            ⬆                                                           Pass
                    Derived Class 2                                       class Derived 2(Derived 1):
                                                                                          Pass                                                                                    '''
class Person:
    def name(self):
        print("Name..")
class Teacher(Person):
    def Qualifications(self):
        print("Qualifications.... B.tech Must")
class HOD(Teacher):
    def experience(self):
        print("Experience.... at least 10+ Years")
h=HOD()
h.name()
h.Qualifications()
h.experience()
