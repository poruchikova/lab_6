from typing import Any

import numpy
import pandas as pd


# набор данных
s = pd.Series(
    data=['1', 2, 3.1, 'hi!', 5, -512, 12.42, 'zero', 10.10, 98],
    index=range(6, 26, 2)
)


# 1 номер
s2 = pd.Series(
    data=s.values,
    index=range(2, 12, 1)
)
print('1)', s2, sep='\n')


# 2 номер
RES_FILE = './res.txt'


def save_result(result: Any):
    with open(RES_FILE, mode='w') as fw:
        fw.write(str(result))


if type(s2[3]) in [float, int] and type(s2[5]) in [float, int]:
    res = s2[3] + s2[5]
    save_result(res)
    print(f'2) res={res}')
else:
    print('2) cannot be calculated')


# 3 номер
values = [v for v in s.values if isinstance(v, int)]
desp = round(float(numpy.var(values, ddof=0)), 2)
print(f'3) desp={desp}')


# Ответы
# 3) Ответ: не может быть определен
# 4) Ответ: 57591.19
