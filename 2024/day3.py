inp = open("d3.txt", "r")

state = 1

r1 = 0
r2 = 0

for line in inp:
    i = 0
    while i < len(line):
        if line[i:i+4] == "do()":
            state = True
        if line[i: i + 7] == "don't()":
            state = False
        if line[i:i+4] == "mul(":
            i = i + 4
            a = ''
            while 48 <= ord(line[i]) <= 57:
                a = a + line[i]
                i = i + 1
            if line[i] == ",":
                i = i + 1
                b = ""
                while 48 <= ord(line[i]) <= 57:
                    b = b + line[i]
                    i = i + 1
                if line[i] == ')':
                    r1 += int(a) * int(b)
                    r2 += int(a) * int(b) * state
                    i = i + 1
                else:
                    a = ''
                    b = ''
                    i = i + 1
            else:
                a = ''
                b = ''
                i = i + 1
        else:
            i = i + 1

print(r1, r2)
