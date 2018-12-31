pierwsze = [2,3,5,7,8]
for pierwsza in pierwsze:
    if pierwsza%2==0:
        print ("liczba pierwsza: ", pierwsza)


#wpisze liczby od 0 do 4
for x in range(5):
    print(x)

#wypisze od liczby 2 do 5
for x in range (2,5):
        print(x)


#pętle WHILE
licznik =0
while licznik <5:
    print("licznik: ",licznik)
    licznik+=1

#break
licznik2=0
while True:
    print(licznik2)
    licznik2+=1
    if licznik2>=5:
        break

#continue z uzyciem wyszukania liczby pierwszej
pierwszaLiczba=0
for x in range(100):
    y=x
    if (y%3!=0 and y%2!=0 and y%5!=0 and y%7!=0):
        print("pierwsza liczba: ", x)
        continue