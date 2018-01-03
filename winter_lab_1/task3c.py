start_time = (6 * 3600) + (52 * 60) # reference time 12 am

easy_pace_rate = (8 * 60) + 15 ## number of seconds to cover a mile
tempo_pace_rate = (7 * 60) + 12## number of seconds to cover a mile

time_taken = ((2 * easy_pace_rate) + (3 * tempo_pace_rate))

reach_time = start_time + time_taken

print("Reach Time: " + str(int(reach_time/3600)) + ":" + str(int((reach_time%3600)/60)))