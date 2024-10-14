import textwrap


def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))


LIMIT_WITHDRAWALS = 3
AGENCY = "0001"
users = {}
accounts = []
balance = 0
limit = 500
statement = ""
number_withdrawals = 0

def validate_cpf(cpf_input):
    cpf_list = []
    if len(cpf_input) != 11:
        return False

    for i in cpf_input:
        cpf_list.append(int(i))

    def calculate_sum(start_index):
        sum = 0
        multiplier = 2
        for i in range(start_index, -1, -1):
            sum += cpf_list[i] * multiplier
            multiplier += 1
        return sum

    sum_1 = calculate_sum(8)
    remainder_1 = sum_1 % 11
    digit_1 = None
    if remainder_1 < 2:
        digit_1 = 0
    elif remainder_1 >= 2:
        digit_1 = 11 - remainder_1
    if digit_1 != cpf_list[9]:
        return False

    sum_2 = calculate_sum(9)
    remainder_2 = sum_2 % 11
    digit_2 = None
    if remainder_2 < 2:
        digit_2 = 0
    elif remainder_2 >= 2:
        digit_2 = 11 - remainder_2
    if digit_2 != cpf_list[10]:
        return False
    else:
        return True

def create_user(cpf):
    if not validate_cpf(cpf):
        return "CPF inválido"

    if cpf in users:
        return "CPF já cadastrado"
    
    else:
        name = input("Informe o nome completo: ")
        born = input("Informe a data de nascimento (dd-mm-aaaa): ")
        address = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    users[cpf] = {
        "Nome":name,"Data de nascimento":born,"Endereço":address
                  }
    return "Usuário criado com sucesso"

def create_account():
    cpf = input("Digite o cpf do titular da nova conta corrente: ")
    if cpf not in users:
        return "CPF não cadastrado"
    
    account = {"Agência":AGENCY, "Conta":len(accounts)+1,"CPF":cpf, "Titular":users[cpf]["Nome"]}
    accounts.append(account)
    return f"Conta criada\n{account}"

def deposit(insert_value, insert_balance, insert_statement, /):
    if insert_value <= 0:
        return insert_balance, insert_statement, "Depósito negado"
    else:
        insert_balance += insert_value
        insert_statement += f"Depósito: R${insert_value:.2f}\n"
        return insert_balance, insert_statement, "Depósito realizado"

def withdrawal(*, insert_value, insert_balance, insert_statement, insert_number_withdrawals):
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

def verify_statement(insert_balance,/, *,insert_statement):
    if insert_statement == "":
        return "Não foram realizadas movimentações."
    else:
        return f"Movimentações:\n{insert_statement}\nSaldo atual:\nR${insert_balance:.2f}"

def main():

    while True:
        option = menu()

        if option == "d":
            value = float(input("Digite o valor a ser depositado:\n"))
            balance, statement, message = deposit(value, balance, statement)
            print(message)

        elif option == "s":
            value = float(input("Digite o valor a ser sacado:\n"))
            balance, statement, number_withdrawals, message = withdrawal(value = value, balance = balance, statement = statement, number_withdrawals = number_withdrawals)
            print(message)

        elif option == "e":
            print(verify_statement(balance, statement=statement))

        elif option == "q":
            break

        elif option == "nc":
            print(create_account)

        elif option == "lc":
            for acc in accounts:
                print(acc)

        elif option == "nu":
            cpf = input("Digite o CPF do novo usuário: ")
            result = create_user(cpf)
            print(result)

        else:
            print("Operação inválida, por favor selecione novamente a opção desejada.")

main()