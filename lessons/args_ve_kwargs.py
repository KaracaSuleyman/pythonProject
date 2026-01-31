

def summ(*args):
    sum_=0
    for arg in args:
        sum_ += arg
    return sum_


def sum2(*args):
    return sum(args)


def multiply(*args):
    multiply_=1
    for arg in args:
        multiply_ *= arg
    return multiply_



def avarage(*args):
    average_=0
    for arg in args:
       average_= (average_ + arg )
    average_=average_ / len(args)
    return average_

def average2(*args):
    return sum(args) / len(args)


print(summ(1,2,3,4))
print(sum2(1,2,3,4))
print(multiply(1,2,3,4))
print(avarage(1,2,3,4,5,6,7,8,9,10))
print(average2(1,2,3,4,5,6,7,8,9,10))
print('='*100)
print(('-_- ')*25)
print('='*100)

def greetings(name,*args):
    result=''
    result += name
    for arg in args:
        result +=' ' + arg+ ''
    return result


print(greetings('Ahmet', 'nasilsin','nasil gidiyor','havalar iyi mi?'))
print('='*100)
print(('-_- ')*25)
print('='*100)



def func(**kwargs):
    print(kwargs)



func(name='Ahmet', age=25)

print('='*100)
print(('-_- ')*25)
print('='*100)


def func2(need, *args,**kwargs):
    print(need)
    print('?'*14)
    for arg in args:
        print(arg)
    print('?'*14)
    for k,v in kwargs.items():
        print(k,v)


func2('selam',1,2,3,4,5,6,7,8,9,10, name='Ahmet', age=25,lang='python')











