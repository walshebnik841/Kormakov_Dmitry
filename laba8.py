x = []
s = 0

m = int(input("Введите число м"))
N = int(input("Введите количество значений в масиве"))
for i in range(N):
    print("число номер ", i + 1  )
    x.append(int(input()))
for j in range(m):
    s += x[j]
maxS = s
for d in range(m , N):
    s = s +x[d] - x[d - m]
    if s > maxS:
        maxS = s
print("Максимальная сумма:", maxS)

