from datetime import datetime

from statement_printer import StatementPrinter
from transaction import Transaction
from transaction_repository import TransactionRepository


class Account:
    def __init__(self, transaction_repository=None, statement_printer=None, date_provider=None):
        self._transaction_repository = transaction_repository or TransactionRepository()
        self._statement_printer = statement_printer or StatementPrinter()
        self._date_provider = date_provider or self._default_date_provider
        self._balance = 0

    def deposit(self, amount):
        self._register_transaction(amount)

    def withdraw(self, amount):
        self._register_transaction(-amount)

    def printStatement(self):
        self._statement_printer.print_statement(self._transaction_repository.all())

    def _register_transaction(self, amount):
        self._balance += amount
        transaction = Transaction(self._date_provider(), amount, self._balance)
        self._transaction_repository.add(transaction)

    def _default_date_provider(self):
        return datetime.now().strftime("%d/%m/%Y")