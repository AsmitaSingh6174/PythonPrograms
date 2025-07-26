                            #Selecton in Series
'''    Series provides index label loc and ilocand[]to access Rows and columns .
       loc index label : series_name.loc[Start range : Stop range]                 '''
import pandas as pd
import numpy as np
arr=np.array([10,20,30,35,40,50,65,89,90])
s=pd.Series(arr)
print(s)
print(s.loc[:2])              # print from starting till the given index
print(s.loc[2:])              # print all the values after the given index
print(s.loc[3:6])             # print Values between the given index
print(s.loc[3])               # print the particular given index