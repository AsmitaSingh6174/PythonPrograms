#WAP using For Loop to Calculate the Average of first n natural number.
num=int(input("Enter A Number: \t"))
total = 0
for i in range (1,num+1):
 total = total + i
 avg = int(total/num)
print("The Sum of all Numbers : \t",total)
print("The average of natural numbers : \t",avg)

