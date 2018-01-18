import datetime as time

today = time.datetime.today()
days = ['mon','tue','wed','thu','fri','sat','sun']
print(days[today.weekday()])