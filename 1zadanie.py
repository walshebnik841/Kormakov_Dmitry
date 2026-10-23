x = []
y = []
for i in range(10):
    x.append(int(input()))
    if x[i] not in y:
        y.append(x[i])

print(y)
