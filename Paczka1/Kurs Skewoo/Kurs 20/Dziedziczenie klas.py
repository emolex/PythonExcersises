import sys
class Person ():

    def __init__(self, name, surname, age):
        self.name=name
        self.surname=surname
        self.age=age

class Employee(Person):

    def __init__(self, name,  surname, age, position, specialization, salary):
        super().__init__(name, surname, age)
        self.position = position
        self.specialization = specialization
        self.salary = salary
        print( name,  surname, age, position, specialization, salary)

class Client(Person):
    def __init__(self):
        super().__init__("Marta")
        self.orders = "Strona internetowa"


pracownik1=Employee("Emilos","Czersky",28,"Programmer","Python",2000.76)

# klient1 = Client()
# print(klient1.name, klient1.orders)
