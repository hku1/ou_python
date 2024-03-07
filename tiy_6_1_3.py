# Python crash course chapter 6

person = {}

person['first name'] = 'Harmjan'
person['last name'] = 'Kuipers'
person['age'] = 51
person['city'] = 'Rotterdam'

print(person['first name'])
print(person['last name'])
print(person['age'])
print(person['city'])

print(list(person.items()))
print(list(person.keys()))
print(list(person.values()))

favnmbrs = {'HJ' : 8, 'Simon' : 7, 'Teun' : 4, 'Marieke' : 3, 'Olaf' : 10}

print(list(favnmbrs.items()))

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