


def choes_select(operation):
    def summ_(*args):
        return sum(args)

    def mines_(*args):
        result=0
        for arg in args:
            result = result - arg
        return result

    def multiply_(*args):
        result=1
        for arg in args:
            result = result * arg
        return result

    def average_(*args):
        return sum(args) / len(args)


    if  operation == 'sum':
        return summ_
    elif operation == 'mines':
        return mines_
    elif operation == 'multiply':
        return multiply_
    elif operation == 'average':
        return average_



sum_function = choes_select('sum')
mines_function = choes_select('mines')
multiply_function = choes_select('multiply')
average_function = choes_select('average')


print(sum_function(2,3,4,5))
print(mines_function(2,3,4,5))
print(multiply_function(2,3,4,5))
print(average_function(2,3,4,5))




def choes_support(support):

    def choes_team(team):
        return f"{support}'s favourite team is {team}"
    return choes_team




a=choes_support('Ali')
b=choes_support('Bob')
c=choes_support('Chris')

print(a('Fenerbahcce'))
print(b('Liverpool'))
print(c('Man Utd'))


















