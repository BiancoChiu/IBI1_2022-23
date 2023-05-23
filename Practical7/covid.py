import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Changing the current working directory to the specified path
os.chdir(r'E:\文档\Semester_2\IBI\Week 7. Public Health Informatics')
# Reading the CSV file 'full_data.csv' into a pandas DataFrame
covid_data = pd.read_csv('full_data.csv')

# Printing the second column from every 100th row from the first 1000 rows
print(covid_data.iloc[0:1001:100, 1])
# show total cases for all rows corresponding to Afghanistan.
print(covid_data[covid_data['location'] == 'Afghanistan'].iloc[:, 4])

# Creating a new DataFrame 'new_data'
new_data = covid_data[covid_data['date'] == '2020-03-31'].loc[:, [False, True, True, True, False, False]]
# Printing the mean of the 'new_cases' column in the 'new_data' DataFrame
print('mean new cases in 2020-03-31:', np.mean(new_data.loc[:, 'new_cases']))
# Printing the mean of the 'new_deaths' column in the 'new_data' DataFrame
print('mean new deaths in 2020-03-31:', np.mean(new_data.loc[:, 'new_deaths']))

world_data = covid_data[covid_data['location'] == 'World']
# Extracting the 'date', 'new_cases', and 'new_deaths' columns from the 'world_data' DataFrame
world_dates = world_data.loc[:, 'date']
world_cases = world_data.loc[:, 'new_cases']
world_deaths = world_data.loc[:, 'new_deaths']

# Creating a boxplot using the 'new_cases' and 'new_deaths' columns in the 'new_data' DataFrame
plt.boxplot(new_data.iloc[:, 1:3], labels=['new cases', 'new deaths'])
plt.title('new cases and new deaths on 31 March 2020')
plt.ylabel('case numbers')
plt.show()

# Creating line plots for 'world_cases' and 'world_deaths' against 'world_dates'
plt.plot(world_dates, world_deaths, 'r', label='world deaths')
plt.plot(world_dates, world_cases, 'b', label='world cases')
plt.title('new cases and new deaths worldwide')
plt.ylabel('case numbers')
plt.xticks(world_dates.iloc[0:len(world_dates):4], rotation=-90)
plt.legend()
plt.show()

# Creating line plots for 'China_total_cases' and 'China_total_deaths' against 'China_dates'
# By plotting the graphs, we can see at what point the surge in the number of infections occurred.
China_data = covid_data[covid_data['location'] == 'China']
China_dates = China_data.loc[:, 'date']
China_total_cases = China_data.loc[:, 'total_cases']
China_total_deaths = China_data.loc[:, 'total_deaths']
plt.plot(China_dates, China_total_deaths, 'r', label='China total deaths')
plt.plot(China_dates, China_total_cases, 'b', label='China total cases')
plt.title('new cases and new deaths in China')
plt.ylabel('case numbers')
plt.xticks(world_dates.iloc[0:len(world_dates):4], rotation=-90)
plt.legend()
plt.show()
