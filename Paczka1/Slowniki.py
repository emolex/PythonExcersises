kontaktySlownik = {
    "Jan Kowalski":1252555,
    "Maria Kowalsa": 56888998,
    "Jan Nowak": 555
}

odwrotnekontakty = {
    1:"Jan Kowalski",
    2:"Maria Nowak",
    3:"Jan Matejko"
}

for next in odwrotnekontakty:
    print("Numer",next,"TO:",odwrotnekontakty[next])


print("***************************************************************")
for imie, numer in kontaktySlownik.items():
    print(imie, "ma numer:", numer)

# for imie in kontaktySlownik:
#     print(imie, "ma numer o numerach:", kontaktySlownik[imie])

kontaktySlownik.pop("Jan Kowalski")


print("***************************** Nowa lista **********************************")
for imie in kontaktySlownik:
    print(imie, "ma numer o numerach:", kontaktySlownik[imie])