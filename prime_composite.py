#WAP to classify is given number is Prime or Composite
n=int(input("Enter a Number : "))
fact=0
if(n>1):
    for i in range(1,n+1,1):
        if(n%i)==0:
            fact=fact+1
    if(fact==2):
        print(n,"Is Prime Number")   
    else:
        print(n,"Is Composite Number ")
else:
 print(n,"Is neither Prime nor Composite")
