# Oefening 1
# Stel een functie dictvaluesfromto op, met als parameters een dictionary en twee waarden: fromval en toval.
# De functie verandert in de dictionary elke waarde die gelijk is aan fromval in toval.
# Als defaultwaarden gebruik je None voor fromval en 0 voor toval.
#
# a) Schrijf de functiedefinitie, met type hints.
# b) Voeg documentatie toe: een beschrijving, en documentatie voor de parameters.
# c) Voeg één Happy path subcontract toe, en minimaal één ander subcontract.
# d) Voeg test cases toe aan de subcontracten, in doctest.
# e) Implementeer de functie.
# f) Draai de tests.

# write function

def dictvaluesfromto (dct: dict, fromval: float = None, toval:float = 0) -> dict:
    """
     Stel een functie dictvaluesfromto op, met als parameters een dictionary en twee waarden: fromval en toval.
     De functie verandert in de dictionary elke waarde die gelijk is aan fromval in toval.
     Als defaultwaarden gebruik je None voor fromval en 0 voor toval.
    : param dct: dictionary with ints and/or floats
    :param fromval: int,float
    :param toval: int, float
    :return: dictionary with ints and/or floats
    :raises: Type error

    Happy path
    pre: dct is dictionary with ints and/or floats, fromval is int, float, toval is int,float
    post: dictionary with  ints and/or floats

    1. input dictionary with ints and/or floats, fromval, toval int or floats
    >>> nmbrdict= {'a': 2, 'b': 4, 'c': 8.9}
    >>> print(dictvaluesfromto(nmbrdict, 2, 16))
    {'a': 16, 'b': 4, 'c': 8.9}

    Pre broken path
    1: input is list
         raise (TypeError("dct must be dictionary"))
    >>> lst = [1, 2, 3]
    >>> print(dictvaluesfromto(lst, 2, 16))

    2. dictionary contains non integers or floats
        raise TypeError("dictionary values must be ints or floats")
    >>> nmbrdict= {'a': 2, 'b': 4, 'c': 8.9, 'd': 'e'}
    >>> print(dictvaluesfromto(nmbrdict, 2, 16))

    3. fromval and/or toval not int or float
    >>> nmbrdict= {'a': 2, 'b': 4, 'c': 8.9}
    >>> print(dictvaluesfromto(nmbrdict, 'a', 16))

    """

    if not isinstance(dct, dict):
        raise (TypeError("dct must be dictionary"))

    if not all(isinstance(value, (int, float)) for value in dct.values()):
        raise TypeError("dictionary values must be ints or floats")

    if not isinstance(fromval, (int, float)):
        raise (TypeError("base must be number"))

    if not isinstance(toval, (int, float)):
        raise (TypeError("base must be number"))

    for key in dct:
        if dct[key] == fromval:
            dct[key] = toval

    return(dct)

nmbrdict= {'a': 2, 'b': 4, 'c': 8.9}

# print(nmbrdict)
# print(dictvaluesfromto(nmbrdict.copy(), 2, 16))
