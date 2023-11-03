import numpy as np
import pandas as pd
def df_sum_int(x):
    res = 0
    for i in df.index:
        for j in df.columns:
            if isinstance(df.loc[i, j], np.int64 | np.float64):
                res += df.loc[i, j]
    return res

dct = {'Товар':['A', 'B', 'C', 'D', 'E'],
       'Шт':[10,20,30,40,50],
       'Цена':[100,50,30,20,5]}
df = pd.DataFrame(dct)
print(df_sum_int(df))

import numpy as np
import pandas as pd
def df_sum_int(x):
    res = 0
    for i in df.index:
        for j in df.columns:
            print(df.loc[i,j])
    # return res

dct = {'Товар':['A', 'B', 'C', 'D', 'E'],
       'Шт':[10,20,30,40,50],
       'Цена':[100,50,30,20,5]}
df = pd.DataFrame(dct)
print(df_sum_int(df))