# Python crash course chapter 7

# 7.8

sandwich_orders = ['BLT', 'cheese', 'ham', 'tomato','brie']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f'{current_sandwich} sandwich prepared\n')
    finished_sandwiches.append(current_sandwich)

print(f'prepared {finished_sandwiches} sandwiches\n')

# 7.9

sandwich_orders = ['BLT', 'cheese', 'ham', 'tomato','brie', 'pastrami', 'pastrami', 'pastrami']
finished_sandwiches = []

print("no pastrami sandwiches today\n")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f'{current_sandwich} sandwich prepared\n')
    finished_sandwiches.append(current_sandwich)

print(f'prepared {finished_sandwiches} sandwiches')

# 7.10

responses = {}

polling_active = True

while polling_active:
    name = input('what is your name: ')
    dest = input('what is your fav holiday destination?: ')
    responses[name] = dest

    repeat = input('\nWould you like to let another person respond? (yes/ no): ')
    if repeat.lower() == 'no':
        polling_active = False

print('\n --- Poll results ---')
for name, dest in responses.items():
    print(f"{name}'s favourite holiday destination is: {dest}")


lst1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lst2 = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
lst3 = zip(lst1, lst2)
print(list(lst3))

for x, y in enumerate(lst3):
    print(f'{x} * 2 is {y}\n')

lst1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lst2 = {i : 17*i for i in lst1}
print(lst2)

lst_gen = (i*17 for i in lst1)

for i in lst_gen:
    print(i)

