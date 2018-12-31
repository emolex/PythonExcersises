#OBSLUGA PLIKOW- TRYBY WRITE I READ

f = open("dokument1","r+")   #JEST a+, KTORY NIE USUWA ZAWARTOSCI DANEGO PLIKU, ORAZ w+, KTORY USUWA ZA KAZDYM RAZEM ZAWARTOSC PLIKU.

numeracja = 0

f.write(" Liczby: "+"\n")

while numeracja<10:         #WYPISUJE LICZBY OD 1 DO 10 W PLIKU "dokument1"
    numeracja+=1
    f.write(str(numeracja)+"\n")



for x in f.readlines():     #WYPISUJE NA KONSOLI (ODCZYTUJE) ZAWARTOSC PLIKU, GDZIE DLA KAZDEGO ELEMENTU USUWA WSZYSTKIE ZNAKI BIALE
    print(x.strip())

f.close()