#WAP to demonstrate name clash of the local and global variable
var="Morning"                                          #Global Variable
def show():
    var="Good"                                           #Local Variable
    print("In function var is : ",var)
show()
var="Evening"
print("Outside the function var is : ",var)
