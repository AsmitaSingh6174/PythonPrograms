                                   #Types of Files : 
'''1. ASCII Text Files
   2. Binary Files
1) Open File  : file obj = open(File_name[,access_mode])
      example : file = open("File.txt","")
2) Close File : print(file.close())  '''
#Ques : Write a Program to open a File and Print its attribute values . 
file=open("file.txt","w")
print("Name of the File ", file.name)
print("File is Closed.", file.closed)
print("File has opened in ", file.mode,"mode")

#WAP to Access a file after it is closed .
file=open("file.txt ","w+") 
print("Name of the File ", file.name)
print("File is Closed.", file.closed)
print("File has opened in ", file.mode,"mode")
print("File is now being closed.", file.close())

#WAP that writes a message in the file.txt .
file=open("file.txt ","w")
file.write("Hey Everyone hope so it is easy for you to understand this program !!")  #fileobj.writes(string)
file.close()
print("Data written into file")  # write() returns none


