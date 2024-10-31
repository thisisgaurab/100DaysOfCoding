'''My name is Gaurab Upreti. This program reads the csv files, group the state together, take the sum. It then
assigns the annual growth rate between 2010 and 2015 iand put it as a column in the data frame. It then takes the mean
of the average growth rate and filter the value such that negative values are neglected and at last we use the formula to
predict the population of 2016 which we add as a column in the dataframe.'''

import pandas as pd

state = pd.read_csv('census.csv', encoding='ISO-8859-1')  # loading the data from csv file

grouped_data = state.groupby('STNAME')[['POPESTIMATE2010', 'POPESTIMATE2011', 'POPESTIMATE2012', 'POPESTIMATE2013', 'POPESTIMATE2014', 'POPESTIMATE2015']]   #group the data according to STNAME
grouped_sum = grouped_data.sum()          #taking the sum of states

#creating the column for 4 annual growth rate
cols = ['GrowthRate2010-2011', 'GrowthRate2011-2012', 'GrowthRate2013-2014', 'GrowthRate2014-2015']

def growth_rate(growth_col_name, current_col_name, previous_col_name):
    grouped_sum[growth_col_name] = ((grouped_sum[current_col_name] - grouped_sum[previous_col_name])/ grouped_sum[previous_col_name]) *100

#adding the 4 different growth rate in the dataframe

growth_rate('GrowthRate2010-2011', 'POPESTIMATE2011', 'POPESTIMATE2010')
growth_rate('GrowthRate2011-2012', 'POPESTIMATE2012', 'POPESTIMATE2011')
growth_rate('GrowthRate2013-2014', 'POPESTIMATE2014', 'POPESTIMATE2013')
growth_rate('GrowthRate2014-2015', 'POPESTIMATE2015', 'POPESTIMATE2014')

grouped_sum['Average_Growth_Rate'] = grouped_sum[cols].mean(axis = 1);

#only taking the rows whose average growth rate is >0
pop_prediction = grouped_sum[grouped_sum["Average_Growth_Rate"]>0]


#using the formula to predict the population of 2016. This will add the predicted population of 2016 in the last column of dataframe
pop_prediction.loc[:,'POPESTIMATE2016'] = pop_prediction['Average_Growth_Rate'] * pop_prediction['POPESTIMATE2015'] + pop_prediction['POPESTIMATE2015']

#printing the predicted population
print(pop_prediction)
