import numpy as np
import pandas as pd

inp = pd.read_csv("day1.txt", sep = ' ', header = None)

col1 = np.array(inp)[:,0]
col2 = np.array(inp)[:,3]
col1.sort()
col2.sort()

print(np.sum(np.abs(col1 - col2)))

col2u, col2uc = np.unique(col2, return_counts=True)
dic = {col2u[i]:col2uc[i] for i in range(len(col2u))}

res = 0
for i in col1:
    if i in dic:
        res += i * dic[i]

print(res)
