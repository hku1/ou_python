ages = [6, 72, 98, 24, 35, 17]

def isadult(x: int):
    """
    Check if an age is adult

    Happy path
    pre: x is an age
    post: True if age >= 18, otherwise False
    1: x > 18
    >>> isadult(25)
    True

    2: x = 18
    >>> isadult(18)
    True

    3: x < 18
    >>> isadult(17)
    False

    Pre broken path
    1: x is not an int
        raises: TypeError: argument must be an age
    >>> isadult('fifty')
    Traceback (most recent call last):
    ...
    TypeError: argument must be an age

    2: x < 0
        raises: ValueError: argument must be an age
    >>> isadult(-3)
    Traceback (most recent call last):
    ...
    ValueError: argument must be an age

    3: x > 150
        raises: ValueError: argument must be an age
    >>> isadult(151)
    Traceback (most recent call last):
    ...
    ValueError: argument must be an age
    """

    if not isinstance(x, int):
        raise(TypeError("argument must be an age"))
    if x < 0 or x > 150:
        raise(ValueError("argument must be an age"))
    return x >=18


adults = map(isadult, ages)

for x in adults:
  print(x)