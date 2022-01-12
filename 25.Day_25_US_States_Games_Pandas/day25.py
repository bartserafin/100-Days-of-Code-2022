# DAY 25

# Pandas and CSV


# with open('weather_data.csv', mode='r') as data_file:
#     data = data_file.readlines()

# import csv
#
# with open('weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     # for row in data:
#     #     print(row[1])
#
#     # extract temperatures
#     temperatures = []
#     for row in data:
#         if row[1] == 'temp':
#             continue
#         temp = int(row[1])
#         temperatures.append(temp)
#     print(temperatures)


        #### ---- PANDAS ---- #####

# import pandas
#
# data = pandas.read_csv('weather_data.csv')
#
# print(type(data))  # Data frame is a table, 2 dimensions, rows and columns
# print()
# print(data)
# print()
# print(data['temp'])  # Panda knows first row are the names of the columns, Series is a list, 1 dimension, single column
#
# data_dict = data.to_dict()  # convert data frame to a dictionary
# print()
# print(data_dict)
#
# temp_list = data['temp'].to_list()  # convert series to a list
# print()
# print(temp_list)
#
# # find the average of temps
# avg = round(sum(temp_list) / len(temp_list), 2)
# print(avg)
#
# # find the average of temps -- using PANDAS
# print(data['temp'].mean())
#
# # find max of temps -- using PANDAS
# print(data['temp'].max())
#
# # Get data in Columns
# print(data['condition'])
# # or
# print(data.condition)
#
# # Get data in row
# print(data[data.day == 'Monday'])
#
# # print row where the temp was max
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == 'Monday']
# print(monday.condition)
#
# monday_temp = int(monday.temp) * 9/5 + 32  # convert C to F
#
# # Create a dataframe
#
# data_dict = {
#     'students': ['Amy', 'James', 'Angela'],
#     'scores': [76, 56, 65]
# }
#
# data_new = pandas.DataFrame(data_dict)
# print(data_new)
#
# data_new.to_csv('data_new_csv')




### ---- The Great Squirrel Data Analysis from Central Park OpenData ---- ###
# https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw

# Challenge create a csv like so:
# , Fur Color Count
# 0, Grey, 2473
# 1, Red, 392
# 2, Black, 103
import pandas



squirrel_data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

fur_data = squirrel_data['Primary Fur Color']
fur_dict = {}

for row in fur_data:
    if row not in fur_dict:
        fur_dict[f'{row}'] = 1
    else:
        fur_dict[f'{row}'] += 1

fur_dict.pop('nan')

fur_dict = {
    'Fur color': ['Gray', 'Cinnamon', 'Black'],
    'Count': [fur_dict['Gray'], fur_dict['Cinnamon'], fur_dict['Black']]
}

data_frame_fur = pandas.DataFrame(fur_dict)

data_frame_fur.to_csv('fur_table')



