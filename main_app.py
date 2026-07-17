import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
JSON_PATH = os.path.join(BASE_DIR, 'budget.json')

print("JSON_PATH:", JSON_PATH)
print("Exists?", os.path.exists(JSON_PATH))

def add_to_file(category):
    if os.path.exists(JSON_PATH):
        with open(JSON_PATH, 'r') as f:
            data = json.load(f)
    else:
        data = {}

    data[category.name] = {'ledger': category.ledger}

    with open(JSON_PATH, 'w') as f:
        json.dump(data, f, indent=4)

def read_file(category):
    if os.path.exists(JSON_PATH):
        with open(JSON_PATH, 'r') as f:
            data = json.load(f)
            if category.name in data:
                category.ledger = data[category.name]['ledger']
            else:
                category.ledger = []
    else:
        category.ledger = []

def add_master_to_file(m):
    if os.path.exists(JSON_PATH):
        with open(JSON_PATH, 'r') as f:
            data = json.load(f)
    else:
        data = {}

    data['__master__'] = {
        'savings': m.savings,
        'master_ledger': m.master_ledger
    }

    with open(JSON_PATH, 'w') as f:
        json.dump(data, f, indent=4)

def read_master_from_file(m):
    if os.path.exists(JSON_PATH):
        with open(JSON_PATH, 'r') as f:
            data = json.load(f)
            if '__master__' in data:
                m.savings = data['__master__']['savings']
                m.master_ledger = data['__master__']['master_ledger']
                return
    m.savings = 0
    m.master_ledger = []

categories = []
class master:
    def __init__(self, name) :
        self.name = name
        read_master_from_file(self)

    def total_balance(self):
        return sum(cat.balance for cat in categories)

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

    def save(self, amount) :
        self.savings += amount
        add_master_to_file(self)

    def view_savings(self) :
        return self.savings
    
    def with_sav(self,amount) :
        self.savings -= amount
        add_master_to_file(self)

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
Savings = Category('Savings')
Food = Category('Food')
Social = Category('Social')
Commute = Category('Commute')
Academic = Category('Academic')
Care = Category('Care')
Subscriptions = Category('Subscriptions')
Buffer = Category('Buffer')
Clothing = Category('Clothing')

Master = master('Master')

#--------SERVER CODE--------#

def get_category(name):
    for cat in categories:
        if cat.name == name:
            return cat
    return None