def do_twice(f,f_arg):
    f(f_arg)
    f(f_arg)

def do_four(f,f_arg):
    do_twice(f,f_arg)
    do_twice(f,f_arg)

def print_msg(m):
    print(m)

do_four(print_msg, "spam")