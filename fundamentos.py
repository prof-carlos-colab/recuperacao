# Herança
# Polimorfismo

# Ojetivo:
# Reaproveitamento de código.

# Exemplo: 
from abc import ABC, abstractmethod

# HERANÇA.
# Serve como base ou modelo para outras classes.
class Pessoa(ABC): # Definindo classe: Pessoa.
    # Atributo é uma variável dentro de uma classe.    
    nome: str # atributo nome
    idade: int # atributo idade

    # POLIMORFISMO
    # Função é igual a método
    # Um método é uma função dentro de uma classe.
    @abstractmethod
    def deveres(self):
        pass

# HERANÇA.
class Aluno(Pessoa):
    ra: str

    # POLIMORFISMO
    def deveres(self):
        return "Estudar."

# HERANÇA.
class Professor(Pessoa):
    matricula: str

    # POLIMORFISMO
    def deveres(self):
        return "Ensinar"
    
# Instanciando objetos.
aluno = Aluno()
aluno.nome = input("Digite seu nome: ")
aluno.ra = input("Digite seu R.A.: ")
aluno.deveres()

professor = Professor()
professor.nome = input("Digite seu nome: ")
professor.matricula = input("Digite sua matrícula: ")
professor.deveres()
