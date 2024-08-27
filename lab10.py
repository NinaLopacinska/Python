import statistics
import matplotlib.pyplot as plt
import numpy as np

def podaj_ciag_liczb(file, op):
    try:
        with open('c://temp//' + file, 'r') as f1:
            liczby = f1.readlines()
            liczbyInt = [int(x.strip()) for x in liczby]

        if op == "1":
            result = sum(liczbyInt)
        elif op == "2":
            result = max(liczbyInt)
        elif op == "3":
            result = min(liczbyInt)
        elif op == "4":
            result = sum(liczbyInt) / len(liczbyInt)
        elif op == "5":
            result = statistics.median(liczbyInt)
        elif op == "6":
            result = statistics.pstdev(liczbyInt)
        elif op == "7":
            result = statistics.stdev(liczbyInt)
        elif op == "8":
            result = statistics.pvariance(liczbyInt)
        elif op == "9":
            result = statistics.variance(liczbyInt)
        else:
            raise ValueError("Niepoprawny numer operacji.")
        return result

    except FileNotFoundError:
        return "Podany plik nie istnieje."
    except ValueError as e:
        return str(e)
    except Exception as e:
        return f"Wystąpił błąd: {e}"

if __name__ == '__main__':
    print(" 1 - suma\n 2 - wartość maksymalna\n 3 - wartość minimalna\n 4 - średnia arytmetyczna\n 5 - mediana\n 6 - odchylenie standardowe dla populacji\n 7 - odchylenie standardowe dla próbki\n 8 - wariancja dla populacji\n 9 - wariancja dla próbki")
    file1 = input("Podaj nazwę pliku: \n")
    nr_opcji = input("Podaj numer operacji od 1 do 9: \n")
    result = podaj_ciag_liczb(file1, nr_opcji)
    print(result)

# Rysowanie wykresu
x = np.linspace(0, 2 * np.pi, 1000)
y = 2 * np.sin(3 * x) + 3 * np.cos(2 * x)

plt.plot(x, y)
plt.title("Wykres funkcji y = 2*sin(3x) + 3*cos(2x)")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()
