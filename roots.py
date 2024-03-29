# Oefeningen week 4
# Oefening 1
# In deze opgave ontwikkel je een module roots (roots.py) waarmee nulpunten van een tweedegraads vergelijking berekend kunnen worden. De nulpunten van een tweedegraads vergelijking worden gevonden door x2+bx+c = 0 op te lossen, voor gegeven coëfficienten a, b, c. Kijk zo nodig naar de wiki pagina https://nl.wikipedia.org/wiki/Vierkantsvergelijking voor meer informatie.
#
# Je implementeert in de module roots twee functies:
#
# Een public functie abc die de oplossingen berekent aan de hand van de meegegeven coëfficiënten a, b, en c.
# Een private functie discriminant die de discriminant voor gegeven coëfficiënten berekent (discriminant is gelijk aan b^2 – 4ac).
# Los de opgave in stappen op:
#
# a) We willen abc en discriminant implementeren voor integers. Wanneer is er sprake van één, twee, of geen oplossingen?
# b) Geef de signaturen van de functies abc en discriminant in de vorm van type hints.
# c) Schrijf op basis van je analyse het contract voor functies abc en discriminant. Geef een exception als a, b of c geen integers zijn.
# d) Schrijf op basis van het contract de testen die nodig zijn in de vorm van doctest.
# e) Implementeer beide functies.
# f) Test je implementatie en haal eventuele fouten eruit.
# g) Voeg unittests toe voor abc.


import math
def abc(a:int, b:int, c:int) -> list[float]:
    """
    Solves quadratic equation for integers a,b and c, and a not 0
    :param a: int, not 0
    :param b: int
    :param c: int
    :return: list x containing 1 or 2 floats
    :raises: Type error, Value error, see subcontracts

    Happy path
    pre: a int not 0, b int ,c int
    post: solved quadratic equation returning list x containing 1 or 2 floats

    1. valid parameters, 2 solutions
    >>> abc(1,5,6)
    [-2.0, -3.0]

    2. D = 0 (1 solution)
    >>> abc(1,2,1)
    [-1.0]

    pre-broken path
    1. a, b, c not ints
    >>> abc(1.5,5,6)
    Traceback (most recent call last):
    ...
    TypeError: a, b and c must be ints

    2. a = 0
    >>> abc(0,5,6)
    Traceback (most recent call last):
    ...
    ValueError: a should not be 0

    """
    if not all(isinstance(value, int) for value in [a, b, c]):
        raise TypeError("a, b and c must be ints")

    if a == 0:
        raise ValueError('a should not be 0')

    def _discriminant(a, b, c):
        d = b**2 - 4*a*c
        return d

    d = _discriminant(a, b, c)

    if d < 0:
        raise ValueError('no solutions with real numbers possible')
    else:
        x = [(-b + math.sqrt(d)) / (2 * a), (-b - math.sqrt(d)) / (2 * a)]
        if x[0] == x[1]:
            x.pop(1)
    return x


