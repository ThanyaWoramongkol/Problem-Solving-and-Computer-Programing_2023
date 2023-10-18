"""_"""
 
def main(time):
    """_"""
    days = time // 86400
    hours = (time - (days * 86400)) // 3600
    minutes = (time - ((hours * 3600) + (days * 86400))) // 60
    seconds = (time - ((hours * 3600) + (days * 86400) + (minutes * 60)))
    print(days, hours, minutes, seconds)
main(int(input()))
