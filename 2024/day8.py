import numpy as np

file = open("day8.txt", "r")

inp = []
for line in file:
    if line[-1] == '\n':
        inp.append(list(line[:-1]))
    else:
        inp.append(list(line))

inp = np.array(inp)

#Part 1

antinodes = np.zeros(np.shape(inp))

for f in np.unique(inp):
    if f == ".":
        continue
    else:
        posI, posJ = np.where(inp == f)
        for x in range(len(posI)):
            for y in range(x + 1, len(posI)):
                dI = abs(posI[x] - posI[y])
                dJ = abs(posJ[x] - posJ[y])
                
                if posI[x] < posI[y]:
                    if posJ[x] < posJ[y]:
                        if 0 <= posI[x] - dI and 0 <= posJ[x] - dJ:
                            antinodes[posI[x] - dI, posJ[x] - dJ] += 1

                        if posI[y] + dI < len(inp) and posJ[y] + dJ < len(inp[0]):
                            antinodes[posI[y] + dI, posJ[y] + dJ] += 1
                            
                    else:
                        if 0 <= posI[x] - dI and posJ[x] + dJ < len(inp[0]):
                            antinodes[posI[x] - dI, posJ[x] + dJ] += 1

                        if posI[y] + dI < len(inp) and 0 <= posJ[y] - dJ:
                            antinodes[posI[y] + dI, posJ[y] - dJ] += 1
                            
                else:
                    if posJ[x] < posJ[y]:
                        if posI[x] + dI < len(inp) and 0 <= posJ[x] - dJ:
                            antinodes[posI[x] + dI, posJ[x] - dJ] += 1

                        if 0 <= posI[y] - dI and posJ[y] + dJ < len(inp[0]):
                            antinodes[posI[y] - dI, posJ[y] + dJ] += 1
                            
                    else:
                        if 0 <= posI[y] - dI and 0 <= posJ[y] - dJ:
                            antinodes[posI[y] - dI, posJ[y] - dJ] += 1

                        if posI[x] + dI < len(inp) and posJ[x] + dJ < len(inp[0]):
                            antinodes[posI[x] + dI, posJ[x] + dJ] += 1
                            
print(np.sum(antinodes != 0))


#Part 2

antinodes = np.zeros(np.shape(inp))

for f in np.unique(inp):
    if f == ".":
        continue
    else:
        posI, posJ = np.where(inp == f)
        for x in range(len(posI)):
            for y in range(x + 1, len(posI)):
                dI = abs(posI[x] - posI[y])
                dJ = abs(posJ[x] - posJ[y])
                
                if posI[x] < posI[y]:
                    if posJ[x] < posJ[y]:
                        o = 0
                        while 0 <= posI[x] - o * dI and 0 <= posJ[x] - o * dJ:
                            antinodes[posI[x] - o * dI, posJ[x] - o * dJ] += 1
                            o = o + 1

                        p = 0
                        while posI[y] + p * dI < len(inp) and posJ[y] + p * dJ < len(inp[0]):
                            antinodes[posI[y] + p * dI, posJ[y] + p * dJ] += 1
                            p = p + 1
                            
                    else:
                        o = 0
                        while 0 <= posI[x] - o * dI and posJ[x] + o * dJ < len(inp[0]):
                            antinodes[posI[x] - o * dI, posJ[x] + o * dJ] += 1
                            o = o + 1

                        p = 0
                        while posI[y] + p * dI < len(inp) and 0 <= posJ[y] - p * dJ:
                            antinodes[posI[y] + p * dI, posJ[y] - p * dJ] += 1
                            p = p + 1
                            
                else:
                    if posJ[x] < posJ[y]:
                        o = 0
                        while posI[x] + o * dI < len(inp) and 0 <= posJ[x] - o * dJ:
                            antinodes[posI[x] + o * dI, posJ[x] - o * dJ] += 1
                            o = o + 1

                        p = 0
                        while 0 <= posI[y] - p * dI and posJ[y] + p * dJ < len(inp[0]):
                            antinodes[posI[y] - p * dI, posJ[y] + p * dJ] += 1
                            p = p + 1
                            
                    else:
                        o = 0
                        while 0 <= posI[y] - o * dI and 0 <= posJ[y] - o * dJ:
                            antinodes[posI[y] - o * dI, posJ[y] - o * dJ] += 1
                            o = o + 1

                        p = 0
                        while posI[x] + p * dI < len(inp) and posJ[x] + p * dJ < len(inp[0]):
                            antinodes[posI[x] + p * dI, posJ[x] + p * dJ] += 1
                            p = p + 1
                            
print(np.sum(antinodes != 0))
