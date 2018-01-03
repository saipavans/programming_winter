def do_twice(f,f_arg):
    f(f_arg)
    f(f_arg)

def print_twice(m):
    print(m)
    print(m)

do_twice(print_twice, "hello")