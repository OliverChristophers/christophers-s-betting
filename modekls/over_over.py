import math
import numpy as np


def f_oo2(o0, a, b, ea, eb, t):
    return a * o0 ** ea * math.exp(b * o0 ** eb * t) + (o0 - a * o0 ** ea)


def f_list_si(list_oi, list_oo2n, ou1, r):
    if len(list_oi) == 1:
        return [(r + ou1 + list_oo2n[0] - ou1 * list_oo2n[0]) / (list_oi[0] - list_oo2n[0])]
    else:
        list_a = []
        list_b = []
        for i in range(len(list_oi)):
            list_b.append(r + ou1 + list_oo2n[i] - ou1 * list_oo2n[i])
            list_inner = []
            for j in range(len(list_oi)):
                list_inner.append(-list_oo2n[i])
            list_inner[i] += list_oi[i]
            list_a.append(list_inner)
        a = np.array(list_a)
        b = np.array(list_b)
        return list(np.linalg.solve(a, b))


def f_necessary_oo2(ou1, s):
    return (1 + s) / (ou1 - 1 - s) + 1


def f_r_over(ou1, oo2, s):
    return ou1 / oo2 * (oo2 - 1) - (1 + s)


def f_r_under(ou1, oo2, s):
    return (ou1 - 1) - (ou1 / oo2 + s)


def f_r_insurance_over(sn, s, oin, ou1, oo2n):
    return sn * oin + (ou1 - 1 - s) * (oo2n - 1) - (1 + s)


line_05, line_15, line_25 = [[2.5, 1.78, 2.16], [3.5, 1.29, 4.33], [4.5, 1.1, 10]]
list_insurance_odds = [5, 5.5, 6.5]


a = 0.1
b = 0.055
ea = 1.7
eb = 0

r = 0

list_results = []

for n in range(len(list_insurance_odds)):
    list_oi = list_insurance_odds[:n + 1]
    list_oo2n_15 = []
    list_oo2n_25 = []
    for t in range(len(list_oi)):
        t *= 10
        list_oo2n_15.append(f_oo2(line_05[2], a, b, ea, eb, t))
        list_oo2n_25.append(f_oo2(line_15[2], a, b, ea, eb, t))
    list_si_15 = f_list_si(list_oi, list_oo2n_15, line_15[1], r)
    list_si_25 = f_list_si(list_oi, list_oo2n_25, line_25[1], r)
    necessary_oo2_15 = f_necessary_oo2(line_15[1], sum(list_si_15))
    necessary_oo2_25 = f_necessary_oo2(line_25[1], sum(list_si_25))
    projected_oo2_15 = f_oo2(line_15[2], a, b, ea, eb, 10 * len(list_oi))
    projected_oo2_25 = f_oo2(line_25[2], a, b, ea, eb, 10 * len(list_oi))
    r_over_15 = f_r_over(line_15[1], projected_oo2_15, sum(list_si_15))
    r_under_15 = f_r_under(line_15[1], projected_oo2_15, sum(list_si_15))
    r_over_25 = f_r_over(line_25[1], projected_oo2_25, sum(list_si_25))
    r_under_25 = f_r_under(line_25[1], projected_oo2_25, sum(list_si_25))
    list_r_insurance_over_15 = []
    list_r_insurance_over_25 = []
    for n in range(len(list_oi)):
        list_r_insurance_over_15.append(f_r_insurance_over(list_si_15[n], sum(list_si_15), list_oi[n], line_15[1], list_oo2n_15[n]))
        list_r_insurance_over_25.append(f_r_insurance_over(list_si_25[n], sum(list_si_25), list_oi[n], line_25[1], list_oo2n_25[n]))
    list_results.append([r_under_15, line_15, [necessary_oo2_15, projected_oo2_15], list_oo2n_15, list_si_15])
    list_results.append([r_under_25, line_25, [necessary_oo2_25, projected_oo2_25], list_oo2n_25, list_si_25])

list_results.sort(key=lambda x: x[0], reverse=True)
for list_r in list_results:
    if list_r[2][0] > 0 and sum(list_r[-1]) > 0:
        print(list_r)
        print()