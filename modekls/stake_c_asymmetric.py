import math
import numpy as np

def f_ou2(ou1, m, t):
    return m * t + ou1


def f_oo2(oo1, a, b, t):
    return a * math.exp(b * t) + (oo1 - a)


def f_list_si(list_oi, list_ou2n, ou1, co_m, co_c, r):
    if len(list_oi) == 1:
        return [(1 + co_c - co_m * ou1 / list_ou2n[0]) / (list_oi[0] - 1)]
    else:
        list_a = []
        list_b = []
        for i in range(len(list_oi)):
            list_b.append(r + 1 + co_c - co_m * ou1 / list_ou2n[i])
            list_inner = []
            for j in range(len(list_oi) - 1):
                list_inner.append(-1)
            list_a.append(list_inner)
        for i in range(len(list_oi)):
            list_a[i].insert(i, (list_oi[i] - 1))
        a = np.array(list_a)
        b = np.array(list_b)
        return list(np.linalg.solve(a, b))

    
def f_r_in(sn, oin, s, ou1, ou2, co_m, co_c):
    return sn * oin - s + co_m * ou1 / ou2 - (1 + co_c)


def f_r_over(ou1, oo2, s):
    return ou1 / oo2 * (oo2 - 1) - (1 + s)


def f_r_under(ou1, oo2, s):
    return (ou1 - 1) - (ou1 / oo2 + s)


def f_be_ou2n(sn, oin, s, ou1, co_m, co_c):
    return (co_m * ou1) / (1 + co_c + s - sn * oin)


def f_be_oo2(ou1, s):
    return (1 + s) / (ou1 - 1 - s) + 1


line_05, line_15, line_25 = [[0.5, 19.0, 1.04], [1.5, 5.1, 1.214], [2.5, 2.4, 1.667]]
list_insurance_odds = [5, 5.5, 6.5]

adapt_k = 1
a = 0.3 * adapt_k
b = 0.015 * adapt_k
m = -0.013 * adapt_k

co_m = 0.9
co_c = 0.1

list_results = []

for n in range(len(list_insurance_odds)):
    list_oi = list_insurance_odds[:n + 1]
    list_ou2n_15 = []
    list_ou2n_25 = []
    for t in range(len(list_oi)):
        t *= 10
        list_ou2n_15.append(f_ou2(line_05[1], m, t))
        list_ou2n_25.append(f_ou2(line_15[1], m, t))
    oo2_15 = f_oo2(line_15[2], a, b, t + 10)
    oo2_25 = f_oo2(line_25[2], a, b, t + 10)

    list_si_15 = f_list_si(list_oi, list_ou2n_15, line_15[1], co_m, co_c, 0)
    list_si_25 = f_list_si(list_oi, list_ou2n_25, line_25[1], co_m, co_c, 0)
    list_r_i_15 = []
    list_r_i_25 = []
    for i in range(len(list_oi)):
        list_r_i_15.append(f_r_in(list_si_15[i], list_oi[i], sum(list_si_15), line_15[1], list_ou2n_15[i], co_m, co_c))
        list_r_i_25.append(f_r_in(list_si_25[i], list_oi[i], sum(list_si_25), line_25[1], list_ou2n_25[i], co_m, co_c))
    
    r_under_15 = f_r_under(line_15[1], oo2_15, sum(list_si_15))
    r_over_15 = f_r_over(line_15[1], oo2_15, sum(list_si_15))
    r_under_25 = f_r_under(line_25[1], oo2_25, sum(list_si_25))
    r_over_25 = f_r_over(line_25[1], oo2_25, sum(list_si_25))

    list_results.append([r_under_15, r_over_15, list_r_i_15, oo2_15, 1.5, len(list_oi), list_si_15, list_ou2n_15, line_15, r_under_15 / (sum(list_si_15) + 1)])
    list_results.append([r_under_25, r_over_25, list_r_i_25, oo2_25, 2.5, len(list_oi), list_si_25, list_ou2n_25, line_25, r_under_25 / (sum(list_si_25) + 1)])

list_results.sort(key=lambda x: x[0], reverse=True)

list_best = list_results[0]
oo2 = list_best[3]
list_oi = list_insurance_odds[:list_best[5]]
list_ou2n = list_best[7]
line = list_best[8]

prob_insurance_co = 0.5
prob_over_under = 1 - prob_insurance_co

list_ev_r = []
for r in range(5, 20):
    r /= 100
    list_si_r = f_list_si(list_oi, list_ou2n, line[1], co_m, co_c, r)
    r_o = f_r_over(line[1], oo2, sum(list_si_r))
    r_u = f_r_under(line[1], oo2, sum(list_si_r))
    list_r_i_co = []
    for i in range(len(list_oi)):
        list_r_i_co.append(f_r_in(list_si_r[i], list_oi[i], sum(list_si_r), line[1], list_ou2n[i], co_m, co_c))
    ev = prob_insurance_co * r + prob_over_under * r_o
    list_ev_r.append([ev, r, list_r_i_co, r_o, r_u, list_si_r])
list_ev_r.sort(key=lambda x: x[0], reverse=True)
list_best_r = list_ev_r[0]

list_be_ou2n = []
for i in range(len(list_oi)):
    list_be_ou2n.append(f_be_ou2n(list_best_r[-1][i], list_oi[i], sum(list_best_r[-1]), line[1], co_m, co_c))
be_oo2 = f_be_oo2(line[1], sum(list_best_r[-1]))

print(f'Best bet: ev: {list_best_r[0]}, r_over_under: {list_best_r[3]}, r_insurance_co: {list_best_r[1]}, probability_insurance_co: {prob_insurance_co}\nline: {line}, list_oi: {list_oi}, list_si: {list_best_r[-1]}\nPredicted Odds: oo2: {oo2}, ou2n: {list_ou2n}\nNecessary odds, break even: oo2: {be_oo2}, ou2n: {list_be_ou2n}')