'''WAP To check a No. if it is Leap year or not'''
num=int(input("Enter a YEAR :\t"))
if((num%4==0 and num%100==0) or (num%400==0)):
    print(num,"Is a Leap Year")
else:
    print(num,"Is not a Leap Year")
