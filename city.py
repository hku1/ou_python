def describe_city(name: str, country='NL'):
    print(f'{name} is a city in {country}')

describe_city('Rdam')
describe_city(name='Munich', country='DE')
describe_city(name='NY', country='USA')

describe_city(1)