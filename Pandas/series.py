#Creating a Series from a Dictionary

import pandas as pd
d={'Name':'Virat','Team':'RCB','Run':120}        #Creating a Dictionary
s=pd.Series(d)                                   #Create a Series
print(s)

#Mathematical Operators in Series
import pandas as pd
s=pd.Series([1,2,3,4,5])
print("To Multiply all the values in series by 2")
print("___________________________________________")
print(s*2)
print("To Find the square of all Values")
print("___________________________________________")
print(s**2)
print("To Multiply all the values in series that are greater than 2")
print("______________________________________________________________")
print(s[s>2])




