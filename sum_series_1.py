#WAP to sum the series ----1+1/2+1/3------+1/n.
n=int(input("enter the value of n"))
s=0
for i in range(1,n+1,1):
    s=s+1.0/i
print("the sum of series=",s)


#WAP to sum the series ----1+1/2^2+1/3^2------+1/n^2.
n=int(input("enter the value of n"))
s=0
for i in range(1,n+1,1):

    #s=s+1.0/(i**2)
    s=s+1.0/(i*i)
print("the sum of series=",s)


#WAP to sum the series ----1/2+2/3+3/4------+n/n+1.
n=int(input("enter the value of n"))
s=0
for i in range(1,n+1,1):
    s=s+i/(i+1)
print("the sum of series=",s)

#WAP to sum the series ----1^1/1+2^2/2+3^3/3------+n^n/n.
n=int(input("enter the value of n"))
s=0
for i in range(1,n+1,1):

    s=s+(i**i)/i
    
print("the sum of series=",s)

#WAP to sum the series ----1^3+2^3+3^3------+n^3.
n=int(input("enter the value of n"))
s=0
for i in range(1,n+1,1):

    s=s+(i**3)
    
print("the sum of series=",s)




