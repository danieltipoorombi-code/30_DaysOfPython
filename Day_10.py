#iterate 0 to 10
for i in range(0, 11):
    print(i)


#from 10 to 0
for i in range(10, -1, -1):
    print(i)

#triangle of # with 7 lines
for i in range(1, 8):
    print('#' * i)


#rectangle
for row in range(4):
    for col in range(8):
        print('#', end='')
    print()

#multiplication table
for i in range(0, 11):
    print(f'{i} x {i} = {i * i}')

#iterate through list
tech_list =  ['Python', 'Numpy','Pandas','Django', 'Flask'] 

for item in tech_list:
    print(item)

# even numbers from 0 to 100
for i in range(0, 101, 2):
    print(i)

#odd number from 0 ro 100
for i in range(0, 100,):
    if i % 2 == 1:
          print(i)

total = 0
for i in range(0, 101):
    total += i
    print(f'The sum is {total}')

evens_sum = 0
odds_sum = 0

for i in range (0, 101):
    if i % 2 == 0:
        evens_sum += i
    else:
        odds_sum += i

    print(f'the sum of evens is {evens_sum} and odds is {odds_sum}')