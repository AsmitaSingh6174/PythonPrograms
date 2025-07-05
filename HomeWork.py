 #WAP USing while loop to read the number until -1 is incountered also the count the
#number of prime no and composite no.entered by the user

'''n=int(input("Enter a number : "))
prime=0
comp=0
while(n != -1):
   print(n)
  if(n==-1):
      break
  if(n<=1):
      continue
  count=0'''
num=int(input(""))
  
    

##WAP to calculate pow(x,n)
x=int(input("Enter Base : "))
n=int(input("Enter exponent : "))
#i=0
#res=1
#while(i<n):
# res=res*x
# i=i+1
res=x**n
print(x,"Raised to the power",n,"=",res)
print("\n")

###WAP that display all leap years from 1900 to 2101years.
print("Leap years from 1900 to 2101:")
for year in range(1900, 2102):
    if ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
        print(year)
       #print(i,end='')
print("\n")

####WAP to sum the series -----1+1/2+......+1/n
n=int(input("Enter a Number : "))
total=0
for i in range(1,n+1):
 total= total + 1/i
print("Sum of the series 1+1/2+......+1/",n,"=",total)
print("\n")

#####1/1^2+1/2^2+1/3^2+........1/n^2
n=int(input("Enter the value of n : "))
sum=0
i=1
while(i<=n):
    sum=sum+1/(i*i)
    i=i+1
print("Sum of the series 1/1^2+1/2^2+1/3^2+........1/",n,"^2 =",sum)
print("\n")

######1/2+2/3+........+n/(n+1)
n=int(input("Enter the value of n : "))
sum=0
i=1
while(i<=n):
    sum=sum+i/(i+1)
    i=i+1
print("Sum of the series 1/2+2/3+........+",n,"/(",n,"+1) =",sum)
