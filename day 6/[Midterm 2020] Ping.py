"""[Midterm 2020] Ping"""

def protocol(statis):
    """-"""
    if "[" in statis[2]:
        http = statis[2]
        https = http[http.index('[')+1:http.index(']')]
    else:
        http = statis[0]
        https = http[http.index('ping ') + 5:]
    return https

def loss(lost):
    """%"""
    if lost >= 4:
        percent = "100%"
    elif lost >= 3:
        percent = "75%"
    elif lost >= 2:
        percent = "50%"
    elif lost >= 1:
        percent = "25%"
    else:
        percent = "0%"
    return percent

def timer(statis):
    """-"""
    count = 1
    broke = 0
    for i in statis[3:]:
        if ":" in i:
            if "<1" in i:
                time = 0
            else:
                time = i[i.index("time")+5:i.index("ms")]
        else:
            time = -1 - broke
            broke += 1

        if count == 1:
            time1 = int(time)
        elif count == 2:
            time2 = int(time)
        elif count == 3:
            time3 = int(time)
        else:
            time4 = int(time)
        count += 1
    timing = [time1, time2, time3, time4]
    for _ in range(len(timing)):
        for i in timing:
            if i <= -1:
                timing.remove(i)
                break
    return timing

def ping(statis):
    """-"""
    timing = []
    receive = 0
    lost = 0
    printf = 1
    https = protocol(statis)
    for i in statis[3:]:
        if 'Reply' in i:
            receive += 1
        else:
            lost += 1

    timing = timer(statis)
    percent = loss(lost)
    if lost == 4:
        printf = 0

    print("Ping statistics for %s:" % https)
    print("    Packets: Sent = 4, Received = %d, Lost = %d (%s loss)," \
    % (receive, lost, percent))
    if printf:
        print("Approximate round trip times in milli-seconds:")
        print("    Minimum = %dms, Maximum = %dms, Average = %dms" \
    % (min(timing), max(timing), sum(timing) / len(timing)))
ping([input() for _ in range(7)])
