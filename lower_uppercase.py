#even odd
#if the no given is leap yr or not

#WAP to enter any character .if the entered character is in lowercasethen convert
#in into uppercase and if it is an uppercase character,then convert it into lowercase...
ch=input("Enter Any Character : \t")
if(ch>='A' and ch<='Z'):
 ch=ch.lower()
 print("The Entered Character in Uppercase,in Lowercase it is:\t"+ch)
else:
 ch=ch.upper()
 print("The Entered Character in lowercase,in Uppercase it is:\t"+ch)

