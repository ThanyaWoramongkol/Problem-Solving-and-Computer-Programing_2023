"""SecondConverter"""

def timing(sec, second, minute, hour):
    """----want, 1 min have, 1 hour have, 1 day have"""
    second_out = sec % second
    minute_out = sec // second
    hour_out = minute_out // minute
    minute_out = minute_out % minute
    hour_out = hour_out % hour
    print("%d:%d:%d" % (hour_out, minute_out, second_out))
timing(int(input()), int(input()), int(input()), int(input()))
