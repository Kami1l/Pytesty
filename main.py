class Bank:

    def __init__(self):
        self.amount = 0
    
    def add_money(self, money:int):
        self.amount += money

    def withdraw_money(self, withdraw:int):
        if self.amount < withdraw:
            raise ValueError("Za mało pieniędzy")
        else:
            self.amount -= withdraw
