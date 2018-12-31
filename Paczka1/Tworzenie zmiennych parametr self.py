class Calcurator():

    def __init__(self): ## WYKONUJE SIE PRZY TWORZENIU KAZDEJ INTANCJI
        print("\n******************************* init- zainicjowanie instancji *******************************")
        self.liczba = 10 #NOWA ZMIENNA, KTORA BEDZIE DOSTEPNA W KAZDEJ INSTANCJI
        self.last_result =0


    def add(self, a, b):
        result = a+b
        self.last_result = result #Tutaj przechowujemy ostatni wynik ze zmiennej wynik
        print("Wynik dodawania to:",result)

    def subtract (self, a , b):
        result=a-b
        self.last_result = result
        print("Wynik odejmowania to:",result)

calc = Calcurator()
calc.liczba=100
calc.liczba+=10
print(calc.liczba)

calc2 = Calcurator()
calc2.liczba+=5
print(calc2.liczba)

calc3 = Calcurator()
calc3.add(5,20)
calc3.add(15,60)
calc3.subtract(80,70)
print("Ostatni wynik to: {}".format(calc3.last_result))