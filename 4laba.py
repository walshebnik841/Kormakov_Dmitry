import math
S = 0
for n in range(1,21,1):
    S = S + (((0.5**2*n)/(n**2 + n))*math.sin(n))
print(S)
