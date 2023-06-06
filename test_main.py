from main import Bank
import pytest

class TestBank:

    def test_create_bank(self):
        bank = Bank()
        assert bank.amount == 0

    def test_add_money(self):
        bank = Bank()
        bank.add_money(100)

        assert bank.amount == 100
    
    def test_withdraw_money(self):
        bank = Bank()
        bank.amount = 110
        bank.withdraw_money(100)

        assert bank.amount == 10