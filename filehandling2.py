#WAP to write to a file using the Written() method . 
file=open("file.txt ","w")
lines=["This is for multiple lines \n",
       "This is for multiple lines \n ",
       "This is for multiple lines "]
file.writelines(lines)  #fileobj.writes(string)
file.close()
print("Data written into file") 









