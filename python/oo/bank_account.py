class bankaccount:
    def __init__(self):
        self.balance = 0

    def withdraw(self, amount):
        self.balance -= amount
        return (self.balance)

    def deposit(self, amount):
        self.balance += amount
        return (self.balance)

aobj = bankaccount()
print aobj
print '-----------------------------------'
bobj = bankaccount()
print bobj.withdraw(50)
print '-----------------------------------'
cobj = bankaccount()
print cobj.deposit(100)
