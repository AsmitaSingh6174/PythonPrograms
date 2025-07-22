#WAP to split the line into a series of the words and use space to perform the split operation.
with open("file.txt","r") as file:
    line = file.readline()
    word = line.split()
    print("Line : ",line)
    print("Words : ",word)

'''WAP to split the line into a series of the words and use (.) to perform the split operation.'''
with open("file.txt","r") as file:
    line = file.readline()
    word = line.split('.')
    print("Line : ",line)
    print("Words : ",word)
    print("File Number : ",file.fileno())
    print("File buffer : ",file.flush())
    print("Read line",file.readline(2))

#isatty()
file=open("file.txt","w")
file.write("Hello")
print(file.isatty())


