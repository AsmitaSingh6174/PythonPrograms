'''The return statement is used for two things :-'''
#1. Return a value to the caller.
#2. To end an exit a function and go back to its caller.
'''notes:- A funtion may or may not return a value.'''
#3. Ex:- Calculator program (Div)

def display():
    print("In function")
    print("About to execute return statement ")
    return                                  #return to the display function
    print("This line will never be displayed")
display()
print("Back to the caller")

 
