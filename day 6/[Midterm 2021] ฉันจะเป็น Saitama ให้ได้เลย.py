"""Saitama"""
from math import ceil

def check(pushw, sitw, squaw, runw):
    """-"""
    if pushw > sitw and pushw > squaw and pushw > runw:
        return pushw
    elif sitw > pushw and sitw > squaw and sitw > runw:
        return sitw
    elif squaw > pushw and squaw > sitw and squaw > runw:
        return squaw
    else:
        return runw

def training():
    """-"""
    push = int(input())
    situp = int(input())
    squart = int(input())
    running = int(input())

    pushd = int(input())
    situpd = int(input())
    rund = int(input())
    squartd = int(input())

    pushw = ceil(push / pushd)
    situpw = ceil(situp / situpd)
    squartw = ceil(squart / squartd)
    runw = ceil(running / rund)

    day = check(pushw, situpw, squartw, runw)
    return day

print(training())
