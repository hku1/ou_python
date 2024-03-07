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

describe_city(1)
