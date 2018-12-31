imie = "Robert"
wiek = 27
print(not False)
tablica = [1, 2, 3, 4]

if imie =="Emil" and wiek == 27:
    print("Masz na imie", imie, "i masz", wiek, "lat")
else: print("Jestes oszustem")

if imie in ["Emil", "Robert"]:
    print("To imie znajdue sie w tablicy")
elif imie != "Wojtek":
    print("To nie jest Emil")
else:"Nic juz nie wiem"

if len(tablica)>3:
    print("Tablica ma wiecej niz 3 miejsca")

###########################

print("Zgadnij liczbe")
x=int(input())
if x==(4):
    print("Zgadza się")
else:
    print("Nie zgadza sie")


####################################33

lista = [2,4,5,6,7]
print("Podaj liczbe do sprawdzenia w tablicy:")
x = int(input())
if not x in lista:
    print("Nie ma tej cyfy  tablicy")
else:print("Liczba jest w tablicy")
