from turtle import *


screensize(2000, 2000)
tracer(0)
left(90)
k = 30

for i in range(5):
    setpos(pos()[0] + 6 * k, pos()[1] + 8 * k)
    setpos(pos()[0] - 8 * k, pos()[1] + 4 * k)
    setpos(pos()[0] + 2 * k, pos()[1] - 12 * k)
    
penup()

for i in range(-40, 40):
    for j in range(-40, 40):
        setpos(i*k, j*k)
        dot(4, 'red')
        
done()


