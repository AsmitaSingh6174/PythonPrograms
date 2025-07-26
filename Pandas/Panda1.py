                                                #Pandas
'''1. It is a package useful for data Analysis and Data Manipulation .
  2. Pandas provide an easy way to create , Manipulate the data .
  3. Pandas provide powerful and easy to use data structure .
'''
                                               #DataStructure
'''                                Panda Deals with 3 Data structure : - 
    1. Series : Is a 1 Dimensional Array like strucrture with homogeneous DataStructure .
                     Which can be used to Handle and manipulate Data.
                     Series is considered as D.S. of Two Arrays :-
                     
                      INDEX                            |                 DATA
           (Associated index with data)                |         (An Array of Actual Data)
                     (Can't Change)                    |            (Can be Changed)
                         0                                                1
                         1                                                2
                         2                                                3
                         3                                                4
'''

import pandas as pd
a=[10,20,30,40]
myvar=pd.Series(a)
print(myvar)

print(myvar[0])                  #Label

#Create Labels : With the index argument , you can rename your own Label.
myvar=pd.Series(a, index=["w","x","y","z"]) 
print(myvar)
print(myvar["x"])
'''    2. DataFrame : 
    3. Panel
'''
import pandas as pd
print("Hello Pandas")
