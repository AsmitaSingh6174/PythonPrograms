#WAP to Display The Content of the file file1.txt using list() method.
file=open("file.txt","r")
for l in file:
    print(l)
file.close()

#WAP to open file using with keyword
with open("file.txt","r") as file:
    for i in file:
        print(i)
print("file is closed : ",file.close())
