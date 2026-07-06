#day2 30 Days of pythom 
first_name = 'Tipo '
last_name = 'Daniel'
full_name = first_name + last_name
country = 'Uganda'
city = 'Kampala'
age = 34
year = 2026
is_married = True
is_true= 0
is_light_on = False
first_name, last_name, age, country = 'Tipo', 'Daniel', 34, 'Kampala'


print(type(first_name))
print(type(last_name))
print(type(full_name))
print(full_name)
print(len(first_name))
print(len(first_name) == len(last_name))

num1 = 5
num2 = 4
diff = num1 - num2
product = num1 * num2
division = num1 / num2
remainder = num1 % num2
floor_division = num1 // num2
area_circle = 3.14 * 30 ** 2 
circumference = 2 * 3.14 * 30

#radius as user input and calculate area
area_of_circle = 3.14 * int(input('Enter radius: ')) ** 2
print(area_of_circle)

first_name = input('Enter your first name: ')
last_name = input('Enter your last name: ')
country  = input('Enter your country: ')
age = int(input('Enter your age: ')) 
