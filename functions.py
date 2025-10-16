def top(p, a, x, n):
    for i in range(a):
        x = (p - i) * x
        i += 1
    x = x * (n ** a)
    return x

def bottom(a, y):
    for i in range(1, a + 1):
        y = i * y
        i += 1
    return y

