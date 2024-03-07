# Python crash course chapter 5

# 5.3

alien_color = ['green']

if 'green' in alien_color:
    print("congrats, you just earned 5 points")

# 5.3

alien_color = ['red']

if 'green' in alien_color:
    print("congrats, you just earned 5 points\n")
else:
    print('congrats, you just earned 10 points\n')

# 5.4

if 'green' in alien_color:
    print("congrats, you just earned 5 points\n")
elif 'yellow' in alien_color:
    print("congrats, you just earned 10 points\n")
else:
    print('congrats, you just earned 15 points\n')

# 5.6

age = 66

if age <2:
    print('a baby\n')
elif 2 <= age < 4:
    print('toddler\n')
elif 4 <= age < 13:
    print('kid\n')
elif 13 <= age < 20:
    print('teenager\n')
elif 20 <= age < 65:
    print('adult\n')
else:
    print('elder\n')

# 5.7

fav_fruit = ['apples', 'grapes', 'bananas']

fruit = 'apples'

if fruit in fav_fruit:
    print(f'you really like {fruit}\n')