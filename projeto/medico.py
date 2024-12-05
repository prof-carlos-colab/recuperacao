from projeto.funcionario import Funcionario
from dataclasses import dataclass

@dataclass
class Medico(Funcionario):
    crm: str

    def mostrar_dados_funcionario(self):
        return "Mostrando os dados do médico"