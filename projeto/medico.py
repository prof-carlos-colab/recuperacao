
from dataclasses import dataclass

from projeto.funcionario import Funcionario


@dataclass
class Medico(Funcionario):
    crm: str

    def mostrar_dados_funcionario(self):
        return "Mostrando os dados do médico"