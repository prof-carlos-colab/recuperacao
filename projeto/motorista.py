from projeto.funcionario import Funcionario
from dataclasses import dataclass

@dataclass
class Motorista(Funcionario):
    cnh: str

    def mostrar_dados_funcionario(self):
        return "Mostrando dados do motorista"