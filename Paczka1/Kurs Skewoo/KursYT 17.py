
try:
    plik = open("test.txt", "r")
    plik.write("Y")
    plik.close()

except FileNotFoundError as e:
    print("ERROR: No such file!")
    print(e)
except:
    print("Nieznany błąd")


