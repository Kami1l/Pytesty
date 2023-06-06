class Bank:

    def __init__(self):
        self.amount = 0
    
    def add_money(self, money:int):
        self.amount += money



class TestBank:

    def test_create_bank(self):
        bank = Bank()
        assert bank.amount == 0

    def test_add_money(self):
        bank = Bank()
        bank.add_money(100)

        assert bank.amount == 100