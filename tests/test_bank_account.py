import pytest
from bank_account.bank_account import BankAccount


@pytest.fixture
def start_account():
    return BankAccount(100)

@pytest.fixture
def second_account():
    return BankAccount(100)

def test_negative_initial_balance():
    with pytest.raises(ValueError):
        BankAccount(-100)

def test_positve_deposit(start_account):
    start_account.deposit(50)
    assert start_account.balance == 150

def test_negative_deposit(start_account):
    with pytest.raises(ValueError):
        start_account.deposit(-100)

def test__positive_withdraw(start_account):
    start_account.withdraw(50)
    assert start_account.balance == 50

def test_negative_withdraw(start_account):
    with pytest.raises(ValueError):
        start_account.withdraw(-10)
    

def test_transfer_to(start_account, second_account):
    start_account.transfer_to(second_account, 50)

    assert start_account.balance == 50
    assert second_account.balance == 150


def test_transfer_to_invalid_target(start_account):
    with pytest.raises(ValueError):
        start_account.transfer_to("not-an-account", 50)


def test_transfer_to_insufficient_funds(start_account, second_account):
    with pytest.raises(ValueError):
        start_account.transfer_to(second_account, 200)

