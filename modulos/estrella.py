import turtle

estrella = turtle.Pen()

estrella.fillcolor('yellow')
estrella.begin_fill()

estrella.rihgt(90)
n=int(input('¿Cuántas puntas quiere que tenga la estrella?'))
for i in range(n):
    estrella.forward(100)
    estrella.right(180-180/n)

import turtle 

estrella=turtle.Pen()
estrella.shape('star')

estrella.fillcolor('yellow')
estrella.color('orange')

estrella.begin_fill()

n=int(input('¿Cuántas puntas quiere que tenga la estrella?'))

for i in range(n):
    estrella.foward(100)
    estrella.right(180-180/n)


estrella.end_fill()

