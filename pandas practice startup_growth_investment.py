import pandas as pd

df=pd.read_csv('startup_growth_investment_data.csv', delimiter=',')
print(df)

print('all rows and columns describe:', df.describe())
print('rows and columns info:', df.info())

print('first 10 row')
print(df.head(10))
print()

print('Last 10 row')
print(df.tail(10))
print()

StartName= df['Startup Name']
print(' assess one column:')
print(StartName)
print()

IndustryFundingRounds=df[['Industry', 'Funding Rounds']]
print('assess multiple column:')
print(IndustryFundingRounds)
print()

second_row=df.loc[4000]
print('assess one row:')
print(second_row)
print()

second_row1=df.loc[[12,4500]]
print('multiple rows')
print(second_row1)
print()

second_row3=df.loc[24:4999]
print('slice the rows and column:')
print(second_row3)
print()

second_row=df.loc[:3500, 'Country']
print('assess one column')
print(second_row)
print()  

second_row1=df.loc[:4999, ['Funding Rounds', 'Year Founded']]
print('assess multiple column:')
print(second_row1)
print(second_row1)

second_row2=df.loc[:6, 'Startup Name':'Funding Rounds']
print('slice the column:')
print(second_row2)
print()

print('.loc use with df index col')

df_index_col=pd.read_csv('startup_growth_investment_data.csv', delimiter=',')
print(df_index_col)
print('data-type:', df.dtypes)
print('data-info:', df.info)
print()

second_row=df_index_col.loc[3500]
print('select a single row')
print(second_row)
print()

second_row1=df_index_col.loc[[3200, 2012]]
print('select a multiple row')
print(second_row1)
print()

second_row2=df_index_col.loc[12:4500]
print('slice a row')
print(second_row2)
print()

second_row=df_index_col.loc[12, 'Industry']
print('single column')
print(second_row)
print()  

second_row1=df_index_col.loc[:, ['Startup Name', 'Industry']]
print('multiple column')
print(second_row1)
print()

second_row2=df_index_col.loc[:, 'Startup Name':'Country']
print('slice a column')
print(second_row2)
print()

print('case3 can be used yb iloc:')

second_row=df_index_col.iloc[10]
print('select a single row')
print(second_row)
print()

second_row1=df_index_col.iloc[[1,6,256]]
print('select a multiple row')
print(second_row1)
print()

second_row2=df_index_col.iloc[:]
print('slice a row')
print(second_row2)
print()


second_row=df_index_col.iloc[:12, 2]
print('select a single column')
print(second_row)
print()

second_row1=df_index_col.iloc[:, [1,5]]
print('select a multiple column')
print(second_row1)
print()

second_row2=df_index_col.iloc[:, 2:5]
print('slice a column')
print(second_row2)
print()


df.drop(3, axis=0, inplace=True)

df.drop(index=2, inplace=True)

df.drop([1,200], axis=0, inplace=True)
print('all modified row')
print(df)

df.drop('Startup Name', axis=1, inplace=True)
df.drop(columns='Country', inplace=True)
df.drop(['Year Founded', 'Industry'], axis=1, inplace=True)
print('all modified column')
print(df)


df.rename(columns={'Funding Rounds':'Funding RoundsChanged'}, inplace=True)
df.rename(mapper={'Valuation':'ValuationChanged', 'Amount': 'AmountChanged'}, axis=1, inplace=True)
print('rename the columns')
print(df.rename)

df.rename(index={1:5}, inplace=True)
df.rename(mapper={2:4, 3:7}, axis=0, inplace=True)
print(' rename label columns')
print(df)  
print(len(df.columns))
print(df.columns)
sorteddf=df.sort_values(by='Growth Rate (%)')
print(df.to_string(index=False))

grouped=df.groupby('Funding RoundsChanged')['Growth Rate (%)'].sum()
print(grouped.to_string())
print('grouped:', len(grouped))

df_cleaned=df.dropna()
print('\n clende the data:', df_cleaned )

data=[1,2,3,4]
array1=pd.array(data)
print(data)