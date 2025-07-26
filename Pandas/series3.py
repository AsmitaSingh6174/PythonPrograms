#head():It is used to access the first 5 rows of the series.
import pandas as pd
import numpy as np
arr=np.array([10,15,20,35,45,67,89,90])
s=pd.Series(arr)                         #Create a Series from Array
print(s.head())                          #To print first 5 rows (by default)
print(s.head(3))                         #To print first 3 rows
print(s.tail())                          #To print last 5 rows (by default)
print(s.tail(3))                         #To print last 3 rows













