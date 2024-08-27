class Dzialania_Na_Plikach:

    def __init__(self):
        print("zadanie 1")
        self.nazwa = input("Podaj nazwę pliku, do którego chcesz wpisać ciąg: ")
        self.ciag = input("Podaj ciąg liczb, oddzielonych spacją: ")
        self.zadanie1(self.ciag, self.nazwa)

        print("zadanie 2")
        self.nazwa_ist = input("Podaj nazwę pliku, z którego chcesz wczytac ciag\n>>")
        self.nazwa_nie = input("Podaj nazwę pliku, w którym chcesz to zapisac\n>>")
        self.zadanie2(self.nazwa_ist, self.nazwa_nie)

        print("zadanie 3")
        self.nazwa_pl = input("Podaj nazwe pliku, w ktorym zapisales informacje\n>>")
        self.nazwa_nowa = input("Podaj nazwe pliku, w którym chcesz zapisac wynik\n>>")
        self.zadanie3(self.nazwa_pl, self.nazwa_nowa)

        print("zadanie 4")
        self.dane = input("Podaj nazwe pliku, ktory zawiera informacje\n>>")
        self.nazwa_pliku = input("Podaj nazwe plku, w którym chcesz zapisac wynik\n>>")
        self.zadanie4(self.dane, self.nazwa_pliku)

        print("zadanie 5")
        self.nazwa_pliku5 = input("Podaj nazwe pliku, z ktorego chcesz wczytać ciąg\n>>")
        self.nazwa_stworzonego5 = input("Podaj nazwe pliku, w ktorym chcesz zapisać wynik\n>>")
        self.zadanie5(self.nazwa_pliku5, self.nazwa_stworzonego5)

        print("zadanie 6")
        self.nazwa_pliku6 = input("Podaj nazwe pliku, z którego chcesz wczytać ciąg\n>>")
        self.nazwa_stworzonego6 = input("Podaj nazwe pliku, w ktorym chcesz zapisać wynik\n>>")
        self.zadanie6(self.nazwa_pliku6, self.nazwa_stworzonego6)

        print("zadanie 7")
        self.nazwa_pliku7 = input("Podaj nazwę pliku, z informacja o macierzy:\n>> ")
        self.nazwa_stworzonego7 = input("Podaj nazwę pliku, w ktorym chcesz zapisać wynik:\n>> ")
        self.zadanie7(self.nazwa_pliku7, self.nazwa_stworzonego7)

        print("zadanie 8")
        self.nazwa_pliku8 = input("Podaj nazwę pliku, z informacja o macierzy:\n>> ")
        self.nazwa_stworzonego8 = input("Podaj nazwę pliku, w ktorym chcesz chcesz zapisać wynik:\n>> ")
        self.zadanie8(self.nazwa_pliku8, self.nazwa_stworzonego8)

        print("zadanie 9")
        self.nazwa_pliku9 = input("Podaj nazwę pliku, z informacja o macierzy:\n>> ")
        self.nazwa_stworzonego9 = input("Podaj nazwę pliku, w ktorym chcesz zapisać wynik:\n>> ")
        self.zadanie9(self.nazwa_pliku9, self.nazwa_stworzonego9)

        print("zadanie 10")
        self.nazwa_pliku10 = input("Podaj nazwę pliku, z informacja o macierzy:\n>> ")
        self.nazwa_stworzonego10 = input("Podaj nazwę pliku, w ktorym chcesz zapisać wynik:\n>> ")
        self.zadanie10(self.nazwa_pliku10, self.nazwa_stworzonego10)

        print("zadanie 11")
        self.nazwa_pliku11 = input("Podaj nazwę pliku, z informacja:\n>> ")
        self.nazwa_stworzonego11 = input("Podaj nazwę pliku, w ktorym chcesz zapisać wynik:\n>> ")
        self.zadanie11(self.nazwa_pliku11, self.nazwa_stworzonego11)

        print("zadanie 12")
        self.nazwa_pliku12 = input("Podaj nazwę pliku, z informacja:\n>> ")
        self.nazwa_stworzonego12 = input("Podaj nazwę pliku, w ktorym chcesz zapisać wynik:\n>> ")
        self.zadanie12(self.nazwa_pliku12, self.nazwa_stworzonego12)

    def zadanie1(self, ciag, nazwa):
        with open(nazwa, "w") as plik:
            plik.write(ciag)

    def zadanie2(self, nazwa_ist, nazwa_nie):
        with open(nazwa_ist, "r") as plik:
            liczby = plik.read()
            print(f"zawartosc pliku \"{nazwa_ist}\": " + liczby)
            liczby = liczby.strip().split(" ")
            numbers = [liczba for liczba in liczby if int(liczba) % 2 == 0]
            with open(nazwa_nie, "w") as plik_zapisz:
                for liczba in numbers:
                    plik_zapisz.write(str(liczba) + " ")

    def zadanie3(self, nazwa_pl, nazwa_nowa):
        with open(nazwa_pl, "r") as plik:
            cyfra = int(plik.readline())
            with open(nazwa_nowa, "w") as plik_do_zapisu:
                wynik = 1
                for i in range(1, cyfra + 1):
                    wynik *= i
                plik_do_zapisu.write(str(wynik))
                print("wynik dzialania: " + str(wynik))

    def zadanie4(dane, nazwa_pliku):
        slownik_miast = {}
        with open(dane, "r") as plik:
            for linia in plik:
                dane_miast = linia.split(":")
                nazwa_miasta = dane_miast[0].strip()
                mieszkancy = dane_miast[1].strip()
                slownik_miast[nazwa_miasta] = int(mieszkancy)
        with open(nazwa_pliku, "w+") as plik_do_zapisu:
            plik_do_zapisu.write(str(slownik_miast))
            print("wszystkie pobrane miasta:")
            print(slownik_miast)

    def zadanie5(nazwa_pliku, nazwa_stworzonego):
        with open(nazwa_pliku, 'r') as plik:
            input_string = plik.read()
        numbers = list(map(int, input_string.split()))
        filtered_numbers = [n for n in numbers if n % 2 == 0 and len(str(n)) == 4 and str(n)[1] == str(n)[2]]
        with open(nazwa_stworzonego, "w") as plik:
            plik.write(str(filtered_numbers))

    def zadanie6(nazwa_pliku, nazwa_stworzonego):
        with open(nazwa_pliku, 'r') as plik:
            input_string = plik.read()
        numbers = list(map(int, input_string.split()))
        print("zawartosc pliku: " + str(numbers))
        filtered_numbers = [n for n in numbers if n % 2 == 0 and len(str(n)) == 4 and str(n)[2] > str(n)[3]]
        with open(nazwa_stworzonego, "w") as plik:
            plik.write(str(filtered_numbers))

    def zadanie7(nazwa_pliku, nazwa_stworzonego):
        with open(nazwa_pliku, "r") as plik:
            dane = plik.readlines()
        wymiar = int(dane[0])
        skalar = int(dane[-1])
        macierz = []
        for i in range(1, wymiar + 1):
            row = list(map(int, dane[i].split(" ")))
            pomnozony_row = [liczba * skalar for liczba in row]
            macierz.append(pomnozony_row)
        with open(nazwa_stworzonego, "w") as plik_do_zapisu:
            for row in macierz:
                plik_do_zapisu.write(str(row) + '\n')

        print("wynikowa macierz: ")
        for i in range(wymiar):
            print(macierz[i])

    def zadanie8(nazwa_pliku, nazwa_stworzonego):
        with open(nazwa_pliku, "r") as plik:
            dane = plik.readlines()
        wymiar = int(dane[0])
        wektor = [int(liczba) for liczba in (dane[-1].split(" "))]
        macierz = []

        for i in range(1, wymiar + 1):
            row = list(map(int, dane[i].split(" ")))
            macierz.append(row)

        result = []
        for i in range(wymiar):
            sum_rzed = 0
            for j in range(wymiar):
                sum_rzed += macierz[i][j] * wektor[j]
            result.append(sum_rzed)

        with open(nazwa_stworzonego, "w") as plik_do_zapisu:
            for i in range(wymiar):
                plik_do_zapisu.write(str(result[i]) + '\n')

        print("twoja macierz: ")
        for i in range(wymiar):
            print(macierz[i])
        print("wynik mnozenia: ")
        for i in range(wymiar):
            print(result[i])

    def zadanie9(nazwa_pliku, nazwa_stworzonego):
        with open(nazwa_pliku, "r") as plik:
            dane = plik.readlines()
        wymiar = int(dane[0])
        macierz1 = []
        macierz2 = []
        for i in range(1, wymiar + 1):
            row = list(map(int, dane[i].split(" ")))
            macierz1.append(row)
        for i in range(wymiar + 1, wymiar * 2 + 1):
            row = list(map(int, dane[i].split(" ")))
            macierz2.append(row)

        print("I macierz:")
        for i in range(wymiar):
            print(macierz1[i])

        print("II macierz:")
        for i in range(wymiar):
            print(macierz2[i])

        result = [[0] * wymiar for i in range(wymiar)]
        for i in range(wymiar):
            for j in range(wymiar):
                result[i][j] = macierz1[i][j] + macierz2[i][j]
        print("suma macierzy:")
        for i in range(wymiar):
            print(result[i])

        with open(nazwa_stworzonego, "w") as plik_do_zapisu:
            for row in result:
                plik_do_zapisu.write(str(row) + '\n')

    def zadanie10(nazwa_pliku, nazwa_stworzonego):
        with open(nazwa_pliku, "r") as plik:
            dane = plik.readlines()
        wymiar = int(dane[0])
        macierz1 = []
        macierz2 = []
        for i in range(1, wymiar + 1):
            row = list(map(int, dane[i].split(" ")))
            macierz1.append(row)
        for i in range(wymiar + 1, wymiar * 2 + 1):
            row = list(map(int, dane[i].split(" ")))
            macierz2.append(row)

        print("I macierz:")
        for i in range(wymiar):
            print(macierz1[i])

        print("II macierz:")
        for i in range(wymiar):
            print(macierz2[i])

        result = [[0] * wymiar for i in range(wymiar)]
        for i in range(len(macierz1)):
            for j in range(len(macierz2[0])):
                for s in range(len(macierz2)):
                    result[i][j] += macierz1[i][s] * macierz2[s][j]

        print("wynik mnozenia dwoch macierzy:")
        for i in range(wymiar):
            print(result[i])

        with open(nazwa_stworzonego, "w") as plik_do_zapisu:
            for row in result:
                plik_do_zapisu.write(str(row) + '\n')

    def print_poly(coefs):
        wynik = ""
        for i in range(len(coefs)):
            if coefs[i] != 0:
                if i != len(coefs) - 1:
                    wynik += f"{coefs[i]}*x^{i} + "
                else:
                    wynik += f"{coefs[i]}*x^{i}"
        return wynik

    def zadanie11(nazwa_pliku, nazwa_stworzonego):
        with open(nazwa_pliku, "r") as plik:
            dane = plik.readlines()
        potega = int(dane[0].strip())
        coef1 = [int(liczba) for liczba in dane[1].split(" ")]
        coef2 = [int(liczba) for liczba in dane[2].split(" ")]

        result_coef = [0] * (potega + 1)

        print("pierwszy wielomonian:")
        print(print_poly(coef1))

        print("drugi wielomian:")
        print(print_poly(coef2))

        for i in range(len(coef1)):
            result_coef[i] = int(coef1[i]) + int(coef2[i])

        print("wynik:")
        print(print_poly(result_coef))

        with open(nazwa_stworzonego, "w") as plik_do_zapisu:
            plik_do_zapisu.write(str(print_poly(result_coef)))

    def zadanie12(nazwa_pliku, nazwa_stworzonego):
        with open(nazwa_pliku, "r") as plik:
            dane = plik.read()
        ciag = [int(liczba) * int(liczba) for liczba in dane.split(" ")]
        suma = 0
        for i in range(len(ciag)):
            suma += ciag[i]

        print("wynik dzialania: " + str(suma))

        with open(nazwa_stworzonego, "w") as plik_do_zapisu:
            plik_do_zapisu.write("wynik dzialania: " + str(suma))

zadanie = Dzialania_Na_Plikach()