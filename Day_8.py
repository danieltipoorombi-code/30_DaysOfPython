dog = {'name': 'Max',
       'color': 'black',
       'breed': 'Golden Retriever',
       'legs': 4,
       'age' : 5}

student = {'First_name': 'Daniel',
           'Last_name': 'Tipo',
           'Gender': 'Male',
           'Age': 25,
           'Marital_status': 'Single',
           'Skills': ['Python', 'Java', 'C++'],
           'Country': 'Uganda',
           'City': 'Kampala',
           'Address': 'Kampala, Uganda'}

print(len(student))
print(student['Skills'])
print(type(student['Skills']))

student['Skills'].append('Raspberry Pi')
print(student['Skills'])

print(student.keys())
print(student.values())

print(student.items())

del student['Marital_status']
print(student)

dog.clear()
print(dog)