#ZAD.1 7 8
def writeToFile(file):
    f1 = open('c://temp//' + file, 'w')

    dl = int(input("Podaj dlugosc ciagu: "))

    for _ in range(dl):
        liczba = input("Podaj wyraz ciagu: ")
        f1.write(liczba + " ")


    f1.close()

if __name__ == '__main__':
    file = input("Podaj nazwe pliku\n")

    writeToFile(file)

#ZAD.2
nums = []


def writeFromFileToFile(file1, file2):
    f1 = open('C:/temp/' + file1, 'r')
    f2 = open('C:/temp/' + file2, 'w')

    nums = f1.readlines()

    for x in nums:
        print(x)

    numsInt = [int(x) for x in nums]

    for x in numsInt:
        if x % 2 == 1:
            f2.write(f"{x}")

    f1.close()
    f2.close()


if __name__ == '__main__':
    file1 = input("Podaj nazwe pliku 1\n")
    file2 = input("Podaj nazwe pliku 2\n")

    writeFromFileToFile(file1, file2)

#ZAD.3

def writeFromFileToFile(file1, file2):
    f1 = open('C:/temp/' + file1, 'r')
    f2 = open('C:/temp/' + file2, 'w')

    liczba = f1.readline()

    print(liczba)
    num = 1
    liczbaInt = int(liczba)
    while liczbaInt >= 1:
        num = num * liczbaInt
        liczbaInt = liczbaInt - 1

    print(num)

    f2.write(f"{num}")

    f1.close()
    f2.close()


if __name__ == '__main__':
    file1 = input("Podaj nazwe pliku 1\n")
    file2 = input("Podaj nazwe pliku 2\n")

    writeFromFileToFile(file1, file2)

#ZAD.4
def writeFromFileToFile(file1, file2):
    f1 = open('c://temp//' + file1, 'r')
    f2 = open('c://temp//' + file2, 'w')

    miastaPopulacja = f1.readlines()

    for miastoPopulacja in miastaPopulacja:
        print(miastoPopulacja)

    miastaPopulacjaLista = []

    for miastoPopulacja in miastaPopulacja:
        x = miastoPopulacja.split()
        miastaPopulacjaLista.append(x)

    final = []
    counter = 1
    for miastoPopulacjaLista in miastaPopulacjaLista:
        for x in miastoPopulacjaLista:
            if(counter % 2 == 0):
                if(int(x) > 300000):
                    final.append(miastoPopulacjaLista)
            counter = counter + 1

    for y in final:
        f2.write(f"{y}" + "\n")

    f1.close()
    f2.close()


if __name__ == '__main__':
    file1 = input("Podaj nazwe pliku 1\n")
    file2 = input("Podaj nazwe pliku 2\n")

    writeFromFileToFile(file1, file2)
#ZAD.5
def writeFromFileToFile(file1, file2):
    f1 = open('c://temp//' + file1, 'r')
    f2 = open('c://temp//' + file2, 'w')

    liczby = f1.readlines()

    liczbyInt = [int(x) for x in liczby]
    listaparzystych = []
    for y in liczbyInt:
        text = f"{y}"
        if len(text) == 4 and int(text) % 2 == 0 and text[1] == text[2]:
            listaparzystych.append(y)

    for liczba in liczby:
        print(liczba)

    for l in listaparzystych:
        f2.write(f"{l}" + '\n')

    f1.close()
    f2.close()


if __name__ == '__main__':
    file1 = input("Podaj nazwe pliku 1\n")
    file2 = input("Podaj nazwe pliku 2\n")

    writeFromFileToFile(file1, file2)
#ZAD. 6
liczby =[]
def writeFromFileToFile(file1, file2):
    f1 = open('c://temp//' + file1, 'r')
    f2 = open('c://temp//' + file2, 'w')

    liczby = f1.readlines()

    liczbyInt = [int(x) for x in liczby]
    listaparzystych = []
    for y in liczbyInt:
        text= f"{y}"
        if len(text) == 4 and int(text)%2 == 0 and text[2] > text[3]:
            listaparzystych.append(y)

    for liczba in liczby:
        print(liczba)

    for l in listaparzystych:
        f2.write(f"{l}" + '\n')

    f1.close()
    f2.close()


if __name__ == '__main__':
    file1 = input("Podaj nazwe pliku 1\n")
    file2 = input("Podaj nazwe pliku 2\n")

    writeFromFileToFile(file1, file2)

#ZAD.7

def writeFromFileToFile(file1, file2):
    f1 = open('c://temp//' + file1, 'r')


    wymiar = int(f1.readline().strip())
    macierz = []
    for y in range(wymiar):
        wiersz = [int(x) for x in f1.readline().split()]
        macierz.append(wiersz)
    skalar = int(f1.readline().strip())

    print(f"Wymiar macierzy: {wymiar}")
    print("Macierz:")
    for wiersz in macierz:
        print(wiersz)
    print(f"Skalar: {skalar}")

    wynik = []
    for y in range(wymiar):
        wiersz2 = []
        for z in range(wymiar):
            wiersz2.append(macierz[y][z] * skalar)
        wynik.append(wiersz2)
    plik2 = open(file2, 'w')
    for wiersz in wynik:
        row = " ".join([str(x) for x in wiersz])
        plik2.write(f"{row}\n")




if __name__ == '__main__':
    file1 = input("Podaj nazwe pliku 1\n")
    file2 = input("Podaj nazwe pliku 2\n")

    writeFromFileToFile(file1, file2)

#ZAD.8

def writeFromFileToFile(file1, file2):
    f1 = open('c://temp//' + file1, 'r')
    wymiar = int(f1.readline().strip())
    macierz = []
    for y in range(wymiar):
        wiersz = [int(x) for x in f1.readline().strip().split()]
        macierz.append(wiersz)
    wektor = [int(x) for x in f1.readline().strip().split()]

    print(f'Wymiar macierzy: {wymiar}')
    print('Macierz:')
    for wiersz in macierz:
        print(wiersz)
    print(f'Wektor: {wektor}')

    wynik = []
    for y in range(wymiar):
        o = 0
        for z in range(wymiar):
            o += macierz[y][z] * wektor[z]
        wynik.append(o)
    f2 = open(file2, 'w')
    f2.write(' '.join([str(x) for x in wynik]))

if __name__ == '__main__':
    file1 = input("Podaj nazwe pliku 1\n")
    file2 = input("Podaj nazwe pliku 2\n")

    writeFromFileToFile(file1, file2)

#ZAD.9

def writeFromFileToFile(file1, file2):
    f1 = open('c://temp//' + file1, 'r')
    wymiar = int(f1.readline().strip())
    macierz1 = []
    for y in range(wymiar):
        wiersz = [int(x) for x in f1.readline().strip().split()]
        macierz1.append(wiersz)
    macierz2 = []
    for y in range(wymiar):
        wiersz = [int(x) for x in f1.readline().strip().split()]
        macierz2.append(wiersz)

    suma = []
    for y in range(wymiar):
        suma = []
        for z in range(wymiar):
            suma_macierzy = macierz1[y][z] + macierz2[y][z]
            wiersz_suma.append(suma_macierzy)
        suma.append(wiersz_suma)

    plik2 = open(file2, 'w')
    for wiersz in suma:
        plik2.write(" ".join(str(x) for x in wiersz))
        plik2.write("\n")

if __name__ == '__main__':
    file1 = input("Podaj nazwe pliku 1\n")
    file2 = input("Podaj nazwe pliku 2\n")

    writeFromFileToFile(file1, file2)

#ZAD.10
import numpy as np
def Mnozenie(file1, file2):
    f1 = open(file1, 'r')
    wymiar = int(f1.readline().strip())
    macierz1 = []
    for y in range(wymiar):
        wiersz = [int(x) for x in f1.readline().strip()]
        macierz1.append(wiersz)
    macierz2 = []
    for y in range(wymiar):
        wiersz = [int(x) for x in f1.readline().strip()]
        macierz2.append(wiersz)

    wynik = macierz1.copy()

    wynik = []
    for x in range(len(wynik)):
        for y in range(len(wynik)):
            wynik = np.matmul(macierz1, macierz2)
            return wynik;

    plik2 = open(file2, 'w')
    plik2.write(wynik)


if __name__ == '__main__':
    file1 = input("Podaj nazwe 1 pliku: ")
    file2 = input("Podaj nazwę 2 pliku: ")
    Mnozenie(file1, file2)

#ZAD.11
liczby =[]
def writeFromFileToFile(file1, file2):
    f1 = open('c://temp//' + file1, 'r')
    f2 = open('c://temp//' + file2, 'w')

    wspolczynnikiWLiscie = f1.readlines()

    for wspolczynnikWLiscie in wspolczynnikiWLiscie:
        print(wspolczynnikWLiscie, end='')

    wspolczynniki1 = []
    wspolczynniki2 = []
    counter = 1

    for wspolczynnikWLiscie in wspolczynnikiWLiscie:
        if (counter == 1):
            for x in wspolczynnikWLiscie:
                wspolczynniki1.append(x)
            counter = counter + 1
        else:
            for x in wspolczynnikWLiscie:
                wspolczynniki2.append(x)

    wspolczynniki1Float = []
    wspolczynniki2Float = []

    counter = 1
    for x in wspolczynniki1:
        if (counter % 2 != 0):
            wspolczynniki1Float.append(float(x))
        counter = counter + 1

    counter = 1
    for x in wspolczynniki2:
        if (counter % 2 != 0):
            wspolczynniki2Float.append(float(x))
        counter = counter + 1

    a = len(wspolczynniki1Float)
    b = len(wspolczynniki2Float)

    print()

    if a > b:
        for x in range(0, len(wspolczynniki2Float)):
            wspolczynniki1Float[x] = wspolczynniki1Float[x] + wspolczynniki2Float[x]
            print(f"{wspolczynniki1Float[x]}" + " ", end='')
            f2.write(f"{wspolczynniki1Float[x]}" + " ")

        N = len(wspolczynniki1Float) - len(wspolczynniki2Float)

        res = wspolczynniki1Float[-N:]

        for x in res:
            print(f"{x}" + " ", end='')
            f2.write(f"{x}" + " ")
    else:
        for x in range(0, len(wspolczynniki1Float)):
            wspolczynniki2Float[x] = wspolczynniki1Float[x] + wspolczynniki2Float[x]
            print(f"{wspolczynniki2Float[x]}" + " ", end='')
            f2.write(f"{wspolczynniki2Float[x]}" + " ")

        N = len(wspolczynniki2Float) - len(wspolczynniki1Float)

        res = wspolczynniki2Float[-N:]

        for x in res:
            print(f"{x}" + " ", end='')
            f2.write(f"{x}" + " ")
    f1.close()
    f2.close()


if __name__ == '__main__':
    file1 = input("Podaj nazwe pliku 1\n")
    file2 = input("Podaj nazwe pliku 2\n")

    writeFromFileToFile(file1, file2)

#ZAD. 12
nums = []
def writeFromFileToFile(file1, file2):
    f1 = open('C:/temp/' + file1, 'r')
    f2 = open('C:/temp/' + file2, 'w')

    nums = f1.readlines()

    for x in nums:
        print(x)

    numsInt = [int(x) for x in nums]

    numsSqr = []

    for x in numsInt:
        x = x * x
        numsSqr.append(x)
    suma = 0
    for x in numsSqr:
        suma = suma + x

    f2.write(f"{suma}")

    f1.close()
    f2.close()



if __name__ == '__main__':
    file1 = input("Podaj nazwe pliku 1\n")
    file2 = input("Podaj nazwe pliku 2\n")

    writeFromFileToFile(file1, file2)
