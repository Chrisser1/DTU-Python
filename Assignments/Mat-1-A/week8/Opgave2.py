from Opgave1 import Person

class BankAccount():

    def __init__(self, account_number: int, account_owner: Person, saldo: float):
        self.__account_number: int = account_number
        self.__account_owner: Person = account_owner
        self.__saldo: float = saldo

    def deposit_amount(self, amount: int):
        self.__saldo += amount

    def withdraw_amount(self, amount: int):
        self.__saldo -= amount

    def show_saldo(self):
        if self.__saldo <= 100:
            print(f"Poor fuck, you owe money to the state and you only have {self.__saldo}")
        else:
            print(f"Good sir, you have about {self.__saldo} on your bank account")


class SavingsAccount(BankAccount):
    def __init__(self, account_number: int, account_owner: Person, saldo: float):
        super().__init__(account_number=account_number, account_owner=account_owner, saldo=saldo)
        self.__interest_rate: float = None

    def set_interest_rate(self, interest_rate: float):
        self.__interest_rate = interest_rate


class CheckingsAccount(BankAccount):
    def __init__(self, account_number: int, account_owner: Person, saldo: float, credit: float):
        super().__init__(account_number=account_number, account_owner=account_owner, saldo=saldo)
        self.__credit: float = credit

    def withdraw_with_credit(self, amount):
        self.__credit = max(self.__saldo - amount, self.__saldo - self.__credit)
