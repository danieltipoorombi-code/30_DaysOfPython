#Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
user_age = int(input('Enter a number: '))
if user_age >= 18:
    print('You are old enough to drive.')
else:
    years_left = 18 - user_age
    print(f"You need {years_left} more years to learn to drive.")


my_age =  25
your_age = int(input('Enter age: '))

if your_age> my_age:
    diff = your_age - my_age
    if diff == 1:
        print(f'You are {diff} years older than me.')
    else:
        print(f'You are {diff} years older than me.')

elif your_age < my_age:
    diff_age = my_age - your_age
    if diff_age == 1:
        print(f'I am {diff_age} years older than you.')
    else:
        print(f'I am {diff_age} years older thn you.')

else:
    print('We are the same age.')


#Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:

a = int(input("Enter number one: "))
b = int(input("Enter number two: "))

if a > b:
    print(f"{a} is greater than {b}")

elif a < b:
    print(f"{a} is smaller than {b}")
else:
    print(f"{a} is equal to {b}")

    #Write a code which gives grade to students according to theirs scores:
    score = int(input("Enter your score: "))

if 90 <= score <= 100:
    grade = "A"
elif 80 <= score <= 89:
    grade = "B"
elif 70 <= score <= 79:
    grade = "C"
elif 60 <= score <= 69:
    grade = "D"
elif 0 <= score <= 59:
    grade = "F"
else:
    grade = "Invalid score"

print(f"Your grade is: {grade}")



person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

# 1. Check if 'skills' key exists, if so print out the middle skill
if 'skills' in person:
    skills = person['skills']
    middle_index = len(skills) // 2
    print("Middle skill:", skills[middle_index])

# 2. Check if 'skills' key exists, check if person has 'Python' skill
if 'skills' in person:
    if 'Python' in person['skills']:
        print("Has Python skill: True")
    else:
        print("Has Python skill: False")

# 3. Determine developer title based on skills
if 'skills' in person:
    skills_set = set(person['skills']) # use set for easy comparison
    
    if skills_set == {'JavaScript', 'React'}:
        print('He is a front end developer')
    elif {'Node', 'Python', 'MongoDB'}.issubset(skills_set):
        print('He is a backend developer')
    elif {'React', 'Node', 'MongoDB'}.issubset(skills_set):
        print('He is a fullstack developer')
    else:
        print('unknown title')

# 4. If married and lives in Finland, print info in format
if person.get('is_married') and person.get('country') == 'Finland':
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.")
