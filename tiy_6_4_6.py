# Python crash course chapter 6

prgm_wrds = {
    'shallow copy' : 'only change pointer var, not object pointer refers to',
    'static typing' : 'variable type declared upfront',
    'immutable' : 'value cannot change',
    'hashable' : 'immutable and value does not point to object that can change value',
    'oop' : 'object oriented programing',
}

print(f"'shallow copy': {prgm_wrds.get('shallow copy')}\n")
print(f"'static typing': {prgm_wrds.get('static typing')}\n")
# etc..

for key, value in prgm_wrds.items():
    print(f"{key}: {value}\n")

rivers = {
    'Nile' : 'Egypt',
    'Rhine' : 'NL',
    'Seine' : 'France',
}

for key, value in rivers.items():
    print(f'The river {key} runs through {value}\n')

for key in rivers:
    print(f'{key}\n')

for value in rivers.values():
    print(f'{value}\n')

fav_lang = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python',
}

take_poll = ['HJ', 'jen', 'Simon', 'phil']

for name in take_poll:
    if name in fav_lang:
        print(f'thank you {name}, for taking the poll\n')
    else:
        print(f'{name}, please take the poll\n')

