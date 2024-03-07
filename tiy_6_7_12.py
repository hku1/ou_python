# Python crash course chapter 6

person1 = {}

person1['first name'] = 'Harmjan'
person1['last name'] = 'Kuipers'
person1['age'] = 50
person1['city'] = 'Rotterdam'

person2 = {}

person2['first name'] = 'Marieke'
person2['last name'] = 'De Heer'
person2['age'] = 45
person2['city'] = 'Rotterdam'

person3 = {}

person2['first name'] = 'Kristien'
person2['last name'] = 'Kuipers'
person2['age'] = 48
person2['city'] = 'Amersfoort'

people = [person1, person2, person3]

for person in people:
    for k,v in person.items():
        print(f"{k} {v}\n")

pet1 = {'name' : 'woofwoof', 'species' : 'dog', 'owner' : 'Harry'}
pet2 = {'name' : 'miawmiauw', 'species' : 'cat', 'owner' : 'Susie'}
pet3 = {'name' : 'moomoo', 'species' : 'cow', 'owner' : 'McDonald'}

pets = [pet1, pet2, pet3]

for pet in pets:
    for k,v in pet.items():
        print(f"{k}: {v}\n")

fav_places = {
    'HJ' : ['Sydney', 'Munich', 'Rotterdam'],
    'Simon' : ['Rhoon', 'Rotterdam', 'school'],
    'Teun' : ['soccerfield', 'Madrid'],
}

for k,v in fav_places.items():
    print(f"{k}:")
    for info in v:
        print(f"{info}")
    print('\n')

favnmbrs = {
    'HJ' : [8, 50, 65],
    'Simon' : [7, 11, 40],
    'Teun' : [4, 12, 35],
    'Marieke' : [3, 13, 666],
    'Olaf' : [10],
}

for name, numbers in favnmbrs.items():
    if len(numbers) > 1:
        print(f"{name}'s favorite numbers are:")
        for number in numbers:
            print(f'{number}')
        print('\n')
    else:
        print(f"{name}'s favorite number is:")
        print(f'{numbers}')

cities = {
    'Rotterdam': {
        'country': 'NL',
        'pop': 5E5,
        'fact': 'largest harbour of Europe'
    },
    'Amsterdam': {
        'country': 'NL',
        'pop': 1E6,
        'fact': 'Ajax'
    },
    'NY': {
        'country': 'USA',
        'pop': 10E6,
        'fact': 'Statue of Liberty'
    },
}

for city, city_info in cities.items():
    print(f"{city}:")
    for k,v in city_info.items():
        print(f"{k}: {v}")
    print('\n')


