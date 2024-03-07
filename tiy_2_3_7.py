# Python crash course chapter 2

name = 'Erica'
name = 'abc'

print(f'hi {name}, do you want to learn some Python today?')

name
print(name.lower())
print(name.upper())
print(name.title())

print(name[len(name)//2])

origstr = 'oefening'

print(origstr.rfind('ing'))

bestanden = '.idea\t\t\t19-7-2--1 15.14\t\tBestandmap\n.pytest_cache\t9-7-2021 12:11\t\tBestandsmap\n__pycache__\t\t13-7-2021 14.24\t\tBestandsmap\ndata\t\t\t29-6-2021 17.28\t\tBestandsmap\nvenv\t\t\t18-6-2021 14.45\t\tBestandsmap\nexamples.py \t14-7-2021 17.14\t\tJetBrains PyCharm Community Edition \t 2 kB\nfactorial.py \t7-7-2021 11.03\t\tJetBrains PyCharm Community Edition \t 2 kB'

bestanden = bestanden.split('\n')

hidden = []

for bestand in bestanden:
    hidden.append(bestand.startswith('.'))

hidden = bestanden[hidden==True]
print(hidden)

