#slicing is a way to retrieve subsets of the data from pandas object 
#syntax:series_name[start:end:step]
import pandas as pd
import numpy as np
arr=np.array ([10,15,20,25,30])
s=pd.Series(arr,index=['A','B','C','D','E'])
print(s)
print(s[1:5:2])
print(s[0:5:2])

