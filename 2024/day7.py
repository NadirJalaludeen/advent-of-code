import re

inp = [[int(x) for x in re.split(': | ', line)] for line in open("day7.txt", 'r')]

def every(tab, x, part = False):
    if len(tab) == 1:
        if part: return {x + tab[0], x * tab[0], int(str(x) + str(tab[0]))}
        else: return {x + tab[0], x * tab[0]}
    else:
        if part: return every(tab[1:], x + tab[0], part = True) | every(tab[1:], x * tab[0], part = True) | every(tab[1:], int(str(x) + str(tab[0])), part = True)
        else: return every(tab[1:], x + tab[0]) | every(tab[1:], x * tab[0])

r1 = 0
r2 = 0

for l in inp:
    if l[0] in every(l[2:], l[1]):
        r1 += l[0]
    if l[0] in every(l[2:], l[1], part = True):
        r2 += l[0]

print(r1, r2)
