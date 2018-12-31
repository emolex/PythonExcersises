#Pętla while

i=0

while i<=10:
    print(i)
    i+=1

print("KONIEC")


j=10
while j>=0:
    print(j)
    j-=1

##############################################################

suma=0

while True:
    print("Wpisz liczbe:")
    x=input()
    suma += int(x)
    print(suma)
    if suma>100:
        break
