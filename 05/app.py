

class BankAccount:
    def __init__(self, owner: str, balance: int=0) -> None:
        self.owner = owner
        self.__balance = balance
    
    def deposit(self, amount: int) -> None:
        if amount > 0:
            self.__balance += amount
            print(f"Wpłacono kwotę {amount} PLN. Twój stan konta to {self.__balance} PLN")
        else:
            print("Wpłacana kwota musi być większa od 0 PLN")
    
    def withdraw(self, amount: str) -> str:
        if self.__balance < amount:
            print("Niewystarczające środki.")
        else:
            self.__balance -= amount
            print(f"Wypłacono kwotę {amount} PLN. Obecny stan konta to {self.__balance} PLN")
    
    def get_balance(self):
        print(f"Stan konta: {self.__balance} PLN")
        

if __name__ == "__main__":
    account = BankAccount("John", 1000)
    account.deposit(150)
    account.withdraw(400)
    account.get_balance()
    
    
        
        
    