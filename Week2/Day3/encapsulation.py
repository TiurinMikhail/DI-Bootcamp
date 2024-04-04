class AtmAccount:
    available_number = 500
    def __init__(self,holder):
        self.__holder = holder
        self._balance = 0.0
        self.__account_number = AtmAccount.available_number
        AtmAccount.available_number += 1

    def deposit(self,amount):
        self._balance += amount

    @property
    def get_holder(self):
        return self.__holder

    @property
    def balance(self):
        return self._balance

    @property
    def funds(self):
        return self._balance

    @funds.setter
    def _funds(self,amount):
        self._balance = amount


    def withdraw(self, amount):
        self._balance -= amount
        return self.balance

    #Dunder methods

    def __str__(self):
        output = f'''
        Account Number: {self.__account_number} 
        Holder: {self.__holder} 
        Balance: {self._balance}
        '''
        return output

    def __iadd__(self,amount):
        self.deposit(amount)
        return self

if __name__ == '__main__':
    account1 = AtmAccount('John Doe')
    account1.deposit(200)
    print(account1)
    print(account1.balance)
    print(account1.get_holder)
    account2 = AtmAccount('John Meanor')
    account3 = AtmAccount('John Dossen')
    print(account1._AtmAccount__account_number)
    print(account2._AtmAccount__account_number)
    print(account2._AtmAccount__account_number)

class Circle:
    color = "red"

    def __init__(self, diameter):
        self.diameter = diameter

    def grow(self, factor=2):
        self.diameter = self.diameter * factor

    def get_color(self):
       return Circle.color

circle1 = Circle(2)
print(circle1.color)
print(Circle.color)
print(circle1.get_color())
circle1.grow(3)
print(circle1.diameter)