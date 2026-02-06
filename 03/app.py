

class Employee:
    def __init__(self, name: str, position: str) -> None:
        self.name = name
        self.position = position
        
    def describe(self) -> str:
        return f"{self.name} pracuje na stanowisku {self.position}."


class Teacher(Employee):
    def __init__(self, name: str, position: str, subject: str) -> None:
        super().__init__(name, position)
        self.subject = subject
        
    def describe(self) -> str:
        return f"{super().describe()} Uczy przedmiotu {self.subject}."    


class Doctor(Employee):
    def __init__(self, name: str, position: str, specialization: str) -> None:
        super().__init__(name, position)
        self.specialization = specialization

    def describe(self) -> str:
        return f"{self.name} jest lekarzem specjalizującym się w {self.specialization}."


if __name__ == "__main__":
    employee = Employee("Jan Kowalski", "Menedżer")
    teacher = Teacher("Joann Dark", "Nauczycyiel", "Matematyka")
    doctor = Doctor("Piotr Zieliński", "Lekarz", "kardiologii")


    print(employee.describe())
    print(teacher.describe())
    print(doctor.describe())
