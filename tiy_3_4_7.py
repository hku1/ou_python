# Python crash course chapter 3

dinner_gsts = []
dinner_gsts.append('Barrack Obama')
dinner_gsts.append('Bill Gates')
dinner_gsts.append('Navalny')
dinner_gsts.append('Zelensky')
dinner_gsts.append('Vladimir Poetin')

print(f'dear {dinner_gsts[0]}, I would like to invite you for dinner')
print(f'dear {dinner_gsts[1]}, I would like to invite you for dinner')

unvlble = dinner_gsts.pop(2)
print(f'I just learned {unvlble} can not make it')

dinner_gsts.insert(2, 'Joe Biden')

print(dinner_gsts)

print(f'I invited {dinner_gsts[2]} instead')

print(f'dear {dinner_gsts} I found a bigger table, so I will invite some more guests')

dinner_gsts.insert(0, 'Mark Rutte')
dinner_gsts.insert(len(dinner_gsts)//2, 'The Pope')
dinner_gsts.append('Donald Trump')

print(dinner_gsts)

uninvite = dinner_gsts.pop()
print(f'sorry {uninvite}, you can not come')

uninvite = dinner_gsts.pop()
print(f'sorry {uninvite}, you can not come')

uninvite = dinner_gsts.pop()
print(f'sorry {uninvite}, you can not come')

uninvite = dinner_gsts.pop()
print(f'sorry {uninvite}, you can not come')

uninvite = dinner_gsts.pop()
print(f'sorry {uninvite}, you can not come')

uninvite = dinner_gsts.pop()
print(f'sorry {uninvite}, you can not come')

print(f'{dinner_gsts[0]} you are still invited')
print(f'{dinner_gsts[-1]} you are still invited')

del dinner_gsts[0]
del dinner_gsts[0]

print(dinner_gsts)


#  for guest in range(len(dinner_gsts), -1, -1):
#      print(f'Sorry {dinner_gsts[guest]}, I have to cancel your invitation')
#      dinner_gsts.pop(guest)
#
# print(range(len(dinner_gsts), -1, -1))


