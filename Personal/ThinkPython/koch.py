import turtle



def koch(x):
    if x < 3:
        l = x
    else:
        l = x/3

    t.fd(l)
    t.lt(60)
    t.fd(l)
    t.rt(120)
    t.fd(l)
    t.lt(60)
    t.fd(l)



def fractal(x):
    for i in range(3):
        koch(x)
        t.rt(120)

t = turtle.Turtle()
screen = turtle.Screen()
fractal(40)
turtle.done()
    
