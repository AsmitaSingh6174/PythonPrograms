#Program To Make a Simple Calculator

import math
print("\t______________________|| Calculator ||__________________________")
def sum(a,b):
   a+=b
    return a

def sub(a,b):
  if a>b:
    a-=b
    return a
  else:
     b-=a
     return b
    
def multi(a,b):
    a*=b
    return a

def div(a,b):
    if a>b:
        q=a/b
        r=a%b
    else:
        q=b/a
        r=b%a
    
    print("\n The Quotient is : ",q)
    print("\n The Remainder is : ",r)

def sqr(a):
    x=math.sqrt(a)
    return x
while(True):
    print("\n\n Choose the Operation You Want To Perform")
    print("\n\t 1. Addition")
    print("\n\t 2. Subtraction (Absolute Difference)")
    print("\n\t 3. Multiplication")
    print("\n\t 4. Division (Quotient & Remainder)")
    print("\n\t 5. Square Root")
    print("\n\t 6. Exit")

    choice = int(input("Enter your choice (1-6): "))
     
    if choice ==1:
        print("\n \n Enter two number:")
        num1=int(input("Enter first number"))
        num2=int(input("Enter second number"))
        s=sum(num1,num2)
        print("The sum is:",s)
    elif choice==2:
        print("\n \n Enter two number:")
        num1=int(input("Enter first number"))
        num2=int(input("Enter second number"))
        s=sub(num1,num2)
        print("The sub is:",s)
    elif choice==3:
        print("\n \n Enter two number:")
        num1=int(input("Enter first number"))
        num2=int(input("Enter second number"))
        s=mul(num1,num2)
        print("The multiply is:",s)
    elif choice==4:
        print("\n \n Enter two number:")
        num1=int(input("Enter first number"))
        num2=int(input("Enter second number"))
        s=div(num1,num2)
        print("The division is:",s)
    elif choice==5:
        num1=int(input("\n \n Enter a number:"))
        s=sqr(num1)
        print("The square root is:",s)
    else:
        print("\n you choose to exit")
        break
    
