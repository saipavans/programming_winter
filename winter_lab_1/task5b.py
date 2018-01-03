def do_twice(f,f_arg):
    f(f_arg)
    f(f_arg)

def print_msg(m):
    print(m)

do_twice(print_msg, "hello")