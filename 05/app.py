

class BankAccount:
    def __init__(self, owner: str, balance: int=0) -> None:
        self.owner: str = owner
        self.__balance: int = balance
    
    def deposit(self, amount: int) -> None:
        if amount > 0:
            self.__balance += amount
            print(f"Wpłacono kwotę {amount} PLN. Twój stan konta to {self.__balance} PLN")
        else:
            print("Wpłacana kwota musi być większa od 0 PLN")
    
    def withdraw(self, amount: int) -> None:
        if amount <= 0:
            print("Wypłacana kwota musi być większa od zera!")
        else:
            if self.__balance < amount:
                print("Niewystarczające środki.")
            else:
                self.__balance -= amount
                print(f"Wypłacono kwotę {amount} PLN. Obecny stan konta to {self.__balance} PLN")
    
    def get_balance(self) -> None:
        print(f"Stan konta: {self.__balance} PLN")
        

if __name__ == "__main__":
    account = BankAccount("John", 1000)
    account.deposit(400)
    account.withdraw(100)
    account.withdraw(-100)
    account.get_balance()
    
    
        
        
    