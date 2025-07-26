#Mathematical Operators in Series To Add 2 Series
import pandas as pd
s1=pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])
s2=pd.Series([10,20,30,40,50],index=['a','b','c','d','e'])
s3=pd.Series([4,27,32,50],index=['a','b','c','d'])
print("To Add Series1 and Series2")
print("___________________________________________")
print(s1+s2)
print("To Add Series1 and Series3")
print("___________________________________________")
print(s1+s3)
print("To Add Series2 and Series3 and filled non matching index with 0")
print("___________________________________________")
print(s2.add(s3,fill_value=0))
