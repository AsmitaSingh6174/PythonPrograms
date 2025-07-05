''' WAP to print the Pattern:
        12345
        12345
        12345
        12345                 '''
for i in range(1,5):
   for j in range(1,6):
     print(j,end='')
   print()
print("\n")

''' WAP to print the Pattern:
        *****
        *****
        *****
        *****                 '''
for i in range(1,5):
   for j in range(1,6):
     print("*",end='')
   print()
print("\n")


''' WAP to print the Pattern:
        1
        12
        123
        1234
        12345                 '''
for i in range(1,6):
   for j in range(1,i+1):
     print(j,end='')
   print()
print("\n")


''' WAP to print the Pattern:
        *
        **
        ***
        ****
        *****                 '''
for i in range(1,6):
   for j in range(1,i+1):
     print("*",end='')
   print()
print("\n")


'''WAP to print the Pattern:
        1
        22
        333
        4444
        55555                  '''
for i in range(1,6):
   for j in range(1,i+1):
     print(i,end='')
   print()
print("\n")


'''WAP to print the Pattern:
        11111
        22222
        33333
        44444
        55555                  '''
for i in range(1,6):
   for j in range(1,7):
     print(i,end='')
   print()
print("\n")


'''WAP to print the Pattern:
        0
        12
        345
        6789                  '''
n=0
for i in range(1,5):
    for j in range(1,i+1):
        print(n,end='')
        n = n+1
    print()
print("\n")
      

'''WAP to print the Pattern:
        5
        54
        543
        5432
        54321                '''
for i in range(5,0,-1):                  #for i in range (1,6,1)
    for j in range(5,i-1,-1):            #for j in range(5,5-i,-1)
        print(j,end='')
    print()
print("\n")

'''WAP to print the Pattern:
             1
          1 2
       1 2 3
    1 2 3 4
 1 2 3 4 5                '''

for i in range(1,6,1):
   for k in range(i,5,1):
        print(" ",end=" ")
   for j in range(1,i+1,1):             
     print(j,end='')
   print()
print("\n")

''' WAP to print the Pattern:
            *
           **
          ***
         ****
        *****                             '''
for i in range(1,6,1):
   for k in range(i,5,1):
        print(" ",end=" ")
   for j in range(1,i+1,1):             
     print("*",end=' ')
   print()
print("\n")


''' WAP to print the Pattern:
            *****
            ****
            ***
            **
            *                             '''
for i in range(5,0,-1):
   for j in range(i):             
     print("*",end=' ')
   print()
print("\n")

''' WAP to print the Pattern:
          5
       45
     345
   2345
12345                               '''
for i in range(5,0,-1):
   for k in range(1,i):
        print(" ",end=" ")
   for j in range(i,6):             
     print(j,end='')
   print()
print("\n")
''' WAP to print the Pattern:
            12345
              1234
                123
                  12
                    1                     '''

''' WAP to print the Pattern:
            5
          44
        333
      2222
    11111                             '''


