import math
import os

def f_ot(o0, a, b, ea, eb, t):
    return a * o0 ** ea * math.exp(b * o0 ** eb * t) + (o0 - a * o0 ** ea)


def f_gen_ts(list_ts, params):
    a, b, ea, eb = params
    o0 = list_ts[0]
    list_gen_ts = []
    for t in range(len(list_ts)):
        list_gen_ts.append(f_ot(o0, a, b, ea, eb, t))
    return list_gen_ts


def f_mape(list_ts, list_gen_ts):
    #mean absolute percentage error
    mape = 0
    for t in range(len(list_ts)):
        mape += abs((list_ts[t] - list_gen_ts[t]) / list_ts[t])
    return mape / len(list_ts)


def f_list_ts(file_name):
    file = open(os.path.realpath(rf'modekls\time_serie\{file_name}.txt'), 'r').read()
    ts = []
    for ot in file.split('\n'):
        ts.append(float(ot))
    return ts


list_file_names = ['ars1', 'ars2', 'ars3', 'ars4', 'fle1', 'fle2', 'fle3', 'fle4', 'gil1', 'gil2', 'gil3', 'gri1', 'gri2', 'gri3', 'gri4', 'hull1', 'hull2', 'pre1', 'pre2', 'pre3', 'pre4', 'rea1', 'rea2', 'rea3', 'rea4', 'shrew1', 'shrew2', 'shrew3', 'shrew4', 'tot1', 'tot2', 'tot3', 'tot4']
list_results = []


for a in range(0, 100, 5):
    a /= 100
    print(a)
    for b in range(0, 100, 5):
        b /= 1000
        for ea in range(0, 20):
            ea /= 10
            for eb in range(0, 20):
                eb /= 10
                mape_score = 0
                for file_name in list_file_names:
                    if 'The Devils' not in file_name:
                        list_ts = f_list_ts(file_name)
                        mape_score += f_mape(list_ts[:30], f_gen_ts(list_ts, [a, b, ea, eb])[:30])
                list_results.append([mape_score, [a, b, ea, eb]])

list_results.sort(key= lambda x: x[0], reverse=False)
for i in range(10):
    print(list_results[i])



