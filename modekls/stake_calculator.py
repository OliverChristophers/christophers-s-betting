import math

def f_ou2(ou1, m, t):
    return m * t + ou1


def f_oo2(oo1, a, b, t):
    return a * math.exp(b * t) + (oo1 - a)


def f_sn(oo2, ou1, ou2n, oin, co_m, co_c):
    return (co_c + ou1 * (1 - 1 / oo2 - co_m / ou2n)) / oin


def f_r(ou1, oo2, s):
    return ou1 * (1 - 1 / oo2) - (1 + s)


def f_r_over(ou1, oo2, s):
    return ou1 / oo2 * (oo2 - 1) - (1 + s)


def f_r_under(ou1, oo2, s):
    return (ou1 - 1) - (ou1 / oo2 + s)


def f_r_in(sn, oin, s, ou1, ou2, co_m, co_c):
    return sn * oin - s + co_m * ou1 / ou2 - (1 + co_c)


line_05, line_15, line_25 = [[0.5, 19.0, 1.04], [1.5, 5.1, 1.214], [2.5, 2.4, 1.667]]
list_insurance_odds = [5, 5.5, 6.5]

adapt_k = 1
a = 0.3 * adapt_k
b = 0.015 * adapt_k
m = -0.013 * adapt_k

co_m = 0.9
co_c = 0.1

list_ou2_line_15 = []
list_oo2_line_15 = []
list_ou2_line_25 = []
list_oo2_line_25 = []

for t in range(len(list_insurance_odds)):
    t *= 10
    list_ou2_line_15.append(f_ou2(line_05[1], m, t))
    list_oo2_line_15.append(f_oo2(line_15[2], a, b, t + 10))
    list_ou2_line_25.append(f_ou2(line_15[1], m, t))
    list_oo2_line_25.append(f_oo2(line_25[2], a, b, t + 10))

list_results = []
    
for n in range(len(list_insurance_odds)): 
    list_oi = list_insurance_odds[:n+1]
    list_sn_line_15 = []
    list_sn_line_25 = []
    for i in range(len(list_oi)):
        oin = list_oi[i]
        list_sn_line_15.append(f_sn(list_oo2_line_15[i], line_15[1], list_ou2_line_15[i], oin, co_m, co_c))
        list_sn_line_25.append(f_sn(list_oo2_line_25[i], line_25[1], list_ou2_line_25[i], oin, co_m, co_c))
    r_line_15 = f_r(line_15[1], list_oo2_line_15[n], sum(list_sn_line_15))
    r_line_25 = f_r(line_25[1], list_oo2_line_25[n], sum(list_sn_line_25))
    list_results.append([r_line_15, 1.5, len(list_oi), list_sn_line_15])
    list_results.append([r_line_25, 2.5, len(list_oi), list_sn_line_25])

list_results.sort(key=lambda x: x[0], reverse=True)
for list_r in list_results:
    print(list_r)
    if list_r[1] == 1.5:
        ou1 = line_15[1]
        oo2 = list_oo2_line_15[len(list_r[-1]) - 1]
        ou2 = list_ou2_line_15[len(list_r[-1]) - 1]
    else:
        ou1 = line_25[1]
        oo2 = list_oo2_line_25[len(list_r[-1]) - 1]
        ou2 = list_ou2_line_25[len(list_r[-1]) - 1]
    print(f_r_over(ou1, oo2, sum(list_r[-1])))
    print(f_r_under(ou1, oo2, sum(list_r[-1])))
    for i in range(list_r[2]):
        print(f_r_in(list_r[-1][i], list_insurance_odds[i], sum(list_r[-1]), ou1, ou2, co_m, co_c))
    print('')