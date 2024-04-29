class UsuarioTelefone:
    def __init__(self, nome, numero, plano):
        self.__nome = nome
        self.__numero = numero
        self.__plano = plano
    
    def __str__(self):
        return f"Usuário {self.__nome} criado com sucesso."


# Entrada:
nome = input()
numero = input()
plano = input()


# Criação do objeto UsuarioTelefone
usuario = UsuarioTelefone(nome, numero, plano)


# Saída:
print(usuario)

# Classe PlanoTelefone
class PlanoTelefone:
    def __init__(self, nome, saldo):
        self.nome = nome
        self.saldo = saldo


    def verificar_saldo(self):
        if self.saldo < 10:
            return "Seu saldo está baixo. Recarregue e use os serviços do seu plano."
        elif self.saldo >= 50:
            return "Parabéns! Continue aproveitando seu plano sem preocupações."
        else:
            return "Seu saldo está razoável. Aproveite o uso moderado do seu plano."


# Classe UsuarioTelefone
class UsuarioTelefone:
    def __init__(self, nome, plano):
        self.nome = nome
        self.plano = plano


    def verificar_saldo(self):
        return self.plano.verificar_saldo()


# Recebendo as entradas do usuário (nome, plano, saldo):
nome_usuario = input()
nome_plano = input()
saldo_inicial = float(input())


# Criação de objetos do plano de telefone e usuário de telefone com dados fornecidos:
plano_usuario = PlanoTelefone(nome_plano, saldo_inicial)
usuario = UsuarioTelefone(nome_usuario, plano_usuario)


# Chamada do método para verificar_saldo sem acessar diretamente os atributos do plano:
mensagem_usuario = usuario.verificar_saldo()
print(mensagem_usuario)

class UsuarioTelefone:
    def __init__(self, nome, numero, plano):
        self.nome = nome
        self.numero = numero
        self.plano = plano


    def fazer_chamada(self, destinatario, duracao):
        custo_chamada = self.plano.custo_chamada(duracao)
        if self.plano.verificar_saldo() >= custo_chamada:
            self.plano.deduzir_saldo(custo_chamada)
            return f"Chamada para {destinatario} realizada com sucesso. Saldo: ${self.plano.verificar_saldo():.2f}"
        else:
            return "Saldo insuficiente para fazer a chamada."




class Plano:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial


    def verificar_saldo(self):
        return self.saldo


    def custo_chamada(self, duracao):
        return duracao * 0.10


    def deduzir_saldo(self, valor):
        self.saldo -= valor




class UsuarioPrePago(UsuarioTelefone):
    def __init__(self, nome, numero, saldo_inicial):
        super().__init__(nome, numero, Plano(saldo_inicial))




nome = input()
numero = input()
saldo_inicial = float(input())
usuario_pre_pago = UsuarioPrePago(nome, numero, saldo_inicial)
destinatario = input()
duracao = int(input())
print(usuario_pre_pago.fazer_chamada(destinatario, duracao))