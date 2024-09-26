"""Niwarn World"""
import math

def funx(var_n):
    """xn"""
    return 2 + (math.log(var_n ** 2, 2) / \
    ((2 * var_n) * (math.log(var_n, 2))))

def funy(var_n, var_s):
    """yns"""
    return (math.sin(math.radians(30)) + \
    math.sqrt(2 * var_s)) / (funx(var_n) + 3)

def funz(var_k):
    """zk"""
    return (funy(var_k, var_k) ** 2) + (8456 * \
    (funx(var_k)) ** 4) / (24 * var_k)

def main(var_n, var_s, var_k):
    """-"""
    ansx = funx(var_n)
    ansy = funy(var_n, var_s)
    ansz = funz(var_k)

    print("X: %.1f, Y: %.1f, Z: %.1f" % (ansx, ansy, ansz))
main(float(input()), float(input()), float(input()))
