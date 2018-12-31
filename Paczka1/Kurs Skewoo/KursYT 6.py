#LISTY- wolniejsze, ale da sie je edytować

produkty=["mleko","ser","kakao","parowki"]
dodatk_do_produktow = ["keczup", "majonez", "musztarda"]

print(produkty[0:2])
print(type(produkty))

produkty.append("kielbasa")
print(produkty)

produkty.extend(dodatk_do_produktow)
print("Po dodaniu z extend:",produkty)

produkty.insert(0,"masło")
print("Dopisanie do pierwszego elementu masła:",produkty)


#TUPLE - Są szybsze, choć nie mozemy ich edytować

produkty1 = ("mleko","ser","kakao","parowki")
print(type(produkty1))


#SLOWNIKI (DICTIONARY)

person = {"wiek":20,
          "imie":"Ania",
          "nazwisko":"Kowalska"}

print(type(person))
print(person)

print(person.get("wiek"))

print(person.keys())

print(person.values())

print(person.items())