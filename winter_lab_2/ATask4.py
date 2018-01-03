import turtle

def arc(t, l, r, arc_angle):
    n = int ((2 * 3.14 * r)/l)
    for i in range(0,n):
        t.fd(l)
        t.lt(arc_angle/n)


if __name__ == '__main__':
    turtle_obj = turtle.Turtle()
    arc(turtle_obj, 5, 50, 270)
    turtle.mainloop()