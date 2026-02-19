import pytest
from bank_account.bank_account import BankAccount


@pytest.fixture
def start_account():
    return BankAccount(100)


def test_deposit(start_account):
    start_account.deposit(50)
    assert start_account.balance == 150
