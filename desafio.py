menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

balance = 0
limit = 500
statement = ""
number_withdrawals = 0
LIMIT_WITHDRAWALS = 3

def deposit(insert_value, insert_balance, insert_statement):
    if insert_value <= 0:
        return insert_balance, insert_statement, "Depósito negado"
    else:
        insert_balance += insert_value
        insert_statement += f"Depósito: R${insert_value:.2f}\n"
        return insert_balance, insert_statement, "Depósito realizado"

def withdrawal(insert_value, insert_balance, insert_statement, insert_number_withdrawals):
    if insert_number_withdrawals < LIMIT_WITHDRAWALS:
        if insert_value > 0 and insert_value <= limit:
            if insert_value <= insert_balance:
                insert_balance -= insert_value
                insert_statement += f"Saque: R${insert_value:.2f}\n"
                insert_number_withdrawals += 1
                return insert_balance, insert_statement, insert_number_withdrawals, "Saque realizado"
            else:
                return insert_balance, insert_statement, insert_number_withdrawals, "Saque negado\nSaldo insuficiente"
        else:
            return insert_balance, insert_statement, insert_number_withdrawals, "Saque negado\nValor além do limite permitido"
    else:
        return insert_balance, insert_statement, insert_number_withdrawals, "Limite de saques diários excedidos"

def verify_statement(insert_statement, insert_balance):
    if insert_statement == "":
        return "Não foram realizadas movimentações."
    else:
        return f"Movimentações:\n{insert_statement}\nSaldo atual:\nR${insert_balance:.2f}"

while True:
    option = input(menu)

    if option == "d":
        value = float(input("Digite o valor a ser depositado:\n"))
        balance, statement, message = deposit(value, balance, statement)
        print(message)

    elif option == "s":
        value = float(input("Digite o valor a ser sacado:\n"))
        balance, statement, number_withdrawals, message = withdrawal(value, balance, statement, number_withdrawals)
        print(message)

    elif option == "e":
        print(verify_statement(statement, balance))

    elif option == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a opção desejada.")