import datetime
import pytz


menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

balance = 0
limit = 500
statement = ""
datetime_transaction = None
number_transactions = 0
LIMIT_TRANSACTIONS = 10
now = datetime.datetime.now(pytz.timezone("America/Sao_Paulo"))

def daily_reset(datetime_last_transaction, insert_number_transactions):

    if datetime_last_transaction is None or datetime_last_transaction.date() != now.date():
        insert_number_transactions = 0
        datetime_last_transaction = now 

    return insert_number_transactions, datetime_last_transaction

def deposit(insert_value, insert_balance, insert_statement, insert_number_transactions, datetime_last_transaction):

    insert_number_transactions, datetime_last_transaction = daily_reset(datetime_last_transaction, insert_number_transactions)

    if insert_number_transactions < LIMIT_TRANSACTIONS:
        if insert_value <= 0:
            return insert_balance, insert_statement, insert_number_transactions, datetime_last_transaction, "Depósito negado"
        else:
            insert_balance += insert_value
            insert_statement += f"Depósito: R${insert_value:.2f}\nHorário: {datetime.datetime.now()}\n"
            insert_number_transactions += 1
            return insert_balance, insert_statement, insert_number_transactions, datetime_last_transaction, "Depósito realizado"
    else:
        return insert_balance, insert_statement, insert_number_transactions, datetime_last_transaction, "Limite de transações diárias excedido"
    
def withdrawal(insert_value, insert_balance, insert_statement, insert_number_transactions, datetime_last_transaction):

    insert_number_transactions, datetime_last_transaction = daily_reset(datetime_last_transaction, insert_number_transactions)
    
    if insert_number_transactions < LIMIT_TRANSACTIONS:
        if insert_value > 0 and insert_value <= limit:
            if insert_value <= insert_balance:
                insert_balance -= insert_value
                insert_statement += f"Saque: R${insert_value:.2f}\nHorário: {datetime.datetime.now()}\n"
                insert_number_transactions += 1
                return insert_balance, insert_statement, insert_number_transactions, datetime_last_transaction, "Saque realizado"
            else:
                return insert_balance, insert_statement, insert_number_transactions, datetime_last_transaction, "Saque negado\nSaldo insuficiente"
        else:
            return insert_balance, insert_statement, insert_number_transactions, datetime_last_transaction, "Saque negado\nValor além do limite permitido"
    else:
        return insert_balance, insert_statement, insert_number_transactions, datetime_last_transaction, "Limite de transações diárias excedido"

def verify_statement(insert_statement, insert_balance):
    if insert_statement == "":
        return "Não foram realizadas movimentações."
    else:
        return f"Movimentações:\n{insert_statement}\nSaldo atual:\nR${insert_balance:.2f}"

while True:
    option = input(menu)

    if option == "d":
        value = float(input("Digite o valor a ser depositado:\n"))
        balance, statement, number_transactions, datetime_transaction, message = deposit(value, balance, statement, number_transactions, datetime_transaction)
        print(message)

    elif option == "s":
        value = float(input("Digite o valor a ser sacado:\n"))
        balance, statement, number_transactions, datetime_transaction, message = withdrawal(value, balance, statement, number_transactions, datetime_transaction)
        print(message)

    elif option == "e":
        print(verify_statement(statement, balance))

    elif option == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a opção desejada.")