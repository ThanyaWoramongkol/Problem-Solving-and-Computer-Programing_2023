"""_"""

def main(time):
    """_"""
    if time >= 864000000:
        print("ERR_:__:__:__")
    else:
        days = time // 86400
        hours = (time - (days * 86400)) // 3600
        minutes = (time - ((hours * 3600) + (days * 86400))) // 60
        seconds = (time - ((hours * 3600) + (days * 86400) + (minutes * 60)))
        print("%04d:%02d:%02d:%02d" % (days, hours, minutes, seconds))
main(int(input()))
