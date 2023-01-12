import numpy as np
import scipy.optimize
import math

def f_list_si(x, list_oi):
    if len(list_oi) == 1:
        return [x/(list_oi[0] - 1)]
    else:
        list_a = []
        list_b = []
        for i in range(len(list_oi)):
            list_b.append(x)
            list_inner = []
            for j in range(len(list_oi) - 1):
                list_inner.append(-1)
            list_a.append(list_inner)
        for i in range(len(list_oi)):
            list_a[i].insert(i, (list_oi[i] - 1))
        a = np.array(list_a)
        b = np.array(list_b)
        return list(np.linalg.solve(a, b))


def f_list_si_asymmetry(list_oi, list_si):
    if len(list_oi) == 1:
        return list_si
    else:
        s1 = list_si[0] * list_oi[-1] / list_oi[0]
        def solve(r, *args):
            return args[0] - (args[1] * (1 - r**args[2]) / (1 - r))
        r = scipy.optimize.fsolve(solve, [0], (sum(list_si), s1, len(list_si)))[0]
        list_new_si = []
        for i in range(len(list_si)):
            list_new_si.append(s1 * r ** i)
        return list_new_si


def f_oo2(list_si, ou1):
    return (1 + sum(list_si)) / (ou1 - 1 - sum(list_si)) + 1


def f_ou2n(list_si, sn, ou1, oin):
    return (0.9 * ou1) / (1.1 + sum(list_si) - sn * oin)


def f_pd(olarger, o):
    return math.log(olarger / (olarger - 1)) - math.log(o / (o - 1))


def f_conditions(ou1, list_si, list_oi):
    check_sum = 0
    if ou1 - 1 - sum(list_si) > 0:
        check_sum += 1
    for i in range(len(list_si)):
        if 1.1 + sum(list_si) - list_si[i] * list_oi[i] > 0 and list_si[i] > 0:
            check_sum += 1
    if check_sum == len(list_si) + 1:
        return True
    else:
        return False


def f_obj(oo1, oo2, ou1, list_ou2n, beta):
    pd_o = -beta * f_pd(oo1, oo2) / len(list_ou2n)
    pd_sum = pd_o
    for i in range(len(list_ou2n)):
        pd_sum += f_pd(list_ou2n[i], ou1) / (i + 1)
    pd_sum /= len(list_ou2n)
    return pd_sum, pd_sum - pd_o, -pd_o


'''
Lyon
list_lines = [[1.5, 4.6, 1.25], [2.5, 2.25, 1.79], [3.5, 1.5, 2.75], [4.5, 1.18, 5.9], [5.5, 1.063, 13], [6.5, 1.015, 29], [7.5, 1.004, 61]]
list_insurance_odds = [4.33, 5, 6, 7.5, 8, 13, 17, 21, 21]
CPFC
list_lines = [[1.5, 3, 1.44], [2.5, 1.69, 2.38], [3.5, 1.25, 4.4], [4.5, 1.08, 9.8], [5.5, 1.02, 23], [6.5, 1.004, 61], [7.5, 1.002, 151]]
list_insurance_odds = [5, 5.5, 6.5, 7.5, 8, 12, 15, 17, 17]
'''

list_results = []
list_lines = [[1.5, 3, 1.44], [2.5, 1.69, 2.38], [3.5, 1.25, 4.4], [4.5, 1.08, 9.8], [5.5, 1.02, 23], [6.5, 1.004, 61], [7.5, 1.002, 151]]
list_insurance_odds = [5, 5.5, 6.5, 7.5, 8, 12, 15, 17, 17]
list_x = []
for i in range(5, 101, 5):
    list_x.append(i / 100)
for line, ou1, oo1 in list_lines:
    list_oi = []
    for oi in list_insurance_odds:
        list_oi.append(oi)
        for x in list_x:
            list_si = f_list_si_asymmetry(list_oi, f_list_si(x, list_oi))
            if f_conditions(ou1, list_si, list_oi):
                oo2 = f_oo2(list_si, ou1)
                list_ou2n = []
                for i in range(len(list_si)):
                    list_ou2n.append(f_ou2n(list_si, list_si[i], ou1, list_oi[i]))
                try:
                    pd, pd_u, pd_o = f_obj(oo1, oo2, ou1, list_ou2n, 1)
                    list_results.append([pd, pd_u, pd_o, line, list_oi, x, ou1, oo1, list_si, sum(list_si), list_ou2n])
                except:
                    pass  
            else:
                pass

print('')

list_final = []
for inner in list_results:
    if f_conditions(inner[6], inner[8], inner[4]):
        list_final.append(inner)

list_final.sort(key=lambda x: x[0], reverse=True)
pd, pd_u, pd_o, line, list_oi, x, ou1, oo1, list_si, sum_si, list_ou2n = list_final[0]
print(pd, line, ou1, oo1, x, sum_si, list_si, list_oi[:len(list_si)])
print(f_pd(oo1, oo2) / len(list_ou2n))
for i in range(len(list_ou2n)):
    print(list_ou2n[i], ou1)
    print(f_pd(list_ou2n[i], ou1) / (i + 1))