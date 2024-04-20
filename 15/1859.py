def d(x, y, a):
    return (2*x + y != 70) or (x < y) or (a < x)


for a in range(100, 1, -1):
    if all(d(x, y, a) for x in range(1, 1000) for y in range(1, 1000)):
        print(a)
        break
    
