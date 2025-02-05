import datetime
#1
# Get the current date
current_date = datetime.datetime.now()

# Subtract five days from the current date
new_date = current_date - datetime.timedelta(days=5)

# Print the new date
print("Current date:", current_date.strftime("%Y-%m-%d"))  #аа так ттоже работает
print("Date after subtracting 5 days:", new_date.strftime("%Y-%m-%d"))


#2
yesterday = current_date - datetime.timedelta(days = 1)
tomorrow = current_date + datetime.timedelta(days = 1)
print("Current date:", current_date.strftime("%Y-%m-%d"))
print("Yesterday:", yesterday.strftime("%Y-%m-%d"))
print("Tomorrow:", tomorrow.strftime("%Y-%m-%d"))



#3
print("Now without milliseconds:", current_date.strftime("%Y-%m-%d %H:%M:%S"))



#4
# Example dates
date1 = datetime.datetime(2023, 10, 1, 12, 0, 0)
date2 = datetime.datetime(2023, 10, 2, 14, 30, 0)

# Calculate the difference between the two dates
difference = date2 - date1

# Get the difference in seconds
difference_in_seconds = difference.total_seconds()

# Print the difference in seconds
print("Difference in seconds:", difference_in_seconds)




#commands
com = dir(datetime)
print(com)