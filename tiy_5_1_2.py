# Python crash course chapter 5

# 5.1

car = 'subaru'

print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

car = 'audi'

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

print("Is car == 'Audi'? I predict False.")
print(car == 'audi')

print("Is car.title() == 'Audi'? I predict True.")
print(car.title() == 'Audi')

print("Is car != 'subaru'? I predict True.")
print(car.title() != 'subaru')

# 5.2

car = 'Audi'

print(" car.lower() == 'audi'? I predict True.")
print(car.lower() == 'audi')

age_sinterklaas = 150
age_kerstman = 100

print("Have Sinterklaas and de Kerstman the same age? I predict False")
print(age_sinterklaas == age_kerstman)

print("Is Sinterklaas older than de Kerstman? I predict True")
print(age_sinterklaas > age_kerstman)

print("both are older than 50 years I predict True")
print(age_sinterklaas > 50 and age_kerstman > 50)

print("one is older than 100 I predict True")
print(age_sinterklaas > 100 or age_kerstman > 100)

gifts = ['ball', 'wooden train', 'doll', 'gamebox']

print("A ball is  one of the presents they bring")
gift = 'ball'
print(gift in gifts)

print("they don't have lego")
gift = 'lego'
print(gift not in gifts)

