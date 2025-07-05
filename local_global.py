num1=10                                                 #Global Variable
print("Global variable num1 : ",num1)
def func(num2):                                       #Num2 is Local Variable
    print("In function - Local variable num2: ",num2)
    num3=30                                             #Num3 is Local Variable
    print("In function Local variable num3 : ",num3)
func(20)                                                   #20 is passed as an argument to the function
print("Num1 again : ",num1)

#print("Num3 outside function : ", num3) = This shows error because it is outside the local variable function

import Module
Module.say_hello()
