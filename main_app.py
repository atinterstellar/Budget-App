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

categories = []

class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.balance = 0
        categories.append(self)

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
        self.balance += amount

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            self.balance -= amount
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
        return amount <= self.balance

    def view_balance(self):
        print(self.get_balance())

    def view_ledger(self) :
        print(f"Ledger for {self.name}:")
        for entry in self.ledger:
            print(f"{entry['description']}: {entry['amount']}")

    def view_payements(self):
        print(f'Payments for {self.name}')
        for i in self.ledger:
            if i['amount'] < 0:
                print(f"{i['description']}: {i['amount']}")

    def view_credits(self):
        print(f'Credist for {self.name}')
        for i in self.ledger:
            if i['amount'] > 0:
                print(f"{i['description']}: {i['amount']}")
        
def total_balance():
    total = 0
    for category in categories:
        total += category.get_balance()
    return total

def view_all_payments():
    for category in categories :
        print(f"Payments for {category.name}:")
        for i in category.ledger :
            if i['amount'] < 0:
                print(f"{i['description']}: {i['amount']}")

def view_all_credits():
    for category in categories :
        print(f"Credits for {category.name}:")
        for i in category.ledger :
            if i['amount'] > 0:
                print(f"{i['description']}: {i['amount']}")

