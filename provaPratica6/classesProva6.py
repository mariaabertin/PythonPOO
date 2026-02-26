class Familia:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_nome(self):
        return self.nome
    def get_idade(self):
        return self.idade

    def set_nome(self, novoNome):
        self.nome = novoNome
    def set_idade(self, novaIdade):
        self.idade = novaIdade

    #Metodos criativo para usar em todos
    def fazerAniversario(self):
        self.idade = self.idade + 1

    def apresentar(self):
        return print(f"Olá, eu sou {self.nome} e tenho {self.idade} anos.\n")


class Filho(Familia):
    def __init__(self, nome, idade, nomeDaMae, qntIrmaos=0):
        super().__init__(nome, idade)
        self.nomeDaMae = nomeDaMae
        self.qntIrmaos = qntIrmaos

    def get_nomeDaMae(self):
        return self.nomeDaMae
    def get_qntIrmaos(self):
        return self.qntIrmaos

    def set_nomeDaMae(self, novoNomeDaMae):
        self.nomeDaMae = novoNomeDaMae
    def set_qntIrmaos(self, novoQntIrmaos):
        self.qntIrmaos = novoQntIrmaos

class Agregados(Familia):
    def __init__(self, nome, idade, sobrenome, parentesco="Amigo"):
        super().__init__(nome, idade)
        self.sobrenome = sobrenome
        self.parentesco = parentesco

    def get_sobrenome(self):
        return self.sobrenome
    def get_parentesco(self):
        return self.parentesco

    def set_sobrenome(self, novoSobrenome):
        self.sobrenome = novoSobrenome
    def set_parentesco(self, novoParentesco):
        self.parentesco = novoParentesco