empty_list = []
print(empty_list)

list = [0,1, 3, 2, 7]
print(list)

print(len(empty_list))

print(list[0:4:2])

mixed_data_types = ['Tipo', 34, 5.9, True, 'Single', 'Kampala']
print(mixed_data_types)

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies)
print(len(it_companies))

#Print the first, middle and last company
print(it_companies[0])  # First company
print(it_companies[len(it_companies)//2])  # Middle company
print(it_companies[-1])  # Last company

it_companies.append('Twitter')
print(it_companies)

it_companies.insert(3, 'Tesla')
print(it_companies)

it_companies[0] = it_companies[0].upper()
print(it_companies)

#Join the it_companies with a string '#;  '
joined_companies = '#;  '.join(it_companies)
print(joined_companies)

#checking if a certain company exists
print('Google' in it_companies)

it_companies.sort()
print(it_companies)

it_companies.reverse()
print(it_companies)

#slice
it_companies.remove('Apple')
print(it_companies)

it_companies.pop()
print(it_companies)

it_companies.clear()
print(it_companies)

#Destroy the IT companies list
del it_companies

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack = front_end + back_end
full_stack.insert(5, 'Python')
full_stack.insert(6, 'SQL')
print(full_stack)

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
print(min(ages))
print(max(ages))

print(median := (ages[len(ages)//2] + ages[len(ages)//2 - 1]) / 2 if len(ages) % 2 == 0 else ages[len(ages)//2])
print(mean := sum(ages) / len(ages))

print(range_of_ages := max(ages) - min(ages))

#Compare the value of (min - average) and (max - average), use abs() method
print(abs(min(ages) - mean))
print(abs(max(ages) - mean))

#vFind the middle country(ies) in the countries list
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
print(countries[len(countries)//2])

#ivide the countries list into two equal lists if it is even if not one more country for the first half.

first_three, *scandic_countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
print(first_three)
print(scandic_countries)