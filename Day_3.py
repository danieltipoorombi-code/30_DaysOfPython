age = 43
height = 5.9
complex = 3 + 2j
#Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
base = int(input('Enter base: '))
height = float(input('Enter height: '))
area= 0.5 * base * height

a = int(input('Enter a: '))
b = int(input('Enter b: '))
c = int(input('Enter c: '))
perimeter = a + b + c

length = int(input('Enter length: '))
width = int(input('Enter width: '))
area_rectangle = length * width
perimeter_rectangle = 2 * (length + width)

radius = int(input('Enter radius: '))
area = 3.14 * radius ** 2
circumference = 2 * 3.14 * radius
print(circumference)


print(int(7 // 3) ==int(2.7))

print(type('10') == type(10))

#weekly earning
hours = int (input('Enter hours: '))
hourly_rate = int(input('Enter hourly rate: '))
weekly_earning = hourly_rate * hours
print('Weekly earning: $', weekly_earning)