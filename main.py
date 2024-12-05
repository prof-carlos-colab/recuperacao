from projeto.endereco import Endereco
from projeto.medico import Medico
from projeto.motorista import Motorista

# Instanciar objetos.
medico = Medico(
    nome = input("Digite seu nome: "),
    idade = int(input("Digite sua idade: ")),
    crm = input("Digite seu CRM: "),
    endereco = Endereco(
    logradouro = input("Digite o logradouro: "),
    numero = input("Digite o número da residência: ")
    )
)
medico.mostrar_dados_funcionario()



motorista = Motorista(
    nome = input("Digite seu nome: "),
    idade = int(input("Digite sua idade: ")),
    cnh = input("Digite seu CNH: "),
    endereco = Endereco(
    logradouro = input("Digite o logradouro: "),
    numero = input("Digite o número da residência: ")
    )
)
motorista.mostrar_dados_funcionario()