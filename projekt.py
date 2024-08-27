import matplotlib.pyplot as plt


def writeFromFileToFile(file1, file2):
    f1 = open('c://temp//' + file1, 'r')
    f2 = open('c://temp//' + file2, 'w')

    imionaNajpopularniejsze = f1.readlines()

    for imieLiczba in imionaNajpopularniejsze:
        print(imieLiczba)

    imionaNajpopularniejszeLista = []
    imieNajpop = {}

    for imieLiczbaWys in imionaNajpopularniejsze:
        x = imieLiczbaWys.split()
        imionaNajpopularniejszeLista.append(x)

    suma = 0
    licznik = 1
    for imieNajpopularniejszeLista in imionaNajpopularniejszeLista:
        for x in imieNajpopularniejszeLista:
            if licznik == 1:
                max = x
            if licznik % 2 == 0:
                suma = suma + int(x)
                wys = x
            else:
                imie = x
            licznik = licznik + 1
        imieNajpop[imie] = int(wys)

    suma = suma + 77473
    suma = suma / 12

    t = "MonthAvg"

    f2.write(
        "Średnio miesięcznie w 2022 roku urodziło się " + f"{suma}" + " dziewcząt.\nNajpopularniejszym imieniem bylo imie " + f"{max}"".")

    imieNajpop[t] = suma
    data = imieNajpop
    imie = list(data.keys())
    iloscWystepowania = list(data.values())
    fig = plt.figure(figsize=(10, 5))
    plt.bar(imie, iloscWystepowania, color='black',
            width=0.4)

    plt.ylim(2500, 14000)
    plt.xlabel("Imie")
    plt.ylabel("Ilość występowań")
    plt.title("Imiona żeńskie nadane dzieciom w Polsce w 2022 r.")
    plt.show()

    f1.close()
    f2.close()


if __name__ == '__main__':
    file1 = input("Podaj nazwe pierwszego pliku: \n")
    file2 = input("Podaj nazwe drugiego pliku:  \n")

    writeFromFileToFile(file1, file2)
