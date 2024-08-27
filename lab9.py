def zad1(nazwa_pliku):
    f = open(nazwa_pliku, 'r')
    n = f.read().split()
    for x in n:
        if len(x) == 4 and int(x) % 2 == 0 and x[0]  == x[2]:
            yield x
    f.close()


def zad2(nazwa_pliku):
    f = open(nazwa_pliku, 'r')
    n = f.read().split()
    for x in n:
        if len(x) == 3 and int(x) % 2 != 0 and x[0] == x[2]:
            yield x
    f.close()


def zad3(nazwa_pliku):
    f = open(nazwa_pliku, 'r')
    n = f.read().split()
    primes_numbers = []
    for x in n:
        x = int(x)
        if x == 2:
            primes_numbers.append(x)
        elif x % 2 != 0 and x > 1:
            pierwsza = int(x**0.5) + 1
            for dzielnik in range(3, pierwsza, 2):
                if x % dzielnik == 0:
                    break
            else:
                primes_numbers.append(x)
    f.close()
    yield from primes_numbers


def zad4(nazwa_pliku):
    f = open(nazwa_pliku, 'r')
    n = f.read().split()
    slownik = eval(n())
    for miasto, liczba_mieszkancow in slownik.items():
        if liczba_mieszkancow > 300000:
            yield f"{miasto} : {liczba_mieszkancow} "



if __name__ == '__main__':
    nazwa_pliku = input("Podaj nazwe pliku: ")

    print("\n Zadanie 1 \n")
    zad1(nazwa_pliku)
    for x in zad1(nazwa_pliku):
        print(x)

    print("\n Zadanie 2 \n")
    zad2(nazwa_pliku)
    for x in zad2(nazwa_pliku):
        print(x)

    print("\n Zadanie 3 \n")
    zad3(nazwa_pliku)
    for x in zad3(nazwa_pliku):
        print(x)

    print("\n Zadanie 4 \n")
    zad4(nazwa_pliku)
    for x in zad4(nazwa_pliku):
        print(x)

#poprawione