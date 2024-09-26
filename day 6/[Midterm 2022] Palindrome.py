"""Palindrome"""
def main(count, time):
    """-"""
    number = ''
    nub = 0

    hour = int(time[0:time.index(':')])
    natee = int(time[time.index(':')+1:])
    while True:
        natee += 1
        if nub == count:
            break

        if natee > 59:
            natee = 0
            hour += 1
        if hour > 23:
            hour = 0
        number = str(hour) + "%02d" % natee

        if number == number[::-1]:
            if len(number) == 3:
                print(number[0] + ":" + number[1:])
            else:
                print(number[0:2] + ":" + number[2:])
            nub += 1

main(int(input()), input())
