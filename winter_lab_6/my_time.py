class Time(object):

    hours = 0
    minutes = 0
    seconds = 0

    def __init__(self, hours=0, minutes=0, seconds=0):
        if (hours > 24 or hours < 0) or (minutes > 60 or minutes < 0) or (seconds > 60 or seconds < 0):
            return None
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def time_to_int(self):
        minutes = self.hours * 60 + self.minutes
        seconds = minutes * 60 + self.seconds
        return seconds

    @staticmethod
    def int_to_time(total_seconds):

        if total_seconds > 60:
            minutes, seconds = divmod(total_seconds, 60)

        if minutes > 60:
            hours, minutes = divmod(minutes, 60)

        return Time(hours, minutes, seconds)

    def mul_time(self, num):
        return Time.int_to_time(self.time_to_int() * num)


