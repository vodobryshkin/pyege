def d(x, y, a):
    return (x**2 - 10*x + 16 > 0) or (y**2 - 10*y + 21 > 0) or (x*y < 2*a)


for a in range(1, 100):
    if all(d(x, y, a) for x in range(1, 1000) for y in range(1, 1000)):
        print(a)
        break
    
