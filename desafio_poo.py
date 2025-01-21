import textwrap
from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        pass
    def adicionar_conta(self, conta):
        self.contas.append(conta)



class PessoaFisica(Cliente):
    usuarios_cadastrados = set()
    @staticmethod
    def validate_cpf(cpf):
        cpf_list = []
        if len(cpf) != 11:
            return False

        for i in cpf:
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
        
    def __init__(self, nome, data_nascimento, cpf, endereco):
        if not self.validate_cpf(cpf):
            raise ValueError("CPF inválido")
        if cpf in PessoaFisica.usuarios_cadastrados:
            raise ValueError("CPF já cadastrado")
        
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.usuarios_cadastrados.add(cpf)
        


class Conta:
    def __init__(self, numero, cliente):
        pass

    @classmethod
    def nova_conta(cls, cliente, numero):
        pass

    @property
    def saldo(self):
        pass

    @property
    def numero(self):
        pass

    @property
    def agencia(self):
        pass

    @property
    def cliente(self):
        pass

    @property
    def historico(self):
        pass

    def sacar(self, valor):
        pass

    def depositar(self, valor):
        pass


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        pass

    def sacar(self, valor):
        pass

    def __str__(self):
        pass


class Historico:
    def __init__(self):
        pass

    @property
    def transacoes(self):
        pass

    def adicionar_transacao(self, transacao):
        pass


class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractclassmethod
    def registrar(self, conta):
        pass


class Saque(Transacao):
    def __init__(self, valor):
        pass

    @property
    def valor(self):
        pass

    def registrar(self, conta):
        pass


class Deposito(Transacao):
    def __init__(self, valor):
        pass

    @property
    def valor(self):
        pass

    def registrar(self, conta):
        pass


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


def filtrar_cliente(cpf, clientes):
    pass


def recuperar_conta_cliente(cliente):
    pass


def depositar(clientes):
    pass


def sacar(clientes):
    pass


def exibir_extrato(clientes):
    pass


def criar_cliente(clientes):
    pass


def criar_conta(numero_conta, clientes, contas):
    pass


def listar_contas(contas):
    pass


def main():
    clientes = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            depositar(clientes)

        elif opcao == "s":
            sacar(clientes)

        elif opcao == "e":
            exibir_extrato(clientes)

        elif opcao == "nu":
            criar_cliente(clientes)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("\n@@@ Operação inválida, por favor selecione novamente a operação desejada. @@@")


main()
