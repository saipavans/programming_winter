import datetime

def is_after(t1,t2):
    return t1>t2

def main():
    time_1 = datetime.datetime.now()
    time_2 = datetime.datetime.now()
    print(is_after(time_1,time_2))
    print(is_after(time_2,time_1))



if __name__ == '__main__':
    main()