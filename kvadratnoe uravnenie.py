import math

def m(a,b,c):
    D = b*b - 4*a*c
    if D<0:
        print("Error")
    else:
        x1 = (-b + math.sqrt(D))/(2*a)
        x2 = (-b - math.sqrt(D))/(2*a)
        print(x1)
        print(x2)

m(-5, 14, -5)
