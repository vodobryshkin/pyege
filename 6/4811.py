from turtle import *


screensize(2000, 2000)
tracer(0)
left(90)
k = 30

for i in range(1):
    setpos(pos()[0] + 5 * k, pos()[1] + 4 * k)
    setpos(pos()[0] + 4 * k, pos()[1] - 4 * k)
    setpos(pos()[0] - 7 * k, pos()[1] - 2 * k)
    setpos(pos()[0] - 2 * k, pos()[1] + 2 * k)
    
penup()

for i in range(-40, 40):
    for j in range(-40, 40):
        setpos(i*k, j*k)
        dot(4, 'red')
        
done()


