
# Programação Orientada a Objetos - POO

# Objeto?
# Uma variável que carrega as características de uma classe.
# Quando usa-se uma classe para definir características.

# Exemplo:
class Pessoa:
    nome: str # atributo nome
    idade: int # atributo idade
    peso: float # atributo peso

class Pet:
    nome: str # atributo nome
    idade: int # atributo idade
    peso: float # atributo peso

# Exemplo de forma de uso.
# Instanciar um objeto.
cliente = Pessoa()

cliente.nome = input("Digite seu nome: ")
cliente.idade = int(input("Digite sua idade: "))
cliente.peso = float(input("Digite seu peso: "))

pet = Pet()

pet.nome = input("Digite seu nome: ")
pet.idade = int(input("Digite sua idade: "))
pet.peso = float(input("Digite seu peso: "))