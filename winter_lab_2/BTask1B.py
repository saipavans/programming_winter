def do_n(f, n):
    for i in range(0,n):
        f()

def print_hello():
    print("Hello")

do_n(print_hello, 3)