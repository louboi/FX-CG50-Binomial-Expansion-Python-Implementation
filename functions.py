'''All functions and classes used in the main.py program'''

def top(p:float, a:int, x:float, n:float):
    '''Calculates the top value for the fraction'''
    for i in range(a):
        x = (p - i) * x
        i += 1
    x = x * (n ** a)
    return x

def bottom(a:int, y:int):
    '''Calculates the bottom value for the fraction'''
    for i in range(1, a + 1):
        y = i * y
        i += 1
    return y

