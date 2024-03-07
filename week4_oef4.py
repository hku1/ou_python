# Oefening 4
# Schrijf een decorator functie countcalls die bijhoudt hoe vaak een functie wordt aangeroepen. Schrijf dat aantal maal naar de console.console

# from typing import Union
# def countcalls(func):
#     c = 1
#     while True:
#         yield c
#         print(f'function {func.__name__} called {c}times')
#         c += 1
#
#         def wrapper_func(*args, **kwargs):
#             result = func(*args, **kwargs)
#
#             return wrapper_func
#
# @countcalls
# def power(x: Union[float, int], y: int) -> Union[float, int]:
#     if not isinstance(y, int):
#         raise (TypeError("exponent must be int"))
#     if not isinstance(x, (int, float)):
#         raise (TypeError("base must be number"))
#     if y == 0 and x == 0:
#         raise (ValueError("0 to the power of 0 is not defined"))
#     r = 1
#     negative_exponent = y < 0
#     if negative_exponent:
#         y = -y
#     while y > 0:
#         r = r * x
#         y = y - 1
#     if negative_exponent:
#         r = 1 / r
#     return r
#
# power(2,3)
# power(4,6)


from typing import Union

def countcalls(func):
    c = 0

    def wrapper_func(*args, **kwargs):
        nonlocal c
        c += 1
        print(f'function {func.__name__} called {c} times')
        result = func(*args, **kwargs)
        print("Resultaat: " + str(result))

    return wrapper_func

@countcalls
def power(x: Union[float, int], y: int) -> Union[float, int]:
    if not isinstance(y, int):
        raise TypeError("exponent must be int")
    if not isinstance(x, (int, float)):
        raise TypeError("base must be number")
    if y == 0 and x == 0:
        raise ValueError("0 to the power of 0 is not defined")
    r = 1
    negative_exponent = y < 0
    if negative_exponent:
        y = -y
    while y > 0:
        r = r * x
        y = y - 1
    if negative_exponent:
        r = 1 / r
    return r

power(2, 3)
power(4, 6)