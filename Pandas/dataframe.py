''' Dataframe : it is a two deminsional object that is useful in representing data in the 
                form of rows and columns it s similar to a spreadsheet or a sql table.
               This is the most commanly used pandas object.
columns->     index     |  player_name |IPL team| base price INCR|
               0        |   Rohit      | MI     |    13
               1        |   virat      | rcb    |     17 
               2        |   dhoni      |  csk   |     14
Properties of dataframe:
1.A dataframe has axix row index(axix=0) and cloumn index(axix=1).
2.row index is called index and column index is called column name.
3.A dayaframe contains heterogeneous data
4.A dataframe size is mutable
5.A Dataframe data is mutable
6.A dataframe can be created using any of the following series,lists ,dictionries,numpy 2darrays 
'''
#WAP to create Empty Dataframe
import pandas as pd
df=pd.DataFrame()
print(df)

#WAP to create a Dataframe from series
s=pd.Series(['a','b','c','d'])
df=pd.DataFrame(s)
print(df)

#WAP to create a DataFrame from dictionary of series
name=pd.Series(['Balaji','Niit'])
team=pd.Series(['Civil_Lines','Asuran'])
dic={'Name':name,'Team':team} #these are column name
df=pd.DataFrame(dic)
print(df)

#WAP to create a DataFrame from list od dictionaries
l=[{'Name':'Sushmita' , 'Surname':'Santra'},
   {'Name':'Shreya','Surname':'Singh'}]
df=pd.DataFrame(l)
print(df)

#using iterrow(): it is used to access the data row wise
for(row_index,row_value) in df.iterrows():
    print('\n Row index is:', row_index)
    print('Row value is:' ,row_value)

#iteritems(): it is used to access data column wise.
for (col_name, col_value) in df.iteritems():
    print('\n')
    print('column name')

