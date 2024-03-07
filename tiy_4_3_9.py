# Python crash course chapter 4

for number in range(1,21):
    print(number)


# nmbrs = []
# for number in range(1,10000001):
#     nmbrs.append(number)
# print(len(nmbrs))
# print(min(nmbrs))
# print(max(nmbrs))
# print(sum(nmbrs))

for number in range(1, 21, 2):
    print(number)

thrs=[]
for number in range(3, 31, 3):
    thrs.append(number)
    print(number)

cubes=[]
for value in range(1, 11):
    cubes.append(value**3)

for cube in cubes:
    print(cube)


cubes = [value**3 for value in range(1, 11)]
print(cubes)


