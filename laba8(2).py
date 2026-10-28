x = []
n = int(input("Введите количество строк"))
m = int(input("Введите количество столбцов"))
for i in range(n):
    y = []
    for j in range(m):
        el = int(input())
        y.append(el)
    x.append(y)

res1 = []
for d in range(m):
    nul = True
    for z in range(n):
        if x[d][z] != 0:
            nul = False
            break
    res1.append((nul))
print(res1)

res2 = []
for k in range(m):
    vozr = True
    for g in range(n -1):
        if x[g][k] >= x[g+1][k]:
            vozr = False
            break
    res2.append(vozr)
print(res2)

res3 = []
for h in range(n):
    nstr = x[h]
    sim = True
    for f in range(m // 2):
        if nstr[f] != nstr[m - 1 -f]:
            sim = False
            break
    res3.append(sim)
print(res3)

S = int(input("Введите число S"))
res4 = True
for o in range(n):
    sstr = 0
    for e in range(m):
        sstr += x[o][e]
    if sstr >= S:
        res4 = False
        break
print(res4)

