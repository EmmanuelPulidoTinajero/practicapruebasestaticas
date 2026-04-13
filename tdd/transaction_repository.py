class TransactionRepository:
    def __init__(self):
        self._transactions = []

    def add(self, transaction):
        self._transactions.append(transaction)

    def all(self):
        return list(self._transactions)