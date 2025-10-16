import functions as F

p = float(0.5) # Function power
a = int(2) # Required power of x
n = float(1) # x coefficient
x = float(1) # top variable
y = int(1) # bottom variable

t = F.top(p, a, x, n)
b = F.bottom(a, y)
out = t / b

print(out)