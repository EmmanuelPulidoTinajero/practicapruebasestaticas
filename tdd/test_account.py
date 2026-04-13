from unittest.mock import Mock, patch

from account import Account
from statement_printer import StatementPrinter
from transaction import Transaction
from transaction_repository import TransactionRepository


def test_deposit_records_transaction_with_balance():
    date_provider = Mock(return_value="01/04/2014")
    repository = TransactionRepository()
    account = Account(transaction_repository=repository, date_provider=date_provider)

    account.deposit(1000)

    assert repository.all() == [Transaction("01/04/2014", 1000, 1000)]


def test_withdraw_records_negative_transaction_and_updated_balance():
    date_provider = Mock(side_effect=["01/04/2014", "02/04/2014"])
    repository = TransactionRepository()
    account = Account(transaction_repository=repository, date_provider=date_provider)

    account.deposit(1000)
    account.withdraw(100)

    assert repository.all() == [
        Transaction("01/04/2014", 1000, 1000),
        Transaction("02/04/2014", -100, 900),
    ]


def test_print_statement_delegates_to_statement_printer():
    date_provider = Mock(side_effect=["01/04/2014", "02/04/2014"])
    repository = TransactionRepository()
    statement_printer = Mock()
    account = Account(
        transaction_repository=repository,
        statement_printer=statement_printer,
        date_provider=date_provider,
    )

    account.deposit(1000)
    account.withdraw(100)
    account.printStatement()

    statement_printer.print_statement.assert_called_once_with(repository.all())


def test_statement_printer_prints_transactions_in_reverse_order():
    transactions = [
        Transaction("01/04/2014", 1000, 1000),
        Transaction("02/04/2014", -100, 900),
        Transaction("10/04/2014", 500, 1400),
    ]
    printer = StatementPrinter()

    with patch("builtins.print") as mock_print:
        printer.print_statement(transactions)

    assert mock_print.call_args_list == [
        (("DATE | AMOUNT | BALANCE",), {}),
        (("10/04/2014 | 500.00 | 1400.00",), {}),
        (("02/04/2014 | -100.00 | 900.00",), {}),
        (("01/04/2014 | 1000.00 | 1000.00",), {}),
    ]