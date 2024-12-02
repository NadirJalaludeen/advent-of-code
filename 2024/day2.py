import numpy as np
import pandas as pd

inp = np.array(pd.read_csv("day2.txt", header=None, sep = " "))

r1 = 0
r2 = 0


for i in inp:
    i = i[np.logical_not(np.isnan(i))]
    d = i[1:] - i[:-1]
    
    if (not False in ((1 <= d) & (d <= 3))) or (not False in ((-3 <= d) & (d <= -1))):
        r1 += 1
    else:
        for k in range(len(i)):
            ik = np.concatenate((i[:k], i[k+1:]))
            ik = ik
            d = ik[1:] - ik[:-1]
            
            if (not False in ((1 <= d) & (d <= 3))) or (not False in ((-3 <= d) & (d <= -1))):
                r2 += 1
                break

print(r1, r1 + r2)
