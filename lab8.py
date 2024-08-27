# ZAD 1.
def writeToFile(file):
    try:
        with open('c://temp//' + file, 'r') as f1:
            liczba = f1.readlines()
            liczbaInt = [int(x) for x in liczba]
            for x in liczbaInt:
                print(x)
    except FileNotFoundError:
        print("Podany plik nie istnieje")


if __name__ == '__main__':
    file = input("Podaj nazwę pliku\n")
    writeToFile(file)

# ZAD 2. i ZAD 3.
class LiczbaWiekszaOd100(Exception):
    informacja = "Liczba jest większa od 100"

    def __init__(self, informacja):
        self.informacja = informacja

def writeToFile(file):
    try:
        with open('c://temp//' + file, 'r') as f1:
            liczba = f1.readlines()
            liczbaInt = [int(x) for x in liczba]

            for x in liczbaInt:
                print(x)

            kwadraty = [a * a for a in liczbaInt]
            suma = sum(kwadraty)
            print(suma)

            if suma > 100:
                raise LiczbaWiekszaOd100("Liczba jest większa od 100")
            else:
                print("Liczba nie jest większa od 100")
    except LiczbaWiekszaOd100 as wyj:
        print("Wystąpienie wyjątku: LiczbaWiekszaOd100")
        print(wyj)
    except FileNotFoundError:
        print("Podany plik nie istnieje")

if __name__ == '__main__':
    file = input("Podaj nazwę pliku\n")
    writeToFile(file)

# ZAD 4. i ZAD 5.
class LiczbaWiekszaOd100(Exception):
    def __init__(self, informacja):
        self.informacja = informacja

class Liczba0(LiczbaWiekszaOd100):
    def __init__(self, informacja="Liczba wynosi 0"):
        super().__init__(informacja)

def writeToFile(file):
    try:
        with open('c://temp//' + file, 'w') as f1:
            print("Podaj jeden z wymiarów macierzy kwadratowej")
            a = int(input())
            if a > 0:
                b = a
                macierz = [[0 for i in range(a)] for j in range(b)]

                print("Podaj wszystkie współczynniki macierzy, aby ją wypełnić")
                f1.write("MACIERZ:\n")
                for i in range(len(macierz)):
                    for j in range(len(macierz[i])):
                        print(f"a{i+1}{j+1} współczynnik:", end=' ')
                        wsp1 = int(input())
                        macierz[i][j] = wsp1
                        f1.write(f"a{i+1}{j+1} {wsp1}")
                        try:
                            if wsp1 > 100:
                                raise LiczbaWiekszaOd100(" - współczynnik jest większy od 100")
                            elif wsp1 == 0:
                                raise Liczba0(" - współczynnik jest równy 0")
                        except LiczbaWiekszaOd100 as e:
                            f1.write(str(e))
                        except Liczba0 as e:
                            f1.write(str(e))
                        f1.write("\n")
    except FileNotFoundError:
        print("Podany plik nie istnieje")

if __name__ == '__main__':
    file = input("Podaj nazwę pliku\n")
    writeToFile(file)

# ZAD 6.
class LiczbaWiekszaOd100(Exception):
    def __init__(self, informacja):
        self.informacja = informacja

class Liczba0(LiczbaWiekszaOd100):
    def __init__(self, informacja="Liczba wynosi 0"):
        super().__init__(informacja)

class ZlaLiczba(Liczba0):
    def __init__(self, informacja):
        self.informacja = informacja

def writeToFile(file):
    try:
        with open('c://temp//' + file, 'w') as f2:
            ciag = input("Podaj ciąg liczb oddzielonych spacjami: ").split()
            ciag = [int(x) for x in ciag]
            f2.write("Ciąg:\n")
            for x in ciag:
                f2.write(str(x) + "\n")
    except FileNotFoundError:
        print("Podany plik nie istnieje")

    try:
        with open('c://temp//' + file, 'r') as f1:
            print(f1.read())
    except FileNotFoundError:
        print("Podany plik nie istnieje")

    suma = sum(a ** 2 for a in ciag)
    try:
        if suma > 100:
            raise LiczbaWiekszaOd100("Suma kwadratów jest większa od 100")
        elif suma == 0:
            raise Liczba0("Suma kwadratów jest równa 0")
        else:
            print(suma)
    except LiczbaWiekszaOd100 as e:
        print(str(e))
    except Liczba0 as e:
        print(str(e))

if __name__ == '__main__':
    file = input("Podaj nazwę pliku\n")
    writeToFile(file)

# ZAD 7.
class LiczbaWiekszaOd100(Exception):
    def __init__(self, informacja):
        self.informacja = informacja

class ZlaLiczba(Exception):
    def __init__(self, informacja):
        self.informacja = informacja

def superrosnacy(ciag):
    suma = 0
    for a in range(len(ciag)):
        if ciag[a] <= suma:
            raise ZlaLiczba(f"Liczba {ciag[a]} nie spełnia warunku.")
        suma += ciag[a]
    return True

def sredniaar(ciag):
    srednia = sum(ciag) / len(ciag)
    if srednia > 100:
        raise LiczbaWiekszaOd100("Średnia arytmetyczna jest większa od 100.")
    return srednia

def funkcja(nazwapliku):
    try:
        with open(nazwapliku, 'r') as plik:
            ciag = [int(x) for x in plik.read().split(', ')]
            print("Ciąg superrosnący: ", ciag)
            superrosnacy(ciag)
            srednia = sredniaar(ciag)
            print("Średnia arytmetyczna: ", srednia)
    except FileNotFoundError:
        print("Podany plik nie istnieje.")
    except ZeroDivisionError:
        print("Nie można dzielić przez zero.")
    except LiczbaWiekszaOd100 as e:
        print(str(e))
    except ZlaLiczba as e:
        print(str(e))

def main():
    nazwapliku = input("Podaj nazwę pliku: ")
    funkcja(nazwapliku)

if __name__ == "__main__":
    main()

# ZAD 8.
class LiczbaWiekszaOd100(Exception):
    def __init__(self, informacja):
        self.informacja = informacja

class ZlaLiczba(Exception):
    def __init__(self, informacja):
        self.informacja = informacja

def obliczsr(nazwapliku):
    try:
        liczba = []
        with open(nazwapliku, "r") as f:
            for line in f:
                num = int(line.strip())
                if liczba and num <= sum(liczba):
                    raise ZlaLiczba("Podany ciąg nie jest superrosnący")
                liczba.append(num)

        sr = sum(liczba) / len(liczba)
        print("Średnia wynosi:", sr)
        if sr > 100:
            raise LiczbaWiekszaOd100("Średnia jest większa od 100")
    except FileNotFoundError:
        print("Podany plik nie istnieje")
    except ZeroDivisionError:
        print("Nie można obliczyć średniej dla pustego pliku")
    except ZlaLiczba as e:
        print("Błąd:", e)
    except LiczbaWiekszaOd100 as e:
        print("Błąd:", e)
    finally:
        print("Ten kod został wykonany w klauzuli finally")

if __name__ == "__main__":
    obliczsr("ciag.txt")
