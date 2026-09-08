import pandas as pd
df=pd.read_csv('FastFoodRestaurants.csv', delimiter=',')
print(df)

print('df-data type:', df.dtypes)
print('df.info():', df.info())

print('first three row')
print(df.head(4))

print('last three row')
print(df.tail(4))

print('summarize the rows and column by using describe:', df.describe())
print('rows and column shape:', df.shape)

address=df['address']
print('access one column: df:')
print(df)
print()

address_city=df[['address','city']]
print('access multiple column:df:')
print(address_city)
print()


second_row=df.loc[1]
print('access on row:df:')
print(second_row)
print()

second_row1=df.loc[[1,3]]
print('access multiple row:')
print(second_row1)
print()

second_row2=df.loc[1:5]
print('slice the row')
print(second_row2)
print()

second_row3=df.loc[:1,'city']
print('access one index in column city')
print(second_row3)
print()

second_row4=df.loc[:1, 'city']
print('access index one and 3 in city:')
print(second_row4)
print()

second_row5=df.loc[1:5, ['city', 'country']]
print('selecying a multiple column')
print(second_row5)
print()

second_row6=df.loc[2:4, 'city': 'longitude']
print('slice the column:')
print(second_row6)
print()

print('case 2: using .loc with index_col-start here')
df_index_col=pd.read_csv('FastFoodRestaurants.csv', delimiter=',')
print(df_index_col)
print('data-type:', df.dtypes)
print('data-info:', df.info())
print()

second_row= df.loc[450]
print('selecting a single row')
print(second_row)
print()

second_row1=df.loc[[550,850]]
print('selecting a mutiple row')
print(second_row1)
print()

second_row2=df.loc[1:960]
print('slice a row:')
print(second_row2)
print()

second_row3=df.loc[:15, 'country']
print('selecting a single column')
print(second_row3)
print()

second_row3=df.loc[:20, ['city', 'country']]
print('selecting a multiple column')
print(second_row3)
print()

second_row4=df.loc[1:30, 'city': 'websites']
print('selecting a slice:')
print(second_row4)
print()

print('case3 using .iloc-start here')


second_row=df_index_col.iloc[0]
print('select a single row')
print(second_row)
print()

second_row1=df_index_col.iloc[[0,3,5]]
print('selecg a multiple row')
print(second_row1)
print()

second_row2=df_index_col.iloc[1:8]
print('selecting a slice row')
print(second_row2)
print()
 
second_row3=df_index_col.iloc[:6, 1]
print('selecting a single column:')
print(second_row3)
print()

second_row4=df_index_col.iloc[0:9, [1,5]]
print('selecting a multiple column')
print(second_row4)
print()

second_row5=df_index_col.iloc[0:5, 1:9]
print('selecting a slice column')
print(second_row5)
print()

print("Next Run")

df.loc[len(df.index)]=[12,48,867,12,45,'pakistan',567,987,234,'ali zain']
print('Modified datframe add a new row')
print(df)
print()


df.drop(1, axis=0, inplace=True)
df.drop(index=2, inplace=True)

df.drop([10,55], axis=0, inplace=True)

print('modified dataframe .remove row')
print(df)

df.drop('city', axis=1, inplace=True)
df.drop(columns='country', inplace=True)
df.drop(['province', 'name'], axis=1, inplace=True)
print('select a column delete:')
print(df)


df.rename(columns={'city_nameChanged': 'city_nameChanged'}, inplace=True)

df.rename(mapper={'city':'city_changed', 'country':'country_changed'}, axis=1, inplace=True)
print(' change the name')
print(df)


df.rename(index={0:4}, inplace=True)
df.rename(mapper={1:3, 6:9}, axis=0, inplace=True)
print('column change')
print(df)



print(df.columns.tolist())

selected_row=df.query('address == "324 Main St"')
print(selected_row.to_string())
print(len(selected_row))

selected_row1=df.query('keys == "us/nmay/ssena/324mainst/-1161002137"')
print(second_row1.to_string())
print(len(selected_row1))

selected_row2=df.query('latitude == "44.9213"')
print(second_row2.to_string())
print(len(selected_row2))


selected_row4=df.query('postalCode == "44.9213"')
print(selected_row4.to_string())
print(len(selected_row4))

grouped_by=df.groupby('keys')['longitude'].sum()
print(grouped_by.to_string)
print("grouped:", len(grouped_by))

df_cleaned=df.dropna()
print('cleaned-data:', df_cleaned)

data=[1,2,34,6]
array1=pd.array(data)
print(data)


