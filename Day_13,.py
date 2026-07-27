numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
filtered_numbers = [num for num in numbers if num <= 0]
print(filtered_numbers)

#flatten list
list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [number for row in list_of_lists for number in row]
print(flattened_list)

#new list
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
output = [[c.upper(), c[:3].upper(), city.upper()] 
          for [[c, city]] in countries]
print(output)

#list of tuples
list_of_tuples = [(i, i**0, i**1, i**2, i**3, i**4, i**5) for i in range(6)]
print(list_of_tuples)

#concatenate names
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
output = [f'{first} {last}' for [[first, last]] in names]
print(output)

#lambda function for slope and y-intercept
# for slope
slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1)
#for y - intercept
y_intercept = lambda x1,  y1, x2, y2: y1 - slope(x1, y1, x2, y2) * x1

print(slope(1,3,4,6))
print(y_intercept(1, 2, 3,6))
