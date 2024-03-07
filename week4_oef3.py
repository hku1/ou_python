from typing import Union

def log_func(func):
    result = 0
    print("Aanroep van ", func.__name__)
    def wrapper_func(*args, **kwargs):
        for arg in args:
            print("Input: ", arg)
        result = func(*args, **kwargs)
        print("Resultaat: " + str(result))
    return wrapper_func

@log_func
def power(x: Union[float, int],  y: int) -> Union[float, int]:
    if not isinstance(y, int):
        raise (TypeError("exponent must be int"))
    if not isinstance(x, (int, float)):
        raise (TypeError("base must be number"))
    if y == 0 and x == 0:
        raise (ValueError("0 to the power of 0 is not defined"))
    r = 1
    negative_exponent = y < 0
    if negative_exponent:
        y = -y
    while y > 0:
        r = r * x
        y = y - 1
    if negative_exponent:
        r = 1/r
    return r

power(2, 3)