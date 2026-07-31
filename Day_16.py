from datetime import datetime
now = datetime.now()
print(now)                     
day = now.day                  
month = now.month              
year = now.year                 
hour = now.hour                 
minute = now.minute           
second = now.second
timestamp = now.timestamp()
print(day, month, year, hour, minute, second)
print('timestamp', timestamp)
print(f'{day}/{month}/{year}, {hour}:{minute} : {second}') 

#get the current day, month, yearx, hour, minute and timestamp
now = datetime.now()
print('Day: ', now.day)
print('Month: ', now.month)
print('Year: ', now.year)
print('Hour: ', now.hour)
print('Minute: ', now.minute)
print('Timestamp: ', now.timestamp())

#format the current date using this format: %m/%d/%Y %H:%M:%S
now = datetime.now()
formatted = now.strftime('%m/%d/%Y,%H:%M:%S')
print(formatted)

#'Today is 5 December, 2019' Change this time string to time object\
data_string = '5 December, 2019'
date_object = datetime.strptime(data_string, '%d %B, %Y')
print(date_object)
print(type(date_object))

#calculate the time difference between now and new year
now = datetime.now()
new_year = datetime(now.year + 1, 1, 1)
time_left = new_year - now
print(f'Time left until New Year; {time_left}')
print(f'Days left: {time_left.days}')

#Calculate the time difference between 1 January 1970 and now
epoch = datetime(1970, 1, 1)
now = datetime.now()
diff = now - epoch
print(f"Seconds since Jan 1, 1970: {diff.total_seconds()}")
print(f"Days since Jan 1, 1970: {diff.days}")

eroch = datetime(2005, 11, 24)
now = datetime.now()
diff2 = now - eroch
print(diff2.days)

