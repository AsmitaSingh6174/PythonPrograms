'''WAP to with class bill. the user have the option to pay the bill either by check or by cash. use the inheritance
   to model this situation.'''
class Bill():                                                                          #Base Class
    def __init__(self,item,price):
        self.total=0;
        self.item=item
        self.price=price
        for i in self.price:
            self.total=+i
    def display(self):
        print("\n ITEM \t\t\t PRICE") 
        for i in range(len(self.item)):
            print(self.item[i],"\t\t\t",self.price[i])
        print("_____________________________")
        print("Total = ",self.total)
class cash_payment(Bill):                                                 #Child Class
    def __init__(self,item,price,demo,value):
        Bill.__init(self,item,price)
        self.deno=deno
        self.value=value
    def cash_payment_details(self):
        Bill.display(self)
        for i in range(len(deno)):
            print(deno[i],"*",value[i],"=",deno[i]*value[i])
class cheque_payment(Bill):                                             #Child Class
    def __init__(self,item,price,cno,name):
        Bill.__init__(self,item,price)
        self.cno=cno
        self.name=name
    def cheque_payment_details(self):
        Bill.display(self)
        print("Check Number : ",self.cno)
        print("Bank name : ",self.name)
item=["External Hard disk","RAM","Printer","Pen Drive"]
price=[5000,2000,6000,800]
option=int(input("Would you like to pay by cheque or Cash (1/2) : "))
if(option==1):
    name=input("Enter the name of the Bank : ")
    cno=input("Enter the cheque number : ")
    cheque=cheque_payment(item,price,cno,name)
    cheque.cheque_payment_details()
else:
    deno=[10,20,50,100,500,2000]
    value=[1,1,1,20,4,5]
    cp=cash_payment(item,price,deno,value)
    cp.cash_payment_details()



            
