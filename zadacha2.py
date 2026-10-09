N = int(input("Введте целое чсло"))
P = 1
kol = 0
for i in range(1, N+1):
    a = int(input())
    if i>=3 and i%3 == 0:
        if a > 0 or a <0:
            kol+=1
            P = P * a
if kol > 2:
    print(P)

