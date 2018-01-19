import winter_lab_6.my_time as time

time_obj = time.Time(2,0,0)
new_time = time_obj.mul_time(4)
print(new_time.hours, new_time.minutes, new_time.seconds)