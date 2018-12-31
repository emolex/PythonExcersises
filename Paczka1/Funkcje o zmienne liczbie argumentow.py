def foo (pierwszy, drugi, trzeci, *reszta): #Ostatni argument moze przyjmowac kazdy typ jaki tylko chcemy i ile chcemy
    print("Pierwszy", pierwszy)
    print("Drugi",drugi)
    print("Trzcie", trzeci)
    print("I cała reszta...", list(reszta))

print(foo(1,2,3,4,"Pięć"))


def funkcja (pierwsza, druga, trzecia, **opcje): # 2 gwiazdki (**) sa uzywanne do przypisania, robienia slowa-kluczy
    if opcje.get("akcja")=="dodaj":
        print("Suma to:",(pierwsza+druga+trzecia))

    if opcje.get("akcja")=="iloczyn":
        print("Iloczyn to:",pierwsza*druga*trzecia)

        if opcje.get("zwroc")=="pierwsza":
            return pierwsza


wynik = funkcja(1,3,5, akcja="iloczyn")
print(wynik)

def foo1 (*zmienna3):
    return print(list(zmienna3))

def bar  (*magicznaLiczba):

    wywoalnie = foo1(1,22,45,32,543,1331,5555)