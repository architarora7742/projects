# Pandas library is very useful if you are doing anything data science related in python.
# You have a lot of flexibility in pandas as compared to excel.
# You can work with a lot larger datasets
# dataframe is the object type for pandas

import pandas as pd

df = pd.read_csv('pokemon_data.csv')

# print(df)

# To print the first three/n rows of data, you can use the head and pass in the number of rows if you don't by default, it is set to 5
# print(df.head(3))
# The numbering starts from 0

# You can also get last rows by using the tail function
# print(df.tail())

# You can also ingest other file types like Excel, txt
# df_xlsx = pd.read_excel('pokemon_data.xlsx')
# print(df_xlsx)

# You can also read tab separated files, you can set delimiter to anything that is separating those columns.
# df_txt = pd.read_csv('pokemon_data.txt', delimiter="\t")
# print(df_txt)

# ! Reading the headers and it will return the list of all the column headers
print(df.columns)

# ! Read each column / specific column
# print(df['Name']) # the name is case-sensitive

# print(df['Name'][0:5]) # To get the first five values of that particular column
# print(df.Name)

#! If you want to get multiple columns at the same time
# You have to give nested-list for that
# print(df[['Name', 'Type 1', 'Type 2']])

# ! Read Each Row
# print(df.iloc[1])
# print(df.iloc[1:4]) # iloc stands for integer location.

# for index,row in df.iterrows():
#     print(index, row['Name'])
# ! Finding specific data in our dataset, this is not integer based like iloc
# You can also give multiple conditions.
# print(df.loc[df['Type 1'] == 'Grass'])


# ! Read a specific location (R, C) R --> Row, C --> Column
# print(df.iloc[2,1])

# ! Describe will give useful metrics for all the columns like mean, count etc
# print(df.describe())

# ! You can sort values for any particular column
# df.sort_values('Name', ascending=False)
# print(df.sort_values(['HP','Type 1'], ascending=False))
# print(df.sort_values(['Type 1','HP'], ascending = [1,0])) # TYPE 1 WILL BE ASCENDING AND HP WILL BE DESCENDING.

# TODO: NOW WE ARE GOING TO MAKE CHANGES TO OUR DATA.
# # adding new column
# df['Total'] = df['HP'] + df['Attack'] + df['Sp. Def'] + df['Speed'] + df['Defense']
# print(df.head())

# ! Drop a specific column, you have to assign it back to the df to implement the changes.
# df = df.drop(columns=['Total'])
# print(df.head())

# ? Add the column to the df in a different way
df['Total'] = df.iloc[:,4:10].sum(axis=1) # add all the column from 4 to 9
# axis = 1 means you are adding columns horizontally, 0 for vertically

# print(df.head())
# * Move the head column to the left of HP
# cols = list[df.columns.values]
# df = df[['Total', 'HP', 'Defense']]
# print(df.head())

# Save the changes to a new csv file or Excel file
# df.to_csv('modified.cv')
# df.to_csv('modified.csv', index=False)
# df.to_excel('m.xlsx', index=False)
# df.to_csv('m.txt', index=False, sep='\t')


# TODO: ADVANCE FILTERING OF DATA
# You can give multiple conditions but they should be separated by parenthesis.
# and will not work to add conditions, we have to use &
var1 = df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison')]
var2 = df.loc[(df['Type 1'] == 'Grass') | (df['Type 2'] == 'Poison')]

var3 = df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['HP'] > 70)]
# You can reset the index and, by default, it will save the old index, but if you don't want that to happen, we can do drop = True

# new_df = var3.reset_index(drop=True)
# print(new_df)
# ! If you want it to save to the old variable without creating new variable
# var3.reset_index(drop=True, inplace=True)
# print(var3)
# ? if you want to remove very specific type data.
# ? We want to filter out all the names that contain mega.
# ? If we use ~ sign then we will drop all the rows that contain mega
new_df = df.loc[~df['Name'].str.contains('Mega')]
# print(new_df)

import re
# ! Regular expression is used for filtering out data based on the textual patterns.
x = df.loc[df['Name'].str.contains('Fire|Grass', regex=True)]
# To ignore the case sensitivity
y = df.loc[df['Name'].str.contains('fire|grass', flags=re.I, regex=True)]
z = df.loc[df['Name'].str.contains('^pi[a-z]*', flags=re.I, regex=True)]
# print(z)

# ! We can actually change our df based on a condition.
# df.loc[df['Type 1'] == 'FLamer', 'Type 1'] = "Fire"
# df.loc[df['Type 1'] == 'Fire', 'Legendary'] = True

# ! Conditional Changes
# df.loc[df['Total'] > 500, ['Generation', 'Legendary']] = 'Test Value'

# ! You can give multiple values to multiple columns at once
# df.loc[df['Total'] > 500, ['Generation', 'Legendary']] = ["Test 1", "Test 2"]
# The Python Interpreter has given me the warning that in future it will give me the error based on the datatype that you are giving.
# It will cross-check the datatype before inputting into a particular column.
# ! HOW TO USE GROUP BY FUNCTION
# df.groupby(['Type 2']).mean().sort_values('Defense', ascending=False)
# df.groupby(['Type 1']).count()
df.groupby(['Type 1', 'Type 2']).count()

# ! Working with large amounts of data
# * If your dat size is very big, then you can run it in chunks unless you have very powerful machine to load all that data in memory
# ? chunk-size 5 means that 5 rows are passed.
for df in pd.read_csv('pokemon_data.csv', chunksize=5):
    print(df.head(1))






