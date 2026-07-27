'''
map: Transforms every item in a list. Returns a new list with same length.
Ex: map(lambda x: x*2, [1,2,3]) → [2,4,6]filter: Keeps only items that meet a condition. Returns a shorter list.
Ex: filter(lambda x: x>5, [1,2,10]) → [10]reduce: Reduces a list to a single value by combining items.
Ex: reduce(lambda x,y: x+y, [1,2,3]) → 6
'''

'''
Higher order function: A function that takes another function as argument or returns a function.
 Ex: map, filterClosure: A function that remembers variables from the outer scope even after that outer function is done.
 Decorator: A special higher order function that wraps another function to add behavior. Ex: @staticmethod
'''
# a call function before map, filter or reduce
from functools import reduce

def square(x):
    return x * x

def is_even(x):
    return x % 2 == 0

def add(x, y):
    return x + y

numbers = [1, 2, 3, 4, 5]

mapped = list(map(square, numbers))        # [1, 4, 9, 16, 25]
filtered = list(filter(is_even, numbers))  # [2, 4]
reduced = reduce(add, numbers)             # 15

print(mapped)
print(filtered)
print(reduced)

#Use for loop to print each country in the countries list.
countries = ['Uganda', 'Congo', 'Rwanda', 'Kenya', 'Tanzania', 'Seychelles']

for country in countries:
    print(country)

# Use for to print each name in the names list.
names = ['Daniel', 'David', 'Elijah', 'Emmanuel']

for name in names:
    print(name)

# Use for to print each number in the numbers list.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in numbers:
    print(number)

#using map to create new list by changing each country to uppercase
countriesUpper = list(map(str.upper, countries))
print(countriesUpper)

#use map to change each number to its square
numbersSquare = list(map(square, numbers))
print(numbersSquare)

#use map to change each name to upper case
namesUpper = list(map(str.upper, names))
print(namesUpper)

#filter to filter out countries containing and
andCountries = list(filter(lambda c: 'and' in c.lower(), countries))
print(andCountries)

# filter out countries containing six letters and more
sixOrMore= list(filter(lambda c: len(c) >= 6, countries))
print(sixOrMore)

#chaining two or more list iterators
chained = list(map(str.upper, filter(lambda c: len(c)>=6, countries)))
print(chained)

#declare a function called get_string_lists which takes a list and returns only string items
def get_string_lists(lst):
    return list(filter(lambda x: isinstance(x, str), lst))
mixed = [1, 'hello', 3.14, 'world', True]
print(get_string_lists)

#use reduce to sum all the numbers in the numbers list
from functools import reduce

total = reduce(lambda x, y: x + y, numbers)
print(total)

#use reduce to concatenate all the countries to produce a sentence

sentence = reduce(lambda acc, c: acc + c + ', ', countries[:-1]) + 'are African countries.'
print(sentence)

#getb first ten countries
def get_first_ten_countries(country_list):
    return country_list[:10]


