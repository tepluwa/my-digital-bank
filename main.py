import datetime

class Account:
    auto_account_number = 1234567890
    
    def __init__(self, currency: str, initial_balance: float = 0):
        self._account_number = Account.auto_account_number
        Account.auto_account_number += 1
        self.currency = currency
        self.initial_balance = initial_balance
        self.timestamp = datetime.datetime.now()

    @property #decorators
    def account_number(self):
        return self._account_number

    @account_number.setter
    def account_number(self):
        pass

class Client:
    def __init__(self, name: str):
        self.name = name
        self.timestamp = datetime.datetime.now()
        self.accounts = []

    def add_account(self, account: Account):
        self.accounts.append(account)

    def print_accounts(self):
        print(f'Accounts of client {self.name}')
        for acc in self.accounts:
            print(f'{acc.account_number} ({acc.currency} {acc.initial_balance})')        

class Transaction:
    def __init_(self, amount: float = 0, note: str = ''):
        self.amount = amount
        self.note = note
        self.timestamp = datetime.datetime.now()
  

#UZDEVUMS: izveido metodu klientiem, kas izdrukā visus lklienta kontus šādā formātā:
#PIEMĒRS
#Accounts of client Anna
#1234567890 (EUR 200)
#1234567891 (USD 150)
#1234567892 (CAD 300)  


clients = []
clients.append(Client('Margo'))
clients.append(Client('Simone'))
clients.append(Client('Rohini'))

clients[0].add_account(Account('EUR', 800))
clients[0].add_account(Account('USD', 1050))
clients[0].add_account(Account('CAD', 3000))

clients[1].add_account(Account('EUR', 1000))
clients[1].add_account(Account('JPY', 20000))

clients[2].add_account(Account('EUR'))

clients[1].accounts[1]._account_number = '999999999999'

for client in clients:
    client.print_accounts()
