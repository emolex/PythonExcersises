import re
print("Wprawdz pin")
pin = input()

teskt = "tu jest kod pin "+pin+" o takiej tresci"
sciezka = r'\d\d\d\d'
dopasowanie = re.search(sciezka, teskt)
print(dopasowanie)
if dopasowanie:
    numer = dopasowanie.group()
    print("PIN to:",numer)