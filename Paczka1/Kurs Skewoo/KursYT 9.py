fruits = ["apple", "orange", "pear", "banana","apple"]

# for i in enumerate(fruits):
#     print(i)

print("START")
for index, fruit in enumerate(fruits): #pętla for przyjmuje 2 argumenty. Dla kazdego indexu
    print("Sprawdzam {}".format(index)) #FUNKCJA FORMAT- w klamrach pozniej dodaje zmienne
    if index == 3:
        break
    # print(index, fruit)
    print("{} jest ok".format(fruit))

print("KONIEC")