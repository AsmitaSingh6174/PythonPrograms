                                                                  #Multiple Inheritance
''' When a Derived class inherits features from more than one base class it is called multiple inheritance . 
                                                                   class Base1:
                                                                       Statement block
                                                                   class Base2:
                                                                        Statement block
                                                                   class Derived(Base1,Base2)
                                                                         Statement block                 '''

class Asmi():                                                        #First Base Class (Father)
    def __init__(self):
        super(Asmi,self).__init__()
        print("Asmita ka home")
class Sush():                                                         #Second Base Class (Mother)
    def __init__(self):
        super(Sush,self).__init__()
        print("Sushmita ka home")
class Shreya(Asmi,Sush):                                   #Derived class (Child)
    def __init__(self):
        super(Shreya,self).__init__()
        print("Shreya ka Home")
c=Shreya()
