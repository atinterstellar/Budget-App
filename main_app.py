import json
import os

def add_to_file(category):
    if os.path.exists('budget.json'):
        with open('budget.json', 'r') as f:
            data = json.load(f)
    else:
        data = {}

    data[category.name] = {'ledger': category.ledger}
    
    with open('budget.json', 'w') as f:
        json.dump(data, f, indent=4)

def read_file(category):
    if os.path.exists('budget.json'):
        with open('budget.json', 'r') as f:
            data = json.load(f)
            if category.name in data:
                category.ledger = data[category.name]['ledger']
            else:
                category.ledger = []
    else:
        category.ledger = []

categories = []
class master:
    def __init__(self) :
        self.balance = 0
        for i in categories :
            self.balance += i.balance
        self.master_ledger = []

    def deposit_master(self,amount) :
        perc = 100
        for i in categories:
            print(f' To {i}')
            trans = int(input(f'Enter percentage ( max = {perc} ) to be transferred : '))
            if trans <= perc :
                per_cat = trans*amount/100
                i.deposit(per_cat, 'Master Deposit')
                perc -= trans
                print(f'{trans}% of {amount} added to {i.name}')
                self.master_ledger.append({ 'amount' : -per_cat , 'description' : f'To {i.name}' })

class Category:
    def __init__(self, name):
        self.name = name
        read_file(self)
        self.balance = 0
        for i in self.ledger:
            self.balance += i['amount']
        categories.append(self)

    def deposit(self, amount, description=""):
        if amount < 0:
            return "Amount can't be -ve"
        if not isinstance(amount , (int , float) ):
            return "Amount must be integer"
        self.ledger.append({"amount": amount, "description": description})
        self.balance += amount
        add_to_file(self)

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            self.balance -= amount
            add_to_file(self)
            return True
        return False

    def get_balance(self):
        return self.balance

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def view_balance(self):
        print(self.get_balance())

    def view_ledger(self) :
        print(f"Ledger for {self.name}:")
        for entry in self.ledger:
            print(f"{entry['description']}: {entry['amount']}")

    def view_payments(self):
        print(f'Payments for {self.name}')
        for i in self.ledger:
            if i['amount'] < 0:
                print(f"{i['description']}: {i['amount']}")

    def view_credits(self):
        print(f'Credits for {self.name}')
        for i in self.ledger:
            if i['amount'] > 0:
                print(f"{i['description']}: {i['amount']}")

    def get_exp(self):
        exp = 0
        for entry in self.ledger:
            if entry['amount'] < 0:
                exp -= entry['amount']
        return exp
        
def total_balance():
    return master.balance

def view_all_payments():
    total_exp = 0
    for category in categories :
        print(f"Payments for {category.name}:")
        for i in category.ledger :
            if i['amount'] < 0:
                total_exp = total_exp - i['amount']
                print(f"{i['description']}: {i['amount']}")
    print(total_exp)

def get_total_exp() :
    total = 0
    for category in categories :
        for i in category.ledger :
            if i['amount'] < 0:
                total = total - i['amount']
    return total

def view_all_credits():
    for category in categories :
        print(f"Credits for {category.name}:")
        for i in category.ledger :
            if i['amount'] > 0:
                print(f"{i['description']}: {i['amount']}")

def view_perc_bal() :
    m_bal = master.balance
    for cat in categories:
        perc = (cat.balance * 100)/m_bal
        print(f'{cat.name} : {perc}')

def view_expenses() :
    total = 0
    print('Expenses')
    for cat in categories:
        print(f'{cat.name} : {cat.get_exp()} ')
        total += cat.get_exp()
    print(f'Total Expense : {total}')
    
def view_expenses_by_perc() :
    total = get_total_exp()
    print('Expenses by percentage')
    for cat in categories:
        perc= cat.get_exp() * 100 / total
        print(f'{cat.name} : {perc} ')

food = Category('Food')
rent = Category('rent')

