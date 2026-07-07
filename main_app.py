import json
import os

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

