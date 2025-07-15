#Multi-Path/Hybrid Inheritance
'''            Base Class
            ↙                 ↘
   D cl 1                       D cl 2
         \                           ↗
             Derived Class'''    

class student:                                                          #base class
    def name(self):                                              
        print('Name...')
class Academic_Performance(student):                   #(Father)
    def acad_score(self):
        print("Academic score----90% and above")
        self.name()
class ECA(student):                                                 #(Mother)
    def ECA_score(self):
        print("ECA score----60% and above")
class Result(Academic_Performance,ECA):              #inherited both acad_score and ECA   (child)
    def Eligibility(self):
        print("*Minimum Eligibility to apply")
        self.acad_score()                    #call its method
        self.ECA_score()                     #call its method
R=Result()                                     #diamond problem
R.Eligibility()
