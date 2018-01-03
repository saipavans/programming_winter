import turtle

bob = turtle.Turtle()

def draw(t,x):
    if x<3:
        t.fd(x)
        return
    draw(bob,x/3)
    t.lt(60)
    draw(bob,x/3)
    t.rt(120)
    draw(bob,x/3)
    t.lt(60)
    draw(bob,x/3)

draw(bob, 100)
turtle.mainloop()