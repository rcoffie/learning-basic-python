class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        print(f"__init__ Account created with {self.balance} balance")

    def getbalance(self):
        return self.balance

    def __repr__(self):
        return "__repr__ Account ({}, {})".format(self.name, self.balance)

    def __str__(self):
        return "__str__ Account name = {} and Account Balance = {}".format(
            self.name, self.balance
        )

    def __int__(self):
        return int(self.balance)

    def __float__(self):
        return float(self.balance)

    def __lt__(self, obj):
        try:
            return self.balance < obj.getbalance()
        except:
            return "Are you sure you are comparing two bank accounts"

    def _del__(self):
        self.balance = 0
        print("__del__ Account deleted")


"""Creating the matildas account"""
matildas_account = BankAccount("matilda", 3000)

"""creating deborah's account"""
deborah_account = BankAccount("Deborah", 3455)

"""checking deborah's account balance """
deborah_balance = deborah_account.getbalance()

"""'getting matildas account balance """
matildas_balance = matildas_account.getbalance()

"""' print debroah's account balance """
print(deborah_balance)

"""' returning string using str dunder method"""
print(str(deborah_account))

""" returning string user repr dunder  method  """
print(repr(matildas_account))

"""' printing balance in integer form """
print(int(deborah_balance))

"""printing balance in float form """
print(float(matildas_balance))

""" comparing account balance using __lt__  dunder method"""
compare = deborah_account > matildas_account
print(compare)
