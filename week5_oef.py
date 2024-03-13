# Oefening 1

# a) Wat is de output van het volgende programma?
#
# class Circle:
#     def __init__(self):
#         self.radius = 11
#
# circle_1 = Circle()
# circle_2 = Circle()
#
# print(circle_1.radius)
# print(circle_2.radius)
#
# circle_1.radius = 1
#
# print(circle_1.radius)
# print(circle_2.radius)
#
# circle_1.other_radius = 1000
#
# print(circle_1.radius)
# print(circle_1.other_radius)
# print(circle_2.radius)

# antwoorden a)

 # 11
 # 11

 # 1
 # 11

 # 1
 # 1000
 # 11

 # b) see 'week5_oef1b.pptx'


# Oefening 2
# Bereid de klasse Circle uit met een klassevariabele number_of_circles .
# Zorg ervoor dat, elke keer wanneer er een circle-object wordt gemaakt, de klassevariabele met één wordt opgehoogd.
# Test je programma door een aantal circle-objecten aan te maken en te controleren of het aantal klopt.

# class Circle:
#     number_of_circles = 0
#     def __init__(self):
#         self.radius = 11
#         Circle.number_of_circles += 1
#
#     def tot_nr(self):
#         print(f'total no. of circles is: {Circle.number_of_circles}')
#
# circle_1 = Circle()
#
# circle_1.tot_nr()
#
# circle_2 = Circle()
#
# circle_2.tot_nr()
#
# circle_1.tot_nr()
#
# print(Circle.number_of_circles)

# Oefening 3
# Het uitgangspunt is de volgende code (voor een boekhandel):

# class Book:
#     def __init__(self, title, author, isbn, num_copies=0):
#         self.title = title
#         self.author = author
#         self.isbn = isbn
#         self.num_copies = num_copies
#
#     def sell_copy(self):
#         if self.num_copies <= 0:
#             raise ValueError("No copies left")
#         else:
#             self.num_copies -= 1
#
#     def in_stock(self):
#         return self.num_copies > 0
#
#     def add_stock(self, num):
#         self.num_copies += num

# Voeg een subklasse NonFictionBook toe, met als extra attribuut subject .
#
# Maak een object aan van die subklasse en vraag de gegevens er van op via obj.__dict__ om te kijken of het object
# inderdaad ook over de attributen beschikt die in de superklasse zijn gedefinieerd.

# class NonFictionBook(Book):
#     def __init__(self, title, author, isbn, num_copies=0):
#         super().__init__(title, author, isbn, num_copies)
#         self.subject = 'non-fiction'
#
# nfbook1 = NonFictionBook('book title', 'HKU1', 4554764523)
#
# print(nfbook1.__dict__)

# Oefening 4
# Een vierkantsvergelijking heeft de vorm: ax^2 + bx + c = 0
#
# We hebben er een klasse voor opgesteld, met een methode die je een lijst geeft met nul, een of twee oplossingen.
# Om dat te kunnen berekenen hebben we de discriminant nodig, waarvoor we een private methode hebben geschreven:

# import math
# class VierkantsVergelijking:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#         self.__discriminant = self.b * self.b - 4 * self.a * self.c
#     # def _discriminant(self):
#     #     return self.b * self.b - 4 * self.a * self.c
#
#     def solve(self):
#         discr = self.__discriminant
#         if discr < 0:
#             return []
#         elif discr == 0:
#             return [-self.b / 2 * self.a]
#         else:
#             return [(-self.b + math.sqrt(discr)) / 2 * self.a, (-self.b - math.sqrt(discr)) / 2 * self.a]
#
# # Testen kan als volgt:
#
# # 2 oplossingen: -1 en 1
# vk1 = VierkantsVergelijking(1, 0, -1)
# print(vk1.solve())
#
# # 1 oplossing: -1
# vk1 = VierkantsVergelijking(1, 2, 1)
# print(vk1.solve())
#
# # geen oplossingen
# vk1 = VierkantsVergelijking(2, 1, 2)
# print(vk1.solve())
# # Nu wordt elke keer dat de methode solve wordt aangeroepen, de discriminant opnieuw berekend.
# # Herschrijf de klasse daarom zo dat je bij initialisatie een private attribuut discriminant aanmaakt,
# # en dat attribuut in de methode solve gebruikt. Test de code.

# for the answer the original code has been adapted

# Oefening 5
# We nemen een verkorte versie van de klasse Breuk als uitgangspunt:

class Breuk:
    def __init__(self, teller, noemer):
        self.teller = teller
        self.noemer = noemer

    @property
    def noemer(self):
        return self.__noemer

    @noemer.setter
    def noemer(self, noemer):
        if noemer == 0:
            raise ValueError('noemer kan niet 0 zijn')
        self.__noemer = noemer

    def product(self, anderebreuk):
        return Breuk(self.teller * anderebreuk.teller, self.noemer * anderebreuk.noemer)

    def _inverse(self):
        return Breuk(self.noemer, self.teller)

    def quotient(self, anderebreuk):
        inv = anderebreuk._inverse()
        return Breuk(self.teller * inv.teller, self.noemer * inv.noemer)

    def show(self):
        print(str(self.teller) + "/" + str(self.noemer))

# Ongewenst aan deze code is dat er geen garantie is dat er als waarde voor de noemer geen 0 wordt gegeven.
# Dat is, uiteraard, niet goed.
# Maak daarom van de noemer een property. Geef een ValueError wanneer geprobeerd wordt een breuk een 0 als noemer te geven.

# Voor het antwoord de code aangepast

# testing

a = Breuk(1, 4)
b = Breuk(2, 3)
a.show()
b.show()

c = Breuk(1,0)
c.show()

