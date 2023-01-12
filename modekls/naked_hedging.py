import math

def f_ot(o0, a, b, ea, eb, t):
    return a * o0 ** ea * math.exp(b * o0 ** eb * t) + (o0 - a * o0 ** ea)


def f