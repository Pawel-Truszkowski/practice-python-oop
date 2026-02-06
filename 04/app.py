

class Animal:
    def __init__(self, name: str):
        self.name = name
        
    def make_sound(self) -> str:
        return "Zwierzę wydaje dźwięk."
    

class Dog(Animal):
    def make_sound(self) -> str:
        return f"{self.name} szczeka: Hau! Hau!"
    
class Cat(Animal):
    def make_sound(self) -> str:
        return f"{self.name} miauczy: Miau! Miau!"
        
        
if __name__ == "__main__":
    animals = [Dog("Burek"), Cat("Mruczek"), Dog("Reksio")]

    for animal in animals:
        print(animal.make_sound())