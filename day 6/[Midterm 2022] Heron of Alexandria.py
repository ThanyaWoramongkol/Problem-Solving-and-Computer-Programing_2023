"""Heron of Alexandria"""

def math(var_a, var_b, var_c):
    """-"""
    var_s = (var_a + var_b + var_c) / 2
    answer = (var_s * (var_s - var_a) * (var_s - var_b) * \
    (var_s - var_c)) ** 0.5
    print("%.3f" % answer)
math(float(input()), float(input()), float(input()))
