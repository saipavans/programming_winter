import turtle

def circle(t, l, r):
    n = int ((2 * 3.14 * r)/l)
    for i in range(0,n):
        t.fd(l)
        t.lt(360/n)


if __name__ == '__main__':
    turtle_obj = turtle.Turtle()
    circle(turtle_obj, 5, 50)
    turtle.mainloop()