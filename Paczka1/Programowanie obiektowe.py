class Calcurator():

    def add(self, a, b):
        wynik = a+b
        print(wynik)

    def subtract (self, a , b):
        wynik=a-b
        print(wynik)


calc = Calcurator()

calc.add(5,10)
calc.subtract(10,2)

calc2 = Calcurator
calc2.mro(4)