a = int(input('Введите сторону а = '))
if a==0:
    print('Таких треугольников нет!')
    quit()
b = int(input('Введите сторону b = '))
if b==0:
    print('Таких треугольников нет!')
    quit()
c = int(input('Введите сторону c = '))
if c==0:
    print('Таких треугольников нет!')
    quit()
P = a+b+c
if a > b:
    Max = a
    Min = b
else:
    Max = b
    Min = a
if Max < c:
    Max = c
if Min > c:
    Min = c
if P > 20:
    print('Периметр = ', P, 'Max сторона = ', Max)
elif P < 10:
    print('Периметр = ', P, 'Min сторона = ', Min)
else:
    print('Периметр = ', P)