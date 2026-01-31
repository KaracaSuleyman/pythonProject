import time
from unittest import result


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Operation took {end - start} seconds")
        return result
    return wrapper
@timer
def power(list):
    result = []
    for i in list:
        result.append(i ** 2)
    return result

@timer
def cube(list):
    result = []
    for i in list:
        result.append(i ** 3)
    return result
@timer
def summ(*args):
    time.sleep(3)
    return sum(args)


power(range(10000000))
