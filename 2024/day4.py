import numpy as np

inp_1 = open("day4.txt", "r")
inp = []
inp_d = []

search = "XMAS"

for line in inp_1:
    l = []
    for c in line:
        if c != "\n":
            l.append(c)
    inp.append(l)

def xmas(tab):
    i = 0
    for c in tab:
        if c == search[i%4]:
            i += 1
    return (''.join(tab)).count("XMAS")
    return i

inp = np.array(inp)
inp90 = np.rot90(inp)

for i in range(140+139):
    inp_d.append(np.diag(inp, k = i - 139))
    inp_d.append(np.diag(inp90, k = i - 139))

r = 0
for _ in range(4):
    inp = np.rot90(inp)
    for i in range(len(inp)):
        r += xmas(inp[i])

for i in range(len(inp_d)):
    r += xmas(inp_d[i])
    r += xmas(inp_d[i][::-1])

print(r)

r2 = 0

for i in range(len(inp) - 2):
    for j in range(len(inp) - 2):
        for _ in range(4):
            inp = np.rot90(inp)
            if inp[i + 0, j + 0] == 'M' and inp[i + 2, j + 0] == 'M' and inp[i + 0, j + 2] == 'S' and inp[i + 2, j + 2] == 'S' and inp[i + 1, j + 1] == 'A':
                r2 += 1

print(r2)
