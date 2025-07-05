import calendar

y = int(input("Enter the year : "))
print("\n\t _____________ Calendar ____________\n")

'''An instance of TextCalendar class is created
calendar.SUNDAY means the week will start from Sunday'''
cal = calendar.TextCalendar(calendar.SUNDAY)

i = 1
while i <= 12:
    '''prmonth() prints the calendar for the given month and year'''
    cal.prmonth(y, i)
    i += 1
