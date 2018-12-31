napis = "Odwazny lis skacze nad wilkiem"
slowa = napis.split() #oddziela kaze slowo i tworzy z nich oddzilne elementy tablicy
print(slowa)
dlugosc_slow=[]
for slowo in slowa:
    if slowo!="nad":
        dlugosc_slow.append(len(slowo))

print(dlugosc_slow)

#Zapis za pomoca listy skadanej

napis1 = "Odwazny lis skacze nad wilkiem"
slowa1=napis1.split()
dlugosc_slow1 = [len(slowo1)for slowo1 in slowa1 if slowo1!="nad"]
print(dlugosc_slow1)


liczby = [-1, -14,0,12.2,2,5.5,43]
nowa =  [int(zmienna) for zmienna in liczby if zmienna>0] #rzutowanie wszystkich liczb na intiger, za pomoca int(zmienna)
print(nowa)