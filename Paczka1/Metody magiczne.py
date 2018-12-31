class Calcurator():

    def __init__(self):
        print("\n******************************* init- zainicjowanie instancji *******************************")

    def __del__(self):
        print("delete- usuwanie instancji")

    def __str__(self):
        # print("String- przekonwertuje klase na ciąg znaków:")
        return "Info"

    def __int__(self):
        return 20

    def __len__(self):
        print("Dlugosc kalkulatora to:")
        return 5

    def __bool__(self):
        return False


    def add(self, a, b):
        wynik = a+b
        print("Wynik dodawania to:",wynik)

    def subtract (self, a , b):
        wynik=a-b
        print("Wynik odejmowania to:",wynik)




calc = Calcurator()
calc.add(5,10)
print(len(calc))

calc2 = Calcurator()
wynik = int(calc2)  + 50 #dodaje to, co w magicznej metodzie, czyli 20 + 50 = 70
print("Metoda __int__ + liczba, ktora podalem w obiekcie calc2:",wynik)

calc3 = Calcurator()
if calc3:
    print("Obiekt calc3: True")
else:
    print("Obiekt calc3: False")







