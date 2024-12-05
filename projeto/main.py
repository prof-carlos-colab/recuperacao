from projeto.medico import Medico
from projeto.motorista import Motorista


# Instanciar objetos.
medico = Medico()
medico.nome = input("Digite seu nome: ")
medico.idade = int(input("Digite sua idade: "))
medico.crm = input("Digite seu CRM: ")
medico.endereco.logradouro = input("Digite o logradouro: ")
medico.endereco.numero = input("Digite o número da residência: ")

medico.mostrar_dados_funcionario()


motorista = Motorista()
motorista.nome = input("Digite seu nome: ")
motorista.idade = int(input("Digite sua idade: "))
motorista.crm = input("Digite seu CRM: ")
motorista.endereco.logradouro = input("Digite o logradouro: ")
motorista.endereco.numero = input("Digite o número da residência: ")

motorista.mostrar_dados_funcionario()