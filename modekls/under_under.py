import math
import random
import numpy as np

#can also use exponential (inverse poisson) to see prob of having to wait t mins for first goal

def f_odds_over_t(o0, a, b, ea, eb, t):
    return a * o0 ** ea * math.exp(b * o0 ** eb * t) + (o0 - a * o0 ** ea)


def f_hedge_stake(su, ou, oo):
    return su * ou / oo


def f_goal_minute(pgm):
    return random.random() <= pgm


def f_minute_process(t, t_exe, g, l_ot, su, ou, pgm, oo, so):
    if t == t_exe and g == 0:
        o0, a, b, ea, eb = l_ot
        oo = f_odds_over_t(o0, a, b, ea, eb, t)
        so = f_hedge_stake(su, ou, oo)
    if f_goal_minute(pgm):
        g += 1
    return [g, oo, so]


def f_return(su, ou, so, oo, l, g):
    if g < l:
        return su * (ou - 1) - so
    else:
        return so * (oo - 1) - su


goal_expectancy = 3
minutes_expectancy = 90
pgm = goal_expectancy / minutes_expectancy

params = [0.1, 0.055, 1.7, 0]
a, b, ea, eb = params
line = [3.5, 1.61, 2.5]
l, ou, o0 = line
l_ot = [o0, a, b, ea, eb]
su = 1

list_outcome = []
for t_exe in range(minutes_expectancy):
    list_returns = []
    for i in range(1000):
        g, oo, so = [0, 0, 0]
        for t in range(minutes_expectancy):
            g, oo, so = f_minute_process(t, t_exe, g, l_ot, su, ou, pgm, oo, so)
        list_returns.append(f_return(su, ou, so, oo, l, g))
    list_outcome.append(np.mean(list_returns))
for i in list_outcome:
    print(i)