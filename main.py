import pandas

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

color = data['Primary Fur Color'].value_counts()

gray_squirrels = len(data[data['Primary Fur Color'] == 'Gray'])
cinnamon_squirrels = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black_squirrels = len(data[data['Primary Fur Color'] == 'Black'])

print(gray_squirrels)

data_dict = {
    'Fur Color': ['Gray', 'Cinnamon', 'Black'],
    'Count': [gray_squirrels, cinnamon_squirrels, black_squirrels]
}

df = pandas.DataFrame(data_dict)
df.to_csv('squirrel_count.csv')
# print(color.Gray)
# color.to_csv('colors.csv')

# colors_df = pandas.DataFrame(color)
# colors_df.to_csv('colors_df.csv')
# print(colors_df)

# if data['Primary Fur Color'] == 'grey':
#     print('hello')


# with open('weather_data.csv') as weather:
#     data = weather.readlines()

# print(data)

# import csv

# with open('weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     print(data)
#     temperatures = []
#     i = 0
#     for row in data:
#         i += 1
#         # print(f'{i} + {row}')
#         if not i == 1:
#             temperatures.append(int(row[1]))
#     print(temperatures)

# data = pandas.read_csv('weather_data.csv')
# # print(data['temp'])
# # print(type(data))

# data_dict = data.to_dict()

# # print(data_dict)

# temp_list = data['temp'].to_list()
# # print(temp_list)

# total_sum = 0
# for temp in temp_list:
#     total_sum += temp

# # print(int(total_sum / len(temp_list)))

# average = sum(temp_list) / len(temp_list)
# # print(average)

# # print(data['temp'].mean())
# # print(data['temp'].max())

# # print(data['condition'])
# # print(data.condition)

# # get data in row
# # print(data[data.day == "Monday"])

# max_temp = data['temp'].max()

# # print(data[data.temp == max_temp])
# # print(data[data.temp == data['temp'].max()])

# monday = data[data.day == 'Monday']
# print((monday.temp * 1.8) + 32)

# # create a dataframe from scratch
# data_dict = {
#     "students": ['Amy', 'James', 'Angela'],
#     'scores': [76, 56, 65]
# }

# new_data = pandas.DataFrame(data_dict)
# new_data.to_csv('new_data.csv')
# print(new_data)

# a series is a list, basically the column in the table (dataframe)