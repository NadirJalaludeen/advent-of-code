import numpy as np

file = open("day5.txt", "r")

def verify(l, iix = False):
    for i in range(len(l) - 1):
        for j in range(i + 1, len(l)):
            if l[i] in dep and l[j] not in dep[l[i]]:
                if iix:
                    return i, j
                return False
    return True

def fix(x):
    new = x
    while not verify(new):
        i, j = verify(new, iix = True)
        new[i], new[j] = new[j], new[i]
    return new

pages = []
dep = {}

for line in file:
    if "|" in line:
        a = line[:line.find("|")]
        b = line[line.find("|") + 1:]
        if int(a) not in dep:
            dep[int(a)] = [int(b)]
        else:
            dep[int(a)].append(int(b))
    if "," in line:
        a = [int(i) for i in line.split(",")]
        pages.append(a)

print(np.sum([x[len(x)//2] for x in pages if verify(x)]))

print(np.sum([fix(x)[len(x)//2] for x in pages if not verify(x)]))
