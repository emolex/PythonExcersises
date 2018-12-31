# MODULY ISM TWORZENIE FOLDEROW, LISTY PLIKOW

import os #MODUL, KTORY DAJE NAM SPORO FUNKCJI DLA SYSTEMU

lista = os.listdir("/home/emil/") #LISTUJE JAKIES KATALOGI
# print(lista)

lista1 = os.listdir(".")
# print(lista1)

for x in os.listdir("/home/emil/PycharmProjects/untitled/Paczka1"):
    # print(x)
    if os.path.isfile(x): #Sprawdza czy element jest plikiem
        print("{} Jest plikiem".format(x))
    else:print("{} nie jest plikiem".format(x))

    if os.path.isdir("/home/emil/"): #Sprawdza, czy element jest folderem
        print("{} jest folderem".format(x))

# TWORENIE FOLDERU
os.mkdir("pliczek")

# ZMIANA NAZWY PLIKU
os.rename("Kurs Skewoo", "Kurs Skewoo")

# TWORZENIE FOLDEROW
path = "pliki/01/"
# #TWORZENIE KATALOGOW (WIECEJ NIZ JEDEN)
os.makedirs(path)
print(path)
# TWORZENIE PLIKU
open("test.txt","w").close()


#TWORZENIE SCIEZKI FOLDEROW I UTWORZENIE PLIKOW
path = "folder1/01/data.txt"
dir_path = os.path.dirname(path)
print(dir_path)
os.makedirs(dir_path)
open(path, "w").close()






