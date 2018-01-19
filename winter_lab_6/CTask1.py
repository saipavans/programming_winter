import winter_lab_6.my_time as time

try:
    time_obj = time.Time(60, 40, 40)
    print(time_obj.hours, time_obj.minutes, time_obj.seconds, sep=":")
except AttributeError:
    print("Could not create an instane of time. Please check the format.")
try:
    time_obj = time.Time(12, 40, 40)
    print(time_obj.hours, time_obj.minutes, time_obj.seconds, sep=":")
    print(time_obj.time_to_int())
except AttributeError:
    print("Could not create an instane of time. Please check the format.")