class Pet:
    def __init__(self, nomeDono, animal, peso, idade):
        self.nomeDono = nomeDono
        self.animal = animal
        self.peso = peso
        self.idade = idade

    def get_nomeDono(self):
        return self.nomeDono
    def get_animal(self):
        return self.animal
    def get_peso(self):
        return self.peso
    def get_idade(self):
        return self.idade

    def set_nomeDono(self, novoNome):
        self.nomeDono = novoNome
    def set_animal(self, novoAnimal):
        self.animal = novoAnimal
    def set_peso(self, novoPeso):
        self.peso = novoPeso
    def set_idade(self, novaIdade):
        self.idade = novaIdade

#Todos os animais do petshop passaram por uma dieta de ganho de peso e
#aumentaram 25% de sua massa corporal, como ficou o peso deles agora?

    def ganhoPeso(self, porcentagem):
        self.peso = self.peso+(self.peso*porcentagem)

if __name__ == '__main__':
    pet1 = Pet("Maria", "cachorro", 3.56, 5)
    print(pet1)

    pet2 = Pet("Fernanda", "gato", 2.48, 2)
    print(pet2)

    pet3 = Pet("Luiz", "cachorro", 7.50, 3)
    print(pet3)

    print(f"Pet 1: {pet1.get_animal()} \nNome do Dono: {pet1.get_nomeDono()}\nPeso: {pet1.get_peso()}\nIdade: {pet1.get_idade()}\n")
    print(f"Pet 2: {pet2.get_animal()} \nNome do Dono: {pet2.get_nomeDono()}\nPeso: {pet2.get_peso()}\nIdade: {pet2.get_idade()}\n")
    print(f"Pet 3: {pet3.get_animal()} \nNome do Dono: {pet3.get_nomeDono()}\nPeso: {pet3.get_peso()}\nIdade: {pet3.get_idade()}\n")

    pet1.ganhoPeso(25/100)
    pet2.ganhoPeso(25/100)
    pet3.ganhoPeso(25/100)
    print("-----------------------")
    print(f"Pet 1: {pet1.get_animal()} \nNome do Dono: {pet1.get_nomeDono()}\nPeso: {pet1.get_peso()}\nIdade: {pet1.get_idade()}\n")
    print(f"Pet 2: {pet2.get_animal()} \nNome do Dono: {pet2.get_nomeDono()}\nPeso: {pet2.get_peso()}\nIdade: {pet2.get_idade()}\n")
    print(f"Pet 3: {pet3.get_animal()} \nNome do Dono: {pet3.get_nomeDono()}\nPeso: {pet3.get_peso()}\nIdade: {pet3.get_idade()}\n")
