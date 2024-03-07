# week 2 oefeningen 2 tot 4

# oefening 2

lettercount = {'a': 3, 'e': 8, 'i': 1, 'o': 4, 'u': 0, 'y': 0}

nmbr = 9
nmbr in list(lettercount.values())

nmbr = 8
nmbr in list(lettercount.values())

# oefening 3

jaar = {'maanden': 12, 'weken': 52, 'dagen': 365}

str = 'Een jaar heeft {maanden} maanden, {weken} weken en {dagen} dagen.'.format(**jaar)
print(str)

# oefening 4

fruit = {'appel': 1, 'banaan': 2, 'citroen': 3, 'dadel': 4}

fruit.update({'elderberry': 0, 'framboos': 0, 'granaatappel': 0})

# 'setdefault' method in answers