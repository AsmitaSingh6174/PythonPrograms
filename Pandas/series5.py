                                #Selection using[]
'''Syntax : Series_name[Start range : Stop range] or series_name[index]'''
import pandas as pd
import numpy as np
arr=np.array([10,25,15,35,40,55])
s=pd.Series(arr,index=['a','b','c','d','e','f'])
print(s)
print(s[3])
print(s[1:4])
print(s[:4])
print(s.index)

