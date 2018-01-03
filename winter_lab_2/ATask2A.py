import turtle

def square(t, l):
    t.fd(l)
    t.lt(90)
    t.fd(l)
    t.lt(90)
    t.fd(l)
    t.lt(90)
    t.fd(l)
    t.lt(90)

if __name__ == '__main__':
    turtle_obj = turtle.Turtle()
    square(turtle_obj, 100)
    turtle.mainloop()