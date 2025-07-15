#WAP to calculate the Bank Interest

class Bank():                                         #Abstract class
   def Interest():
        raise NotImplementedError()
   def display_Interest():
         raise NotImplementedError()
class SBI(Bank):
     def Interest(self):
         print("________________SBI BANK___________________")
         self.amount=int(input("Enter Total Amount : "))
         self.rate=int(input("Enter the Rate : "))
         self.time=int(input("Enter the time : "))
     def display(self):
        return(self.amount*self.rate*self.time/100)
class HDFC(Bank):
     def Interest(self):
         print("___________________HDFC BANK_________________")
         self.amount=int(input("Enter Total Amount : "))
         self.rate=int(input("Enter the Rate : "))
         self.time=int(input("Enter the time : "))
     def display(self):
        return(self.amount*self.rate*self.time/100)
s=SBI()
s.Interest()
print(s.display())
h=HDFC()
h.Interest()
print(h.display())


