import turtle

def polygon(t, l, n):
    for i in range(0,n):
        t.fd(l)
        t.lt(360/n)


if __name__ == '__main__':
    turtle_obj = turtle.Turtle()
    polygon(turtle_obj, 100, 6)
    turtle.mainloop()