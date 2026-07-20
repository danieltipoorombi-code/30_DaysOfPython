def sum (num1, num2):
    return num1 + num2

print(sum(1, 2))


def area_circle(r):
    PI = 3.14
    area = PI * r ** 2
    return area_circle

print(area_circle(3))


def add_all_nums(*args):
    total = 0
    for num in args:
        if not isinstance (num, (int, float)):
            return "All items must be numbers"
        total += num
    return total

print(add_all_nums(1,2,3,4,2))
print(add_all_nums(1,2,3,4,'2'))


#celsius to fahrenheit
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

print(celsius_to_fahrenheit(0))


#check season
def check_season(month):
    month = month.lower()
    if month in ['september', 'october', 'november']:
        return 'Autumn'
    elif month in ['december', 'january', 'february']:
        return 'Winter'
    elif month in ['march', 'april', 'may']:
        return 'Spring'
    elif month in ['june', 'july', 'august']:
        return 'Summer'
    else:
        return 'Invalid month'
    

print(check_season('march'))

#slope of a linear equation
def calculate_slope(x1, y1, x2, y2):
    if x2 - x1 == 0:
        return "Slope is undefined"
    return (y2 - y1) / (x2 - x1)

print(calculate_slope(4,5,8,7))


# solution set of a quadratic equation
import math
def solve_quadratic_equation(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return ' No real solutions.'
    elif discriminant == 0:
        x = -b / (2*a)
        return [x]
    else:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        return [x1, x2]

print(solve_quadratic_equation(4,-3,3))

#print_list
def print_list(lst):
    for item in lst:
        print(item)
print_list([1,2,3,4])

#reverse a list
def reverse_list(arr):
    reversed_arr = []
    for i in range(len(arr) -1, -1, -1):
        reversed_arr.append(arr[i])
    return reversed_arr

print(reverse_list([1,2,3,4]))

#capitalize list
def capitalize_list_items(lst):
    capitalized = []
    for item in lst:
        capitalized.append(item.capitalize())
    return capitalized
print(capitalize_list_items(['danny', 'davy']))


#add_item 
def add_item(lst, item):
    new_list = lst.copy()
    new_list.append(item)
food_stuff = ['Banana', 'Mango', 'Tomato']
print(add_item(food_stuff, 'Meat'))

#remove-item
def remove_item(lst, item):
    new_list = lst.copy()
    if item in new_list:
        new_list.remove(item)
    else:
        print(f"{item} not found in list")
    return new_list

food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_stuff, 'Mango'))

numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))  

#sum of numbers
def sum_of_numbers(n):
    total = 0
    for i in range(0, n + 1):
        total += i
    return total

print(sum_of_numbers(5))  
print(sum_of_numbers(100)) 


#counts even and odds from 0 to n
def evens_and_odds(n):
    evens = 0
    odds = 0
    for i in range(0, n+1):
        if i % 2 == 0:
            evens += 1
        else:
            odds += 1
    print(f'The number of evens are {evens}')
    print(f'The number of odds are {odds}')


print(evens_and_odds(100))

