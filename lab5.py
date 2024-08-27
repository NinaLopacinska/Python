#zad 1

def liczby_nieparzyste(ciag):
    nieparzyste = []
    for liczba in ciag:
        if liczba % 2 != 0:
            nieparzyste.append(liczba)
    return nieparzyste


if __name__ == '__main__':
    ciag = input("Podaj ciąg liczb, oddzielając je spacją: ")
    ciag = [int(x) for x in ciag.split()]
    nieparzyste = liczby_nieparzyste(ciag)
    print("Liczby nieparzyste w podanym ciągu to: ", nieparzyste)

#zad 2

def silnia(n):
    wynik = 1
    for i in range(1, n+1):
        wynik *= i
    return wynik
if __name__ == '__main__':
    n = int(input("Podaj liczbę całkowitą: "))
    wynik = silnia(n)
    print(n, " silnia wynosi:", wynik)


#zad 3

def miasta_powyzej_300k(miejscowosci):
    wynik = {}
    for miasto, liczba_mieszkancow in miejscowosci.items():
        if liczba_mieszkancow > 300000:
            wynik[miasto] = liczba_mieszkancow
    return wynik
if __name__ == '__main__':
    miejscowosci = {}
    while True:
        miasto = input("Podaj nazwę miasta (lub stop, aby zakończyć): ")
        if miasto == 'stop':
            break
        liczba_mieszkancow = int(input("Podaj liczbę mieszkańców: "))
        miejscowosci[miasto] = liczba_mieszkancow
    wynik = miasta_powyzej_300k(miejscowosci)
    print("Miasta z populacją powyżej 300 000 to:", wynik)


#zad 4

def liczby_czterocyfrowe(parzyste_ciag):
    wynik = []
    for i in parzyste_ciag:
        if len(i) == 4 and ((int(i[0]) > int(i[3])) or int(i) % 2 == 0):
            wynik.append(i)
    return wynik

def main():
    ciag = input("Podaj ciąg liczb oddzielanych spacją: ")
    liczby = ciag.split()
    wynik = liczby_czterocyfrowe(liczby)
    print("Czterocyfrowe liczby, w których pierwsza cyfra jest większa od czwartej i są parzyste:")
    print(wynik)

if __name__ == "__main__":
    main()


#zad 5

def liczby_trzy(ciag):
    wynik = []
    for i in ciag:
        if len(i) == 3 and int(i[0]) == int(i[1]) == int(i[2]) and int(i) % 2 == 1:
            wynik.append(i)
    return wynik

if __name__ == "__main__":
    ciag = input("Podaj ciąg liczb oddzielanych spacją: ")
    liczby = ciag.split()
    wynik = liczby_trzy(liczby)
    print("Trzycyfrowe liczby nieparzyste o jednakowych cyfrach, z tych, które podałeś:")
    print(wynik)


#zad 6

def iloczyn_macierzy_przez_skalar(wym_mac, macierz, skalar):
    wynik = [[0 for j in range(wym_mac)] for i in range(wym_mac)]
    for i in range(wym_mac):
        for j in range(wym_mac):
            wynik[i][j] = macierz[i][j] * skalar
    return wynik

if __name__ == "__main__":
    wym_mac = int(input("Podaj wymiar macierzy kwadratowej: "))
    macierz = [[0 for j in range(wym_mac)] for i in range(wym_mac)]
    for i in range(wym_mac):
        for j in range(wym_mac):
            macierz[i][j] = float(input(f"Podaj współczynnik [{i+1},{j+1}]: "))
    skalar = float(input("Podaj wartość skalara: "))

    wynik = iloczyn_macierzy_przez_skalar(wym_mac, macierz, skalar)

    print("Iloczyn macierzy przez skalara:")
    for row in wynik:
        print(row)

#zad 7

def iloczyn_macierz_wektor(wym_mac, macierz, wektor):
    wyn = [0 for i in range(wym_mac)]
    for i in range(wym_mac):
        for j in range(wym_mac):
            wyn[i] += macierz[i][j] * wektor[j]
    return wyn
if __name__ == "__main__":
    wym_mac = int(input("Podaj wymiar macierzy kwadratowej: "))

    macierz = [[0 for j in range(wym_mac)] for i in range(wym_mac)]

    for i in range(wym_mac):
        for j in range(wym_mac):
            macierz[i][j] = float(input(f"Podaj współczynnik [{i+1},{j+1}]: "))

    wektor = [0 for i in range(wym_mac)]
    for i in range(wym_mac):
        wektor[i]=float(input(f"Podaj współczynnik wektora nr [{i+1}]: "))

    wynik = iloczyn_macierz_wektor(wym_mac, macierz, wektor)

    print("Iloczyn macierzy przez wektor:")
    for row in wynik:
        print(row)


#zad 8

def dodaj_macierze(wym_mac, macierz1, macierz2):
    suma_macierz = [[0 for j in range(wym_mac)] for i in range(wym_mac)]
    for i in range(wym_mac):
        for j in range(wym_mac):
            suma_macierz[i][j] = macierz1[i][j] + macierz2[i][j]
    return suma_macierz
if __name__ == "__main__":
    wym_mac = int(input("Podaj wymiar macierzy kwadratowych: "))

    macierz1 = [[0 for j in range(wym_mac)] for i in range(wym_mac)]
    macierz2 = [[0 for j in range(wym_mac)] for i in range(wym_mac)]

    print("Macierz 1 współczynniki: ")
    for i in range(wym_mac):
        for j in range(wym_mac):
            macierz1[i][j] = float(input(f"Podaj współczynnik [{i + 1},{j + 1}]: "))

    print("Macierz 2 współczynniki: ")
    for i in range(wym_mac):
        for j in range(wym_mac):
            macierz2[i][j] = float(input(f"Podaj współczynnik [{i + 1},{j + 1}]: "))

    suma_macierz = dodaj_macierze(wym_mac, macierz1, macierz2)

    print("Suma macierzy:")
    for i in range(wym_mac):
        for j in range(wym_mac):
            print(suma_macierz[i][j], end="\t")
        print()

#zad 9

def iloczyn_macierzy(wymiar, macierz1, macierz2):
    iloczyn = [[0 for j in range(wymiar)] for i in range(wymiar)]
    for i in range(wymiar):
        for j in range(wymiar):
            for xd in range(wymiar):
                iloczyn[i][j] += macierz1[i][xd] * macierz2[xd][j]
    return iloczyn
if __name__ == "__main__":
    wymiar = int(input("Podaj wymiar macierzy kwadratowych: "))

    macierz1 = [[0 for j in range(wymiar)] for i in range(wymiar)]
    macierz2 = [[0 for j in range(wymiar)] for i in range(wymiar)]

    print("Macierz 1 współczynniki: ")
    for i in range(wymiar):
        for j in range(wymiar):
            macierz1[i][j] = float(input(f"Podaj współczynnik [{i + 1},{j + 1}]: "))

    print("Macierz 2 współczynniki: ")
    for i in range(wymiar):
        for j in range(wymiar):
            macierz2[i][j] = float(input(f"Podaj współczynnik [{i + 1},{j + 1}]: "))

    iloczyn = iloczyn_macierzy(wymiar, macierz1, macierz2)

    print("Iloczyn macierzy:")
    for i in range(wymiar):
        for j in range(wymiar):
            print(iloczyn[i][j], end="\t")
        print()


#zad 10


def sumuj_wielomiany(w1, w2):
    print("Wielomian 1:", w1)
    print("Wielomian 2:", w2)
    suma = [0] * max(len(w1), len(w2))
    for i in range(len(w1)):
        suma[i] += w1[i]
    for i in range(len(w2)):
        suma[i] += w2[i]
    return suma

if __name__ == "__main__":
    w1 = [int(x) for x in input("Podaj współczynniki wielomianu 1, oddzielone spacjami: ").split()]
    w2 = [int(x) for x in input("Podaj współczynniki wielomianu 2, oddzielone spacjami: ").split()]
    wynik = sumuj_wielomiany(w1, w2)
    print("Suma wielomianów:", wynik)

#zad 11

def suma_kwadratow(liczba):
    suma=0
    for i in liczba:
        suma+=i**2
    return suma
if __name__ == "__main__":
    liczba=input("Podaj ciąg liczb oddzielonych spacją: ").split()
    liczby=[int(i) for i in liczba]
    wynik = suma_kwadratow(liczby)
    print("Suma kwadratów liczb w ciągu: ", wynik)



# zad 12

def wykonaj_dzialanie(x, y, dzialanie):
    if dzialanie == "+":
        return x + y
    elif dzialanie == "-":
        return x - y
    elif dzialanie == "*":
        return x * y
    elif dzialanie == "/":
        return x / y

if __name__ == "__main__":
    x = float(input("Podaj pierwszą liczbę: "))
    y = float(input("Podaj drugą liczbę: "))
    dzialanie = input("Podaj działanie (+,-,*,/): ")

    wynik = wykonaj_dzialanie(x, y, dzialanie)
    print(f"Wynik działania: {wynik}")
