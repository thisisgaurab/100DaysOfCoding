import pandas as pd
from pandas import Series, DataFrame

df = pd.read_csv('census.csv', encoding='ISO-8859-1')       #loading the CSV file in the dataframe
print(df.columns)

# Group the data by 'STNAME' and calculate the sum for each state
df = df.groupby('STNAME')['POPESTIMATE2010', 'POPESTIMATE2011', 'POPESTIMATE2012', 'POPESTIMATE2013', 'POPESTIMATE2014', 'POPESTIMATE2015'].sum()

# Calculate the annual growth rates for the years 2010 to 2011, 2011 to 2012, 2013 to 2014, and 2014 to 2015
df['GrowthRate2010-2011'] = ((df['POPESTIMATE2011'] - df['POPESTIMATE2010']) / df['POPESTIMATE2010']) * 100
df['GrowthRate2011-2012'] = ((df['POPESTIMATE2012'] - df['POPESTIMATE2011']) / df['POPESTIMATE2011']) * 100
df['GrowthRate2013-2014'] = ((df['POPESTIMATE2014'] - df['POPESTIMATE2013']) / df['POPESTIMATE2013']) * 100
df['GrowthRate2014-2015'] = ((df['POPESTIMATE2015'] - df['POPESTIMATE2014']) / df['POPESTIMATE2014']) * 100

# Calculate the average annual growth rate and store it in a new column
df['average annual growth rate'] = df[['GrowthRate2010-2011', 'GrowthRate2011-2012', 'GrowthRate2013-2014', 'GrowthRate2014-2015']].mean(axis=1)


df['Average_annual_growth_rate'] = df[['GrowthRate0-1', 'GrowthRate1-2', 'GrowthRate3-4', 'GrowthRate4-5']].mean(axis = 1)

#claculating th predict population
df['predict_population'] = df['POPESTIMATE2015']*(1+df['Average_annual_growth_rate']/100)

#selecting the values that are positive
positive_value = df[df['predict_population']>0]
print(positive_value)