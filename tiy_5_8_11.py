# Python crash course chapter 5

# 5.8 + 5.9

users = ['Simon', 'Teun', 'Olaf', 'HJ', 'admin']

for user in users:
    if user != 'admin':
        print(f'hello {user}, thank you for logging in again\n')
    else:
        print('Hello admin, would you like to see a status report?\n')

# 5.10

#users = ['Simon', 'Teun', 'Olaf', 'HJ', 'admin']
users = []

if users:
    for user in users:
        if user != 'admin':
            print(f'hello {user}, thank you for logging in again\n')
        else:
            print('Hello admin, would you like to see a status report?\n')
else:
    print('we need to find some users\n')

# 5.11

ordinals = [i for i in range(1,10)]

for i in ordinals:
    print(i)

for nmbr in ordinals:
    if nmbr == 1:
        print(f'{nmbr}st')
    elif nmbr == 2:
        print(f'{nmbr}nd')
    elif nmbr == 3:
        print(f'{nmbr}rd')
    else:
        print(f'{nmbr}th')
        

