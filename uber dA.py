import numpy as np
import pandas as pd
df=pd.read_csv('D:\DS\python\case study\My Uber Drives - 2016.csv')
# Write a code to get the top 7 rows of the dataset.
print(' Write a code to get the top 7 rows of the dataset.\n',df.head(7))
# Write a code to get the last 5 rows of the dataset.
print('Write a code to get the last 5 rows of the dataset.\n',df.tail(5))
# 4. Get the total number of rows and columns in the dataset.
print('Get the total number of rows and columns in the dataset.\n',df.shape)
# 5. Get the total number of elements in the datase.
print(' Get the total number of elements in the dataset\n',df.size)
# 6. Write a code to get the total number of NULL values across every column in the
# dataset.
print(' Write a code to get the total number of NULL values across every column in the dataset.\n',df.isna().sum())
# 7. Write a code to get the total number of Non-NULL values across every column in the
# dataset.
print('Write a code to get the total number of Non-NULL values across every column in the dataset.\n',df.notna().sum())
# 8. Write a code to get the entries having NULL values in the 'Purpose' column.
print('Write a code to get the entries having NULL values in the Purpose column.\n',df[df['PURPOSE*'].isna()])
# 9. Write a code to get the entries having Non-NULL values in the 'Purpose'.
print('Write a code to get the entries having Non-NULL values in the Purpose. \n',df[~df['PURPOSE*'].isna()])
# 11. Write a code to remove the * in every column name using the rename function.
print('Write a code to remove the * in every column name using the rename function.\n',df.rename(columns={'START_DATE*':'START_DATE','END_DATE*':'END_DATE','MILES*':'MILES','PURPOSE*':'PURPOSE','CATEGORY*':'CATEGORY','START*':'START','STOP*':'STOP'}))
# 12. Write a code to remove the * in every column name using the str.replace() function.
df2=df.rename(columns={'START_DATE*':'START_DATE','END_DATE*':'END_DATE','MILES*':'MILES','PURPOSE*':'PURPOSE','CATEGORY*':'CATEGORY','START*':'START','STOP*':'STOP'})
print(df2.columns.str.replace('START_DATE','START_DATE8*').str.replace('END_DATE','END_DATE*').str.replace('MILES','MILES*').str.replace('PURPOSE','PURPOSE*').str.replace('CATEGORY','CATEGORY*').str.replace('START','START*').str.replace('STOP','STOP*'))
# 14. Get the entries in the data where the START location is 'Fort Pierce'.
print(' Get the entries in the data where the START location is Fort Pierce\n',df[df['START*']=='Fort Pierce'])
# 15. Get the entries in the data where the STOP location is 'Fort Pierce'.
print(' Get the entries in the data where the STOP location is Fort Pierce\n',df[df['STOP*']=='Fort Pierce'])
#16. Write a code to sort the entries in the data in descending order of the 'MILES' column.
print('Write a code to sort the entries in the data in descending order of the MILES column.\n',df.sort_values('MILES*',ascending=False))
# 17. Write a code to drop all the rows where there are NULL values in the STOP column.
print('Write a code to drop all the rows where there are NULL values in the STOP column.\n',df[df['STOP*'].isna()==False])
# 18. Get the Statistical Properties about the numerical columns in the data.
print(df.describe())
# 19. Create a report in an html file using pandas profiling.
# 20. Get the unique and total number of unique values in the START and STOP column of the data.
print('\n\n\nthe unique and total number of unique values in the START\n',df['START*'].unique(),'\n\n\nand STOP column of the data\n\n\n',df['STOP*'].unique())
# 21. Get the rides where we have the same START and STOP locations.
print('rides where we have the same START and STOP locations\n',df[df['START*']==df['STOP*']])
# 23. Use value_counts() function to demonstrate the proportion of different categorical values in the data.
print(df['CATEGORY*'].value_counts())
# 25. Find the favorite starting point according the the total number of MILES covered.
print('favorite starting point according the the total number of MILES covered.\n',df.groupby('START*').agg({'MILES*':'count'}).sort_values('MILES*',ascending=False))
# Find the starting point for the ride where maximum miles are covered.
print('starting point for the ride where maximum miles are covered\n\n\n',df.groupby('START*').agg({'MILES*':'sum'}).sort_values('MILES*',ascending=False))
# 27. Check the data types of all the columns in the dataset.
print('data types of all the columns in the dataset.\n')
df.info()
# 28. Drop the 'unknown location' value from START and STOP column.
print('Drop the unknown location value from START and STOP column\n\n',df[(df['STOP*']!='Unknown Location') | (df['START*']!='Unknown Location')])
df=df[(df['STOP*']!='Unknown Location') | (df['START*']!='Unknown Location')]
# 29. Find the most popular START-STOP pair according to the total number of rides covered.
print('most popular START-STOP pair according to the total number of rides covered\n\n\n',df.groupby(['START*','STOP*']).count().sort_values('START_DATE*',ascending=False)['START_DATE*'])
# 30. Convert the datatypes of START_DATE and END_DATE columns to datetime.
df['START_DATE*'] = pd.to_datetime(df['START_DATE*'], errors='coerce')
df['END_DATE*'] = pd.to_datetime(df['END_DATE*'], errors='coerce')
# 31. Extract the month from START_DATE and try to get the proportion of rides of different months.
print('Extract the month from START_DATE and try to get the proportion of rides of different months\n\n\n',df.pivot_table(index=df['START_DATE*'].dt.month,aggfunc={'START*':'count'}))

# 32. Find the average distance covered each month.
print('average distance covered each month\n\n\n',df.pivot_table(index=df['START_DATE*'].dt.month,aggfunc={'MILES*':'mean'}))

# 33. Extract the day from the START_DATE column.
#print(' Extract the day from the START_DATE column\n\n\n',df['DAY']=df['START_DATE*'].dt.day)
df['DAY'] = df['START_DATE*'].dt.day
print('Extract the day from the START_DATE column\n\n\n',df)
# 34. Find the total miles covered per category per purpose.
print('the total miles covered per category per purpose.\n\n\n',df.pivot_table(index=df['CATEGORY*'],aggfunc={'MILES*':'sum'}))
df1=df.pivot_table(index=df['CATEGORY*'],aggfunc={'MILES*':'sum'})
# 35. Find the percentage of Business Miles covered and Personal mIles covered.
df1['MILES*']=df1['MILES*'].apply(lambda x:x*100/df1.sum())
print('Find the percentage of Business Miles covered and Personal mIles covered\n\n\n',df1)