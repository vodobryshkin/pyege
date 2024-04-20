def d(x, y, a):
    return ((x * y > a) and (x > y) and (x < 8)) == 0


for a in range(1, 1000):
    if all(d(x, y, a) for x in range(1, 1000) for y in range(1, 1000)):
        print(a)
        break
      
