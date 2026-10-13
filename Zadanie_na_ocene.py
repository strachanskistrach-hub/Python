from pathlib import Path

Plik = Path("uczniowie.txt")

def wczytaj(plik):
    with open(plik, "r", encoding="utf-8") as p:
        linie = p.readlines()

    dane = []
    for linia in linie:
        czysta = linia.strip()
        if czysta != "":
            dane.append(czysta)

    return dane

def wyswietl_menu():
    print("Menyu")
    print("1 Wyświetl listę uczniów")
    print("2 Posortuj listę alfabetycznie")
    print("3 Usuń ucznia z listy")
    print("4 Zakończ program")

def wyswietl_dane(dane):
    print("\nLista uczniów:")

    if len(dane) == 0:
        print("Lista jest pusta.")
    else:
        for element in dane:
            print(element)

def posortuj(dane, plik="posortowane.txt"):
    posortowane = dane.copy()
    posortowane.sort()

    with open(plik, "w", encoding="utf-8") as p:
        for element in posortowane:
            p.write(element + "\n")

    print(f"Posortowane dane zapisano do {plik}")
    return posortowane

def usun(dane, plik=Plik):
    if len(dane) == 0:
        print("Lista uczniow jest pusta")
        return

    wyswietl_dane(dane)
    uczen = input("Podaj imie i nazwisko ucznia do usuniecia: ").strip()

    if uczen in dane:
        dane.remove(uczen)

        with open(plik, "w", encoding="utf-8") as p:
            for element in dane:
                p.write(element + "\n")

        print(f"Usunięto ucznia: {uczen}")
    else:
        print("Nie znaleziono takiego ucznia na liście.")

def main():
    try:
        dane = wczytaj(Plik)
    except FileNotFoundError:
        print("Nie ma pliku uczniowie.txt")
        return

    while True:
        wyswietl_menu()
        wybor = input("Wybierz opcję 1-4: ").strip()
        if wybor == "1":
            wyswietl_dane(dane)
        elif wybor == "2":
            dane = posortuj(dane)
        elif wybor == "3":
            usun(dane)
        elif wybor == "4":
            print("Koniec programu.")
            break
        else:
            print("Zły wybór. Wybierz opcję od 1 do 4.")

main()