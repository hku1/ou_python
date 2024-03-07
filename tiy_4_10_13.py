# Python crash course chapter 4

pizzas = ['margherita', 'pepperoni', 'mozarella', 'delacasa', 'salami', 'funghi', 'tonno']

print(f"The first 3 pizzas are ")
for pizza in pizzas[:3]:
    print(pizza)

print(f"The next 2 pizzas are ")
for pizza in pizzas[3:5]:
    print(pizza)

print(f"The last 3 pizzas are ")
for pizza in pizzas[-3:]:
    print(pizza)

friend_pizzas = pizzas[:]

friend_pizzas.append('proscuito')

print("my favorite pizzas are ")
for pizza in pizzas:
    print(pizza)

print("my friend's favorite pizzas are ")
for pizza in friend_pizzas:
    print(pizza)