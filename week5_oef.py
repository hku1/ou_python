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

class Book:
    def __init__(self, title, author, isbn, num_copies=0):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.num_copies = num_copies

    def sell_copy(self):
        if self.num_copies <= 0:
            raise ValueError("No copies left")
        else:
            self.num_copies -= 1

    def in_stock(self):
        return self.num_copies > 0

    def add_stock(self, num):
        self.num_copies += num

# Voeg een subklasse NonFictionBook toe, met als extra attribuut subject .
#
# Maak een object aan van die subklasse en vraag de gegevens er van op via obj.__dict__ om te kijken of het object
# inderdaad ook over de attributen beschikt die in de superklasse zijn gedefinieerd.

class NonFictionBook(Book):
    def __init__(self, title, author, isbn, num_copies=0):
        super().__init__(title, author, isbn, num_copies)
        self.subject = 'non-fiction'

nfbook1 = NonFictionBook('book title', 'HKU1', 4554764523)

print(nfbook1.__dict__)