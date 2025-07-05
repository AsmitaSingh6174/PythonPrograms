'''A recursive function is defined as a function that calls itself to solve a smaller version of it's Task. Until a
Final call is met which does not require a call to itself.'''

def fact(n):
    if(n==1 or n==0):
        return 1
    else:
        return n*fact(n-1)
n=int(input("Enter the value of a : "))
print("The factorial of ",n,"is",fact(n))
