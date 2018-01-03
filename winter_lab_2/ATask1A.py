import turtle

def square(t):
    t.fd(100)
    t.lt(90)
    t.fd(100)
    t.lt(90)
    t.fd(100)
    t.lt(90)
    t.fd(100)
    t.lt(90)

if __name__ == '__main__':
    turtle_obj = turtle.Turtle()
    square(turtle_obj)
    turtle.mainloop()