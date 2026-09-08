import pandas as pd
df= pd.read_csv('Real_Estate_Sales_2001-2022_GL-Short.csv', delimiter=',')
print(df)
print(' describe rows and column:', df.describe())
print('info rows and column:', df.info())

SerialNumber=df['Serial Number']
print('assess one column')
print(SerialNumber)
print()

SerialNumberListYear=df[['Serial Number', 'List Year']]
print('assess multiple column')
print(SerialNumberListYear)
print()

second_row=df.loc[4]
print('assess only one row')
print(second_row)
print()

second_row1=df.loc[[12,45]]
print('assess multiple row')
print(second_row1)
print()

second_row2=df.loc[12:100]
print('slice row and column')
print(second_row2)

print('assess last 10 row:')
print(df.tail(10))

print('assess first 10 row:')
print(df.head(10))

second_row=df.loc[:, 'Serial Number']
print('select only one column')
print(second_row)
print()

second_row1=df.loc[:, ['Serial Number', 'Location']]
print('select multiple column')
print(second_row1)
print()

second_row2=df.loc[:, 'Serial Number':'Location']
print('slice the column')
print(second_row)
print()

print('index col bu using .iloc')

df_index_col=pd.read_csv('Real_Estate_Sales_2001-2022_GL-Short.csv', delimiter=',')
print(df_index_col)
print('data type:', df.dtypes)
print('infi data type', df.info())
 
second_row=df_index_col.loc[100]
print('single row')
print(second_row)
print()

second_row1=df_index_col.loc[1:140]
print('multiple row')
print(second_row1)
print()

second_row=df_index_col.loc[:, 'Location']
print('single row')
print(second_row)
print()
second_row1=df_index_col.loc[:, ['List Year', 'Location']]
print('multiple column')
print(second_row1)
print()
second_row2=df_index_col.loc[:, 'Serial Number':'Location']
print('slice the column')
print(second_row2)
print()

second_row=df_index_col.iloc[10]
print('single row')
print(second_row)
print()
second_row1=df_index_col.iloc[[12,10]]
print('multiple row')
print(second_row1)
print()

second_row2=df_index_col.iloc[:, 4]
print('single column')
print(second_row2)
print()

second_row3=df_index_col.iloc[:, [1,7]]
print('multiple column')
print(second_row3)
print() 
df.drop(1, axis=0, inplace=True)
df.drop(index=2, inplace=True)
df.drop([8,5], axis=0, inplace=True)
print(df)

df.drop(columns='Serial Number', inplace=True)
df.drop('Location', axis=1,inplace=True)
print(df)

df.rename(columns={'OPM remarks':'OPM remarks changed'}, inplace=True)

df.rename(mapper={'Date Recorded':'Data Recorded Change', 'Town':'Town Changed'}, axis=1, inplace=True)
print(df)

sorted_df=df.sort_values(by='List Year')
print(sorted_df.to_string(index=False))

groupedby=df.groupby('Sale Amount')['Assessed Value'].sum()
print(groupedby.to_string())
print('groupedby', len(groupedby))

data=[1,2,3,4]
array1=pd.array(data)
print(data)