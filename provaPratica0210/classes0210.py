class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_nome(self):
        return self.nome

    def get_idade(self):
        return self.idade

    def set_nome(self, novoNome):
        self.nome = novoNome

    def set_idade(self, novoIdade):
        self.idade = novoIdade


class Especie(Animal):
    def __init__(self, nome, idade, classe, nomeEspecie):
        self.nome = nome
        self.idade = idade
        self.classe = classe
        self.nomeEspecie = nomeEspecie

    def get_nomeEspecie(self):
        return self.nomeEspecie
    def get_classe(self):
        return self.classe

    def set_nomeEspecie(self, novoNomeEspecie):
        self.nomeEspecie = novoNomeEspecie
    def set_nomeClasse(self, novoClasse):
        self.classe = novoClasse



