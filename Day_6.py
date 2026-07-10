tuple2 =()
brothers = ('Dan', 'Dav', 'Emma', 'Elijah', 'Trevor')
sisters = ('Diana', 'Doreen', 'Daphine', 'Diana', 'Doreen')

siblings = brothers + sisters
print(siblings)
print(len(siblings))

parents = ('Vivi', 'Vovo')
family_members = siblings + parents
print(family_members)

food_stuff_tpl = ('rice', 'beans', 'potatoes', 'meat', 'fish', 'chicken')
print(list(food_stuff_tpl))


print(food_stuff_tpl[len(food_stuff_tpl)//2])
print(food_stuff_tpl[0:3])
print(food_stuff_tpl[-3:])

del food_stuff_tpl

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Norway' in nordic_countries)


