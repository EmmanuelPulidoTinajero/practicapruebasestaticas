class StatementPrinter:
    def print_statement(self, transactions):
        print("DATE | AMOUNT | BALANCE")

        for transaction in reversed(transactions):
            print(
                f"{transaction.date} | {transaction.amount:.2f} | {transaction.balance:.2f}"
            )