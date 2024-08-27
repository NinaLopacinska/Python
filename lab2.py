# ZAD. 15
a = int(input("Podaj ilość współczunników wielomianu"))
wspolczynniki = []
for i in range(a):
    wspolczynniki.append(input('Podaj współczynnik: '))
wspolczynnikiFloat = [float(x) for x in wspolczynniki]
x = int(input('Podaj punkt na prostej liczb rzeczwylisych\n '))
suma = 0
p = 0
for y in wspolczynnikiFloat:
    suma = suma + y * pow(x, p)
    p = p + 1
print(suma)

# ZAD. 16
a = int(input('Podaj ilość współczynnika pierwszego wielomianu:  '))
wspolczynnik1 = []
for i in range(a):
    wspolczynnik1.append(input('Podaj współczynnik wielomianu 1:'))

b = int(input('Podaj ilość wsółczynnika drugiego wielomianu: '))
wspolczynnik2 = []
for i in range(b):
    wspolczynnik2.append(input('Podaj współczynnik wielomianu 2: '))
wspolczynnik1Float = [float(x) for x in wspolczynnik1]
wspolczynnik2Float = [float(x) for x in wspolczynnik2]
print('wielomian 1')
if a == 1:
    print(wspolczynnik1Float[0], end='')
elif a == 2:
    print(wspolczynnik2Float[0], end='')
    print('+', end='')
    print(wspolczynnik1Float[1], end='')
    print('x', end='')
else:
    print(wspolczynnik1Float[0], end='')
    print('+', end='')
    print(wspolczynnik1Float[1], end='')
    print('x', end='')
    pow = 2;
    for x in wspolczynnik1Float:
        index = wspolczynnik1Float.index(x);
        if index > 1:
            print('+', end='')
            print('x', end='')
            print('x^', end='')
            print(pow, end='')
            pow = pow + 1

print()
print('wielomian 2')
if b == 1:
    print(wspolczynnik2Float[0], end='')
elif b == 2:
    print(wspolczynnik2Float[0], end='')
    print('+', end='')
    print(wspolczynnik2Float[1], end='')
    print('x', end='')
else:
    print(wspolczynnik2Float[0], end='')
    print('+', end='')
    print(wspolczynnik2Float[1], end='')
    print('x', end='')
    pow = 2;
    for x in wspolczynnik2Float:
        index = wspolczynnik2Float.index(x);
        if index > 1:
            print('+', end='')
            print('x', end='')
            print('x^', end='')
            print(pow, end='')
            pow = pow + 1
print()

print('Suma wielomianów:')
if a > b:
    for x in range(0, len(wspolczynnik2Float)):
        wspolczynnik1Float[x] = wspolczynnik1Float[x] + wspolczynnik2Float[x]

if a == 1:
    print(wspolczynnik1Float[0], end='')
elif a == 2:
    print(wspolczynnik2Float[0], end='')
    print('+', end='')
    print(wspolczynnik1Float[1], end='')
    print('x', end='')
else:
    print(wspolczynnik1Float[0], end='')
    print('+', end='')
    print(wspolczynnik1Float[1], end='')
    print('x', end='')
    pow = 2;
    for x in wspolczynnik1Float:
        index = wspolczynnik1Float.index(x);
        if index > 1:
            print('+', end='')
            print('x', end='')
            print('x^', end='')
            print(pow, end='')
            pow = pow + 1
    else:
        for x in range(0, len(wspolczynnik1Float)):
            wspolczynnik2Float[x] = wspolczynnik2Float[x] + wspolczynnik1Float[x]

if b == 1:
    print(wspolczynnik2Float[0], end='')
elif b == 2:
    print(wspolczynnik2Float[0], end='')
    print('+', end='')
    print(wspolczynnik2Float[1], end='')
    print('x', end='')
else:
    print(wspolczynnik2Float[0], end='')
    print('+', end='')
    print(wspolczynnik2Float[1], end='')
    print('x', end='')
    pow = 2;
    for x in wspolczynnik2Float:
        index = wspolczynnik2Float.index(x);
        if index > 1:
            print('+', end='')
            print('x', end='')
            print('x^', end='')
            print(pow, end='')
            pow = pow + 1

            # ZAD 17
a = int(input('Podaj ilość współczynnika pierwszego wielomianu:  '))
wspolczynnik1 = []
for i in range(a):
    wspolczynnik1.append(input('Podaj współczynnik wielomianu 1:'))

b = int(input('Podaj ilość wsółczynnika drugiego wielomianu: '))
wspolczynnik2 = []
for i in range(b):
    wspolczynnik2.append(input('Podaj współczynnik wielomianu 2: '))
wspolczynnik1Float = [float(x) for x in wspolczynnik1]
wspolczynnik2Float = [float(x) for x in wspolczynnik2]
print('wielomian 1')
if a == 1:
    print(wspolczynnik1Float[0], end='')
elif a == 2:
    print(wspolczynnik1Float[0], end='')
    print('+', end='')
    print(wspolczynnik1Float[1], end='')
    print('x', end='')
else:
    print(wspolczynnik1Float[0], end='')
    print('+', end='')
    print(wspolczynnik1Float[1], end='')
    print('x', end='')
    pow = 2;
    for x in wspolczynnik1Float:
        index = wspolczynnik1Float.index(x);
        if index > 1:
            print('+', end='')
            print('x', end='')
            print('x^', end='')
            print(pow, end='')
            pow = pow + 1

print()
print('wielomian 2')
if b == 1:
    print(wspolczynnik2Float[0], end='')
elif b == 2:
    print(wspolczynnik2Float[0], end='')
    print('+', end='')
    print(wspolczynnik2Float[1], end='')
    print('x', end='')
else:
    print(wspolczynnik2Float[0], end='')
    print('+', end='')
    print(wspolczynnik2Float[1], end='')
    print('x', end='')
    pow = 2;
    for x in wspolczynnik2Float:
        index = wspolczynnik2Float.index(x);
        if index > 1:
            print('+', end='')
            print('x', end='')
            print('x^', end='')
            print(pow, end='')
            pow = pow + 1
print()

print('Różnica wielomianów:')
if a > b:
    for x in range(0, len(wspolczynnik2Float)):
        wspolczynnik1Float[x] = wspolczynnik1Float[x] - wspolczynnik2Float[x]
else:
    for x in range(0, len(wspolczynnik1Float)):
        wspolczynnik1Float[x] = wspolczynnik1Float[x] - wspolczynnik2Float[x]

if a == 1:
    print(wspolczynnik1Float[0], end='')
elif a == 2:
    print(wspolczynnik2Float[0], end='')
    print('+', end='')
    print(wspolczynnik1Float[1], end='')
    print('x', end='')
else:
    print(wspolczynnik1Float[0], end='')
    print('+', end='')
    print(wspolczynnik1Float[1], end='')
    print('x', end='')
    pow = 2;
    for x in wspolczynnik1Float:
        index = wspolczynnik1Float.index(x);
        if index > 1:
            print('+', end='')
            print('x', end='')
            print('x^', end='')
            print(pow, end='')
            pow = pow + 1

