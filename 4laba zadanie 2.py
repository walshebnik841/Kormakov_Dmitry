P = 1
for n in range(1,21,1):
    P = P * ((2**-(n/2)+ n ** 3.2 + 1)/(n**3 + 2*n**2+3 ))
print(P)
