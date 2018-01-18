import datetime as time

def increment(time_object, seconds):
    minutes_total = 0
    hours_total = 0

    while seconds > 60:
        minutes, seconds = divmod(seconds, 60)
        minutes_total+= minutes

    while minutes_total > 60:
        hours, minutes_total = divmod(minutes_total, 60)
        hours_total += hours

    return time_object.replace(hour = time_object.hour + hours_total, minute = time_object.minute + minutes_total, second = time_object.second + seconds)



def main():
    time1 = time.datetime.now()
    print(time1)
    print(increment(time1, 300))

if __name__ == '__main__':
    main()