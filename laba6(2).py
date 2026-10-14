a = str(input(''))
y = ''
for i in range(len(a)):
        if a[i] == ' ':
            y =  y + '_'
        else:
            y = y+ a[i]
print(y)





