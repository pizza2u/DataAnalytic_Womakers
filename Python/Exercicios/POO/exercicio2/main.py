from abc import ABC, abstractmethod

class Cliente(ABC):
    def __init__(self, nome, telefone, renda_mensal):
        self._nome = nome
        self._telefone = telefone
        self._renda_mensal = renda_mensal

    @property
    def nome(self):
        return self._nome

    @property
    def telefone(self):
        return self._telefone

    @property
    def renda_mensal(self):
        return self._renda_mensal

    @abstractmethod
    def cheque_especial(self):
        pass

class ClienteMulher(Cliente):
    @property
    def cheque_especial(self):
        return self._renda_mensal

class ClienteHomem(Cliente):
    @property
    def cheque_especial(self):
        return 0

class ContaCorrente:
    def __init__(self):
        self._titulares = []
        self._saldo = 0
        self._operacoes = []

    def adicionar_titular(self, cliente):
        self._titulares.append(cliente)

    @property
    def saldo(self):
        return self._saldo

    @property
    def operacoes(self):
        return self._operacoes

    def depositar(self, valor):
        self._saldo += valor
        self._operacoes.append(f"Depósito: +{valor}")
        print(f"Depósito de {valor} realizado com sucesso.")

    def sacar(self, valor):
        limite = sum(cliente.cheque_especial for cliente in self._titulares)
        if self._saldo - valor >= -limite:
            self._saldo -= valor
            self._operacoes.append(f"Saque: -{valor}")
            print(f"Saque de {valor} realizado com sucesso.")
        else:
            print("Saldo insuficiente para realizar o saque.")

    def mostrar_saldo(self):
        print(f"Saldo atual: {self._saldo}")

    def mostrar_operacoes(self):
        for operacao in self._operacoes:
            print(operacao)

# Criando clientes
cliente1 = ClienteMulher(nome="Maria", telefone="1234-5678", renda_mensal=5000)
cliente2 = ClienteHomem(nome="João", telefone="9876-5432", renda_mensal=3000)

# Criando uma conta corrente
conta = ContaCorrente()

# Adicionando titulares à conta
conta.adicionar_titular(cliente1)
conta.adicionar_titular(cliente2)

# Realizando operações
conta.depositar(1000)
conta.sacar(2000)
conta.sacar(4000)  # Maria tem cheque especial de 5000, então isso deve ser permitido
conta.sacar(5000)  # Isso não deve ser permitido pois ultrapassa o cheque especial de Maria

# saldo e operações
conta.mostrar_saldo()
conta.mostrar_operacoes()
