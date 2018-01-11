import os


def my_walk(dirname):
    for name in os.listdir(dirname):
        if name.startswith('.'):
            continue
        path = os.path.join(dirname, name)
        if os.path.isfile(path):
            print(path)
        else:
            my_walk(path)


my_walk(".")
