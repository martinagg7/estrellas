import turtle

estrella = turtle.Pen()

#ajustes estrella 
estrella.fillcolor('yellow')
estrella.begin_fill()

estrella.rihgt(90)
n=int(input('¿Cuántas puntas quiere que tenga la estrella?'))
for i in range(n):
    estrella.forward(100)
    estrella.right(180-180/n)
estrella.end_fill()

