class Clock:
    def __init__(self,hour,minute):
        hour = abs(hour)
        if hour>23:
            hour = hour%24
        if minute>59:
            minute = minute%60
        minute = abs(minute)
        self.hour = hour
        self.minute = minute
    def __str__(self):
        if len(self.hour<2):
            military_hour = "0" + self.hour
        if len(self.minute<2):
            military_minute = "0" + self.minute
        military_time = military_hour + military_minute
    def add(self, other):



