import turtle
import math
bob = turtle.Turtle()
t = turtle.Turtle()

def square(t,length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

def polygon(t, length, n):
    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)


def circle(t,r):
    circumference = 2 * math.pi * r
    n = 200
    length = circumference / n
    polygon(t, length, n)

given_radius = int(input("please define the radius of your circle: "))

screen = turtle.Screen()
screen.title(bob)
circle(bob,given_radius)
turtle.done()

