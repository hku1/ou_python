
# Oefening 1
# We hebben bij de oefeningen bij het vorige onderwerp de klasse Cupboard een methode show gegeven.
#
# Zorg er nu voor, door de magic methode __str__ te implementeren, dat we de methode show weg kunnen laten,
# en dat een print-opdracht met een Cupboard object als parameter het object op dezelfde wijze laat zien.
#
# We geven de code even weer zonder de documentatie en de tests.

from typing import Union
class Cupboard:

    MINIMUMDISTANCE = 20
    def __init__(self, height: Union[int, float], width: Union[int, float]):
        self.height = height
        self.width = width
        self.number_of_shelves = 0

    @property
    def height(self) -> Union[int, float]:
        return self.__height

    @height.setter
    def height(self, height: Union[int, float]):
        if not isinstance(height, (int, float)):
            raise(TypeError("Height and width must be numbers"))
        if height <= 0:
            raise ValueError("Height must greater than zero!")
        self.__height = height

    @property
    def width(self) -> Union[int, float]:
        return self.__width

    @width.setter
    def width(self, width: Union[int, float]):
        if not isinstance(width, (int, float)):
            raise(TypeError("Height and width must be numbers"))
        if width <= 0:
            raise ValueError("Width must greater than zero!")
        self.__width = width


#
    def __str__(self):
        """Returns a string representation of the cupboard."""
        return "Cupboard height: {0:d}, width: {1:d}, number of shelves: {2}".format (self.height,
                                                                                      self.width,
                                                                                      self.number_of_shelves)

    @property
    def number_of_shelves(self) -> int:
        return self.__number_of_shelves

    @number_of_shelves.setter
    def number_of_shelves(self, number: int):
        if not isinstance(number, int):
            raise(TypeError("number of shelves should be an int"))
        if number < 0:
            raise ValueError("number of shelves should not be negative")
        if self.height / (number + 1) < self.MINIMUMDISTANCE:
            raise ValueError("too many shelves")
        else:
            self.__number_of_shelves = number


# use class

c = Cupboard(100, 80)
c.number_of_shelves = 3
print(c)


import inspect