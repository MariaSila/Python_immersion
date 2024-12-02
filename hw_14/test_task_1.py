import pytest
from task_1 import BankAccount, InsufficientFundsError


@pytest.fixture
def arg_default():
    obj = BankAccount()
    return obj


@pytest.fixture
def arg_set():
    obj = BankAccount(10)
    return obj


def test_init_err():
    with pytest.raises(ValueError):
        BankAccount('10')
        BankAccount(-10)


def test_init(arg_default, arg_set):
    assert arg_default.get_balance() == 'Сумма на счете 0'
    assert arg_set.get_balance() == 'Сумма на счете 10'


def test_deposit(arg_default, arg_set):
    arg_default.deposit(100)
    arg_set.deposit(2.5)
    assert arg_default.get_balance() == 'Сумма на счете 100'
    assert arg_set.get_balance() == 'Сумма на счете 12.5'
    arg_default.deposit(12.5)
    arg_set.deposit(50)
    assert arg_default.get_balance() == 'Сумма на счете 112.5'
    assert arg_set.get_balance() == 'Сумма на счете 62.5'


def test_deposit_err(arg_default):
    with pytest.raises(ValueError):
        arg_default.deposit('10')
        arg_default.deposit(-10)


def test_withdraw(arg_set):
    arg_set.withdraw(10)
    assert arg_set.get_balance() == 'Сумма на счете 0'


def test_withdraw_err(arg_default, arg_set):
    with pytest.raises(InsufficientFundsError):
        arg_default.withdraw(10)
    with pytest.raises(ValueError):
        arg_default.withdraw('10')
        arg_default.withdraw(-10)


if __name__ == '__main__':
    pytest.main(['-v'])



