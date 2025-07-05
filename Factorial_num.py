#Wap to calculate Factorial of a Number.
n=int(input("Enter a Number : "))
factorial=1
if(n<=1):
 print("Factorial is not defined or number is negative num")
else:
 for i in range(1,n+1):
  factorial = factorial*i
print("Factorial of",n,"is",factorial)

 
