#WAP using for loop to print all numbers from m-n, by classifying them as
#even or odd
m=int(input("Enter Begging Number (m) : "))
n=int(input("Enter End Number (n): "))
for i in range(m,n+1):
 if(i%2==0):
   print(i,"is Even")
 else:
   print(i,"in Odd")
