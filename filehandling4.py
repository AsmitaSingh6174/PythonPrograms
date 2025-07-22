#WAP a program that copies firsr 10 bytes
with open("file1.txt", "rb") as file: 
    with open("file2.txt", "wb") as file3: 
        buf =file.read(5) 
        file3.write(buf)
print("File Copied")
''' Write a program that copies one Python script into another in such a way that all 
    comment lines are skipped and not copied in the destination file.
'''
with open("First.py", "rb") as file1: 
    with open("Second.py", "wb") as file2:
        while True: 
            buf = file1.readline() 
            if len(buf)!=0: 
                if buf[0]=='#': 
                    continue 
                else: 
                    file2.write(buf)
            else:
                 break
print("File Copied")

