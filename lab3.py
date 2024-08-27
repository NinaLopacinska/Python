#zadanie 1

a = int(input("Podaj wymiar macierzy (macierz kwadratowa): "))
Lista = []
macierz = []

print("Podaj wspolczynniki macierzy: ( ", int(a)*int(a) , " ) ")

for i in range(a):
    Lista = []
    for i in range (a):
        wsp = int(input())
        Lista.append(wsp)
    macierz.append(Lista)

print(macierz)
skalar = int(input("Wprowadz skalar, przez ktory chcesz pomnozyc macierz: "))

for i in range(a):
    for j in range(a):
        macierz[i][j] *= skalar

print("Nowa macierz to :", macierz)






#zadanie 2

a = int(input("\nPodaj wymiar macierzy (macierz kwadratowa): "))
List = []
macierz = []
wektor = []

print("Podaj wspolczynniki macierzy: ")

for i in range(a):
    List = []
    for i in range (a):
        wsp = int(input())
        List.append(wsp)
    macierz.append(List)
print(macierz)

print("Podaj wspolczynniki wektora: ")
for i in range(a):
    wsp2 = int(input())
    wektor.append(wsp2)
print(wektor)
iloczyn = 0
iloczyn_lista = []

for i in range(a):
    iloczyn = 0
    for j in range(a):
        iloczyn = iloczyn + macierz[i][j] * wektor[j]
    iloczyn_lista.append(iloczyn)

print("Macierz wymnożona przez wektor to: ", iloczyn_lista)




#zadanie 3

a = int(input("Podaj wymiar macierzy kwadratowych: "))

macierz1 = []
for i in range(a):
    row = []
    for j in range(a):
        row.append(float(input(f"Podaj współczynnik macierzy 1 [{i+1}][{j+1}]: ")))
    macierz1.append(row)

macierz2 = []
for i in range(a):
    row = []
    for j in range(a):
        row.append(float(input(f"Podaj współczynnik macierzy 2 [{i+1}][{j+1}]: ")))
    macierz2.append(row)

macierz3 = []
for i in range(a):
    row = []
    for j in range(a):
        row.append(macierz1[i][j] + macierz2[i][j])
    macierz3.append(row)

print("Wynik:")
for row in macierz3:
    print(row)



#zadanie 4


a = int(input("Podaj wymiar pierwszej macierzy (macierz kwadratowa): "))
Lista = []
macierz1 = []

print("Podaj wspolczynniki pierwszej macierzy: ( ", int(a)*int(a) , " ) ")

for i in range(a):
    Lista = []
    for i in range (a):
        wsp = int(input())
        Lista.append(wsp)
    macierz1.append(Lista)

print(macierz1)

b = int(input("Podaj wymiary drugiej macierzy (macierz kwadratowa): "))
Lista = []
macierz2 = []

print("Podaj wspolczynniki drugiej macierzy: ( ", int(b)*int(b) , " ) ")

for i in range(b):
    Lista = []
    for i in range (b):
        wsp2 = int(input())
        Lista.append(wsp2)
    macierz2.append((Lista))

print(macierz2)

wynik = []
for i in range(a):
    Lista = []
    for j in range(a):
        element_sum = 0
        for k in range(a):
            element_sum += macierz1[i][k] * macierz2[k][j]
        Lista.append(element_sum)
    wynik.append(Lista)

print("Iloczyn macierzy wynosi:")
for Lista in wynik:
    print(Lista)


