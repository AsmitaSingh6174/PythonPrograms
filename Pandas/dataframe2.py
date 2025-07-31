#Select Operation in data frame to access the column data , we can mention the column name as subscript
import pandas as pd 
empdata={'empid':[101,102,103,104,105],
         'empname':['Asmita','Sushmita','Shreya','Apoorva','Riyanshi'],
         'Doj':['10-03-2026','20-03-2026','21-03-2026','30-12-2027','20-12-2027']}
df=pd.DataFrame(empdata)
print(df)
print("___________________Employee Names________________________")
print(df.empname)

#To add & rename a column in Dataframe
s=pd.Series([10,15,23,30,35])
df=pd.DataFrame(s)
print(df)
df.columns=['List1']
print(df)
df['List2']=20    #TO Create a new Column list 2 with all values as 20
print(df)
df['List3']=df['List2']+df['List1']
