x = []

dl = 1

n = int(input('Введите количество чисел в массиве:'))
for i in range(n):
    x.append(int(input()))
k = 0
while (k<len(x)):
    mx = 1
    for i in range(k,len(x)-1):
        if x[i] < x[i+1]:
            mx += 1
        else :
            break
    if mx > dl:
        dl = mx
    k+=1
print(dl)
