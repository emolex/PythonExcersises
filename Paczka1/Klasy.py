class MojaKlasa:

    zmienna = "Koala"
    def funkcja (self):
        print("To jest wiadomosc wewnatrz klasy: ")



class InnaKlasa:
        mojObiekt = MojaKlasa()
        mojObiekt.zmienna="wołowa"
        print(mojObiekt.zmienna)
        mojObiekt2 = MojaKlasa()
        mojObiekt2.funkcja()
        mojObiekt2.zmienna="schabowa"
        print(mojObiekt2.zmienna)

class Pojazd:
    kolor = "biały"
    rodzajj = ""
    wartosc = 0
    nazwa =""


pojazd = Pojazd
pojazd.kolor="czerwony"
pojazd.rodzajj = "kabriolet"
pojazd.wartosc = 60000
pojazd.nazwa = "Ferrari"
print(pojazd.kolor, pojazd.rodzajj, pojazd.wartosc, pojazd.nazwa)

pojazd2 = Pojazd
pojazd.kolor="niebieski"
pojazd.rodzajj = "autobus"
pojazd.wartosc = 100000
pojazd.nazwa = "Ikarus"
print(pojazd2.kolor, pojazd2.rodzajj, pojazd2.wartosc, pojazd2.nazwa)