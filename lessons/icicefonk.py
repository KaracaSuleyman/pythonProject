

def calculate(x):

    def square(a):
      return a**2
    def cube(a):
      return a**3
    def factorial(a):
        fact=1
        for i in range(1,a+1):
            fact*=i
        return fact
    def quartic(a):
        return a**0.5
    square_=square(x)
    cube_=cube(x)
    factorial_=factorial(x)
    quartic_=quartic(x)
    return f' Squar is: {square_}\n Cube is:  {cube_}\n Factorial is:{factorial_}\n Quart is: {quartic_}'

# print(calculate(6))
#


def calculate(*args):
    def sum_(tuple):
        return sum(tuple)
    def power_of(tuple):
        power=1
        for i in tuple:
            power*=i
        return power
    return f'Sum: {sum(args)}\nPower_of : {power_of(args)}'


print(calculate(6,5,6,7,8,9))

























