from math import *

x = float(input('x = '))
y = float(input('y = '))
a = float(input('a = '))
e = float(input('e = '))

def calcD(x, y, a, e):
    if x<0:
	    res = float(max(min(a, x ** a, e ** (x * a)), (a * x) + 1))
    elif x>=0 and x<7:
	    res = float((cos(x) ** 2) + sin(x**2) * max(x, y))
    else:
	    res = float(1 + 3 * cos(abs(x + y)))
    return res

res = calcD(x, y, a, e)
print(res)
