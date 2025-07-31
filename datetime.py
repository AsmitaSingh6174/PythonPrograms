#Return current date and time
import datetime as dt 
x=dt.datetime.now()
print(x)

#Return year and name of week day
print(x.year)
print(x.strftime("%A"))
print(x.strftime("%a"))
print(x.strftime("%w")) #weekday as a decimal number,where 0 is sunday and saturday is 6
print(x.strftime("%d")) #days of the months 
print(x.strftime("%B"))
print(x.strftime("%b"))
print(x.strftime("%m"))#month as a decimal number
print(x.strftime("%H"))
print(x.strftime("%h"))
print(x.strftime("%p"))
print(x.strftime("%M"))
print(x.strftime("%S"))


#Create Date objects
y=dt.datetime(2025,7,26)   #Date
print(y)
