import datetime


def print_time(time_object):
    print('%2d' % time_object.hour, '%2d' % time_object.minute, '%2d' % time_object.second)


def main():
    time_1 = datetime.datetime.now()
    print_time(time_1)


if __name__ == '__main__':
    main()
