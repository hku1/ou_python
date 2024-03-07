# Python crash course chapter 8

# 8.1

def display_message():
    print("I learn a lot from this book")

display_message()

# 8.2

def fav_book(title):
    print(f'One of my fav books is {title}')

fav_book('Nirwana')

# 8.3

def make_shirt(size, text):
    print(f'A T shirt of size {size} and text {text}')

make_shirt('L', '"ohno"')

# 8.4

def make_shirt(size='L', text='I Love Python'):
    print(f'A T shirt of size {size} and text {text}')

make_shirt()
make_shirt(size='M')
make_shirt(size='XS', text='hahaha')

# 8.5


def describe_city(name: str, country='NL'):
    print(f'{name} is a city in {country}')

describe_city('Rdam')
describe_city(name='Munich', country='DE')
describe_city(name='NY', country='USA')

describe_city(1.1) # does not raise TypeError?

# 8.9

msgs = ['hello', 'BrB', 'LuvU', 'CU', 'S6']

def show_messages(msgs: list[str]):
    for msg in msgs:
        print(msg)

show_messages(msgs)

# 8.10

msgs = ['hello', 'BrB', 'LuvU', 'CU', 1]
sent_msgs = []
def show_messages(msgs: list[str]):
    if not msgs:
        print('\nno messages')
    else:
        for msg in msgs:
            print(f'\n{msg}')

def send_messages(msgs):
    while msgs:
        curr_msg = msgs.pop()
        print(f'\nsend message {curr_msg}')
        sent_msgs.append(curr_msg)

send_messages(msgs)
show_messages(msgs)
show_messages(sent_msgs)

# 8.11

msgs = ['hello', 'BrB', 'LuvU', 'CU', 1]
sent_msgs = []
def show_messages(msgs: list[str]):
    if not msgs:
        print('\nno messages')
    else:
        for msg in msgs:
            print(f'\n{msg}')

def send_messages(msgs):
    while msgs:
        curr_msg = msgs.pop()
        print(f'\nsend message {curr_msg}')
        sent_msgs.append(curr_msg)

send_messages(msgs[:])
show_messages(msgs)
show_messages(sent_msgs)

# 8.12

fillings = ['bacon', 'egg', 'cheese', 'ham', 'salami', 'pesto', 'tomato']

import random

jane = random.sample(fillings, k=random.randint(2, 5))
hj = random.sample(fillings, k=random.randint(2, 2))
simon = random.sample(fillings, k=random.randint(1, 3))

def sandwich(*fillings):
    print('\nsandwich filling')
    for filling in fillings:
        print(f'- {filling}')

sandwich('tomato', 'cheese', 'egg')
sandwich('hj')

# 8.13

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know from a user"""
    user_info['first name'] = first
    user_info['last name'] = last
    return user_info

hku1 = build_profile('Harmjan', 'Kuipers', hobby='cycling', food='hamburger', work='RnD')

print(hku1)

# 8.14

def car_info(mnfctr, model, **info):
    info['manufacturer']= mnfctr
    info['model']= model
    return info

car = car_info('Honda', 'Jazz', mpg=8.6, speed=120, airco=True)
print(car)

#8.15


