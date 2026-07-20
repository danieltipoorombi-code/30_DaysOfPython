#random id generators
import random
import string
def random_user_id():
    characters = string.ascii_letters + string.digits
    user_id = ''.join(random.choice(characters) for _ in range(6))
    return user_id

print(random_user_id())
    
3
#user_id modification
import random
import string

def user_id_gen_by_user():
    chars = int(input('Enter number of characters: '))
    count = int(input('Enter number of IDs to generate: '))

    characters = string.ascii_letters + string.digits

    for _ in range(count):
        user_id = ''. join(random.choice(characters) for _ in range(chars))
        print('#' + user_id)



user_id_gen_by_user()



#rgb color gen

import random

def rgb_color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f'rgb({r}, {g}, {b})'

print(rgb_color_gen())

#list of colors
import random
import string

def list_of_hex_colors(n):
    hex_chars = '0123456789abcdef'
    colors = []
    for _ in range(n):
        color = '#' + ''.join(random.choice(hex_chars) for _ in range(6))
        colors.append(color)
    return colors

print(list_of_hex_colors(3))


#list of rgb colors'
import random

def list_of_rgb_colors(n):
    for _ in range(n):
        colors= []
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        colors.append(f'rgb({r}, {g}, {b})')
    return colors

print(list_of_rgb_colors(3))

#shuffle_list
import random 

def shuffle_list(lst):
    shuffled = lst[:]
    random.shuffle(shuffled)
    return shuffled 
print(shuffle_list([1,2,3,4,5,6]))


#random numbers from 0 to 9
import random

def unique_random_numbers():
    return random.sample(range(10), 7)

print(unique_random_numbers())