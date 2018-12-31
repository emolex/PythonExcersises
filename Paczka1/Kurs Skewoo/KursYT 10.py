##Pomijanie iteracji (continue)
import Paczka1.Funkcje
fruits = ["apple", "orange", "pear", "banana","apple"]

print("START")

for index in fruits:

    if index =="orange":
        print("To jest orange")
        continue
    print(index)
    if index =="banana": break

print("KONIEC")