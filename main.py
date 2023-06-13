import re

class Client:
    def __init__(self, name, age, gender, address, phone, email):
        assert re.search(r'@',email), f"Not a valid email address."
        self.total_deposit = 0
        self.total_withdraw = 0
        self.withdraw_amount = 0
        self.__balance = 0 # private attribute
        self.name = name
        self.age = age
        self.gender = gender
        self.address = address
        self.phone = phone
        self.email = email

    def get_client_info(self):
        print(
            f"Name : {self.name}, \tAge : {self.age}, \t Gender : {self.gender}, \tAddress : {self.address} \tPhone : {self.phone},\tEmail : {self.email}")

    def deposit(self, deposit_amount):
        self.total_deposit += deposit_amount
        self.__balance += deposit_amount
        print(f"{self.name} deposited {deposit_amount}.")

    def withdraw(self, withdraw_amount):
        if withdraw_amount > self.balance:
            print(
                f"Can't withdraw, balance is less than withdraw amount. {self.name}, you can withdraw only upto your balance : {self.balance}.")
            return
        self.total_withdraw += withdraw_amount
        self.__balance -= withdraw_amount
        print(f"{self.name} has withdrawn {withdraw_amount}.")

    def total_balance(self):
        print(f"Total balance of {self.name} is {self.balance}.")
        return self.balance

    @property
    # property decorator = Read Only Attribute
    def balance(self):
        return self.__balance


client1 = Client("Pratha", "22", "f", "Nepal", "2372323", "ps@djsbds.com")
client2 = Client("Max", 30, "m", "USA", "2873728", "skbj@sgmail.com")

client1.deposit(200)
client1.deposit(500)
client1.withdraw(150)
client1.withdraw(300)
client1.total_balance()

# client2.withdraw(21)
