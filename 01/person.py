
class Person:
    def __init__(self, name: str, age: int, city: str) -> None:
        self.name = name
        self.age = age
        self.city = city

    def introduce(self):
        print(f"Cześć, mam na imię {self.name}, mam {self.age}, i mieszkam w {self.city}.")
        


person1 = Person("Jan", 25, "Warszawa")
person2 = Person("Anna", 30, "Kraków")
person3 = Person("Piotr", 35, "Gdańsk")

person1.introduce()
person2.introduce()
person3.introduce()
        