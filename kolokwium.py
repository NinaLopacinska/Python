#ZAD.1

def zwrocSilnie(liczba):
    silnia = 1
    while liczba >= 1:
        silnia = silnia * liczba
        liczba = liczba - 1
    return silnia

if __name__ == '__main__':
    liczba = int(input("Podaj liczbe, ktorej silnie chcesz policzyc: "))

    zwroconaSilnia = zwrocSilnie(liczba)

    print(zwroconaSilnia)


#ZAD.2
def zwrocCiag(ciag):
    liczby4cyfr = []

    for x in ciag:
        if x >= 0:
            if len(str(x)) == 4 and x % 2 == 0:
                a = str(x)[0]
                b = str(x)[3]

                a = int(a)
                b= int(b)
                if a>b:
                    liczby4cyfr.append(x)
        else:
            if len(str(x)) == 5 and x % 2 == 0:
                a = str(x)[1]
                b = str(x)[4]

                a = int(a)
                b = int(b)
                if a > b:
                    liczby4cyfr.append(x)

    return liczby4cyfr

if __name__ == '__main__':
    dl = int(input("Podaj długość ciągu liczb: "))
    ciag = []

    for _ in range(dl):
        wyraz = int(input("Podaj wyraz ciągu: "))
        ciag.append(wyraz)

    zwrocCiag4cyfr = zwrocCiag(ciag)

    print(zwrocCiag4cyfr)

#ZAD.3
def zapiszDoPliku(file1, file2):
    f1 = open('c://temp//' + file1, 'r')
    f2 = open('c://temp//' + file2, 'w')

    liczby = f1.readlines()
    liczbyInt = []

    for liczba in liczby:
        liczbyInt.append(int(liczba))

    for liczba in liczbyInt:
        print(liczba)

    for liczba in liczbyInt:

        if liczba % 2 != 0:
            f2.write(str(liczba) + "\n")

    f1.close()
    f2.close()


if __name__ == '__main__':
    plik1 = input("Podaj nzawe pliku: ")
    plik2 = input("Podaj nzawe pliku: ")

    zapiszDoPliku(plik1, plik2)

#ZAD.4
class Osoba:
  def __init__(self, wiek, imie):
    self.wiek = wiek
    self.imie = imie

  def funkcja(self):
    print(self.imie)
    self.wiek = self.wiek + 5
    return self.wiek


if __name__ == '__main__':
    os1 = Osoba(30, "Ala")
    wiek = os1.funkcja()
    print(wiek)


