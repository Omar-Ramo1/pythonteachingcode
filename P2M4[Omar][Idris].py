
# import the file

import os
cmd = "curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/world_temp_mean.csv -o mean_temp.txt"
os.system(cmd)



# open in append plus mode and add Rio de Janeiro
mean_temp_file = open('mean_temp.txt', 'a+')
mean_temp_file.write("Rio de Janeiro,Brazil,30.0,18.0\n")

# seek to beginning and read headings
mean_temp_file.seek(0)
headings = mean_temp_file.readline()
headings = headings.split(',')

# print your name
print("Omar Idris")

# while loop to print city and highest monthly average temp
city_temp = mean_temp_file.readline()

while city_temp:
    city_temp = city_temp.split(',')
    print("City of", city_temp[0], "month ave: highest high is", city_temp[2], "Celsius")
    city_temp = mean_temp_file.readline()

mean_temp_file.close()

