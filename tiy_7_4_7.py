# Python crash course chapter 7

# 7.4

# prompt = '\nWhich topping would you like?: '
#
# topping = ""
# while topping != 'quit':
#      topping = input(prompt)
#      if topping != 'quit':
#         print(f'\n{topping} added')

# 7.5 + 7.6


prompt = '\nwhat is your age?: '

age = 0
price = ''

# conditional test

# while age != 'quit':
#     age = input(prompt)
#     if age != 'quit':
#         age = int(age)
#         if age < 3:
#             price = 'free'
#         elif 12 >= age > 3:
#             price = '$10'
#         else:
#             price = '$15'
#         print(f'price is {price}')


# active variable

active = True

while active:
    age = input(prompt)
    if age != 'quit':
        age = int(age)
        if age < 3:
            price = 'free'
        elif 12 >= age > 3:
            price = '$10'
        elif age > 12:
            price = '$15'
        print(f'price is {price}')
    else:
        active = False





