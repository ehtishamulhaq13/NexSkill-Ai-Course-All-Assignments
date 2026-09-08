import pandas as pd
df = pd.read_csv('RealEstate-USA.csv',delimiter=",")
print(df)

print("df - data types" , df.dtypes)

print("df.info():   " , df.info() )

# display the last three rows
print('Last three Rows:')
print(df.tail(3))

# display the first three rows
print('First Three Rows:')
print(df.head(3))
print()

#Summary of Statistics of DataFrame using describe() method.
print("Summary of Statistics of DataFrame using describe() method", df.describe())

#Counting the rows and columns in DataFrame using shape(). It returns the no. of rows and columns enclosed in a tuple.
print("Counting the rows and columns in DataFrame using shape() : " ,df.shape)
print()

# access the Name column
price = df['price']
print("access the Name column: df : ")
print(price)
print()



# access multiple columns
price_price = df[['price','price']]
print("access multiple columns: df : ")
print(price_price)
print()

# Case 1 : using .loc - default case - starts here

#Selecting a single row using .loc
second_row = df.loc[1]
print("#Selecting a single row using .loc")
print(second_row)
print()

#Selecting multiple rows using .loc
second_row2 = df.loc[[1, 3]]
print("#Selecting multiple rows using .loc")
print(second_row2)
print()

#Selecting a slice of rows using .loc
second_row3 = df.loc[1:5]
print("#Selecting a slice of rows using .loc")
print(second_row3)
print()

#Conditional selection of rows using .loc
second_row4 = df.loc[df['price'] == 65000]
print("#Conditional selection of rows using .loc")
print(second_row4)
print()

#Selecting a single column using .loc
second_row5 = df.loc[:1,'price']
print("#Selecting a single column using .loc")
print(second_row5)
print()

#Selecting multiple columns using .loc
second_row6 = df.loc[:,['price','price']]
print("#Selecting multiple columns using .loc")
print(second_row6)
print()

second_row7 = df.loc[:1,'status':'price']
print("#Selecting a slice of columns using .loc")
print(second_row7)
print()

#Combined row and column selection using .loc
second_row8 = df.loc[df['price'] == 65000,'status':'price']
print("#Combined row and column selection using .loc")
print(second_row8)
print()
# Case 1 : using .loc - default case - ends here


# Case 2 : using .loc with index_col - starts here

df_index_col = pd.read_csv('RealEstate-USA.csv',delimiter=",")
print(df_index_col)
print(df_index_col.dtypes)
print(df_index_col.info())

#Selecting a single row using .loc
second_row = df_index_col.loc[112]
print("#Selecting a single row using .loc")
print(second_row)
print()

#Selecting multiple rows using .loc
second_row2 = df_index_col.loc[[112, 192]]
print("#Selecting multiple rows using .loc")
print(second_row2)
print()

#Selecting a slice of rows using .loc
second_row3 = df_index_col.loc[90:150]
print("#Selecting a slice of rows using .loc")
print(second_row3)
print()

#Conditional selection of rows using .loc
second_row4 = df_index_col.loc[df_index_col['price'] == 145000]
print("#Conditional selection of rows using .loc")
print(second_row4)
print()

#Selecting a single column using .loc
second_row5 = df_index_col.loc[:188,'price']
print("#Selecting a single column using .loc")
print(second_row5)
print()


#Selecting multiple columns using .loc
second_row6 = df_index_col.loc[:162,['price','price']]
print("#Selecting multiple columns using .loc")
print(second_row6)
print()

#Selecting a slice of columns using .loc
second_row7 = df_index_col.loc[:162,'status':'price']
print("#Selecting a slice of columns using .loc")
print(second_row7)
print()

#Combined row and column selection using .loc
second_row8 = df_index_col.loc[df_index_col['price'] == 65000,'status':'price']
print("#Combined row and column selection using .loc")
print(second_row8)
print()

# Case 2 : using .loc with index_col  -  ends here


print("# Case 3 : Using .iloc - starts here")

# Case 3 : Using .iloc - starts here

#Selecting a single row using .iloc
second_row = df_index_col.iloc[0]
print("#Selecting a single row using .iloc")
print(second_row)
print()

#Selecting multiple rows using .iloc
second_row2 = df_index_col.iloc[[1, 3,5]]
print("#Selecting multiple rows using .iloc")
print(second_row2)
print()

#Selecting a slice of rows using .iloc
second_row3 = df_index_col.iloc[2:5]
print("#Selecting a slice of rows using .iloc")
print(second_row3)
print()

#Selecting a single column using .iloc
second_row5 = df_index_col.iloc[:,2]
print("#Selecting a single column using .iloc")
print(second_row5)
print()

#Selecting multiple columns using .iloc
second_row6 = df_index_col.iloc[:,[2,4]]
print("#Selecting multiple columns using .iloc")
print(second_row6)
print()

#Selecting a slice of columns using .iloc
second_row7 = df_index_col.iloc[:,2:4]
print("#Selecting a slice of columns using .iloc")
print(second_row7)
print()

#Combined row and column selection using .iloc
second_row8 = df_index_col.iloc[[1, 3,5],2:4]
print("#Combined row and column selection using .iloc")
print(second_row8)
print()

# Case 3 : Using .iloc - ends here

# Next Run 
print("Next Run")

df.loc[len(df.index)] = [175,82,"RealEstate-USA.csv/lahore_model_town_6_kanal_excellent_house_for_sale_in_model_town-347795-8-12.html",3, 31239, "for_sale",145000, 4.0, "Puerto Rico", 731, 1800.0, "NaN"] 
print("Modified DataFrame - add a new row:")
print(df)
print()


#Remove Rows/Columns from a Pandas DataFrame


# delete row with index 1
df.drop(1, axis=0, inplace=True)
# delete row with index 1
df.drop(index=2, inplace=True)
# delete rows with index 3 and 5
df.drop([3, 5], axis=0, inplace=True)
# display the modified DataFrame after deleting rows
print("Modified DataFrame - Remove Rows:")
print(df)



# delete house size column
df.drop('house_size', axis=1, inplace=True)
# delete bed column
df.drop(columns='bed', inplace=True)
# delete status and price columns
df.drop(['status', 'price'], axis=1, inplace=True)
# display the modified DataFrame after deleting column
print("Modified DataFrame -  delete house size , bed , status , price , column :")
print(df)


#Rename Labels in a DataFrame
# rename column 'Name' to 'First_Name'
df.rename(columns= {'brokered_by': 'brokered_byChanged'}, inplace=True)
# rename columns 'Age' and 'City'
df.rename(mapper= {'bath': 'bathrooms', 'city':'city_name'}, axis=1, inplace=True)
# display the DataFrame after renaming column
print("Modified DataFrame  - Rename Labels :")
print(df)

#Example: Rename Row Labels
# rename column one index label
df.rename(index={0: 7}, inplace=True)
# rename columns multiple index labels
df.rename(mapper={1: 10, 2: 100}, axis=0, inplace=True)
# display the DataFrame after renaming column
print("Modified DataFrame - Rename Row - 0  >>> 7 , 1 >>> 10 , 2 >>> 100  Labels:")
print(df)

# select the rows where the age is greater than 25
selected_rows = df.query('bathrooms == \'1.0\' or bathrooms > 1.0')

print(selected_rows.to_string())
print(len(selected_rows))


# sort DataFrame by price in ascending order
sorted_df = df.sort_values(by='bathrooms')
print(sorted_df.to_string(index=False))

#Sort Pandas DataFrame by Multiple Columns

# 1. Sort DataFrame by 'Age' and then by 'Score' (Both in ascending order)
df1 = df.sort_values(by=['acre_lot', 'zip_code'])

print("Sorting by 'acre_lot' (ascending) and then by 'zip_code' (ascending):\n")
print(df1.to_string(index=False))

# group the DataFrame by the location_id column and
# calculate the sum of price for each category
grouped = df.groupby('bathrooms')['state'].sum()
print(grouped.to_string())
print("grouped :" , len(grouped))

# use dropna() to remove rows with any missing values
df_cleaned = df.dropna()
print("Cleaned Data:\n",df_cleaned)

# filling NaN values with 0
df.fillna(0, inplace=True)

print("\nData after filling NaN with 0:\n", df)

# create a list named data
data = [2, 4, 6, 8]
# create Pandas array using data
array1 = pd.array(data)
print(array1)



int_array = pd.array([1, 2, 3, 4, 5], dtype='int')
print(int_array)
print()





