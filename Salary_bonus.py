'''A company decide to give bonus to all it empolyes om diwali. A 5% bonus on salary is
give to the male workers and the 10% to the female workers.WAP to enter the salary of the
employee and gender of the employee.If the salary of the employee is less than 100/-
then the employee gets an extra 2% on salary. Calculate the bonus that has to give the empolyee
and display the salary that the employee will get.'''

ch=input("Enter the Gender of the Employee (M or F):\t")
salary=float(input("Enter the Salary of the Employee:\t"))
if(ch=='m'):
  bonus=.05*salary
else:
  bonus=.10*salary
if(salary<10000):
  extra_bonus=.02*salary
  print("Extra Bonus:\t",extra_bonus)
else:
  extra_bonus=0
  print("Extra Bonus:\t",extra_bonus)
amt_tobe_paid = salary+bonus+extra_bonus
print("______________________________________________\n")
print("Amount to be paid",amt_tobe_paid)

