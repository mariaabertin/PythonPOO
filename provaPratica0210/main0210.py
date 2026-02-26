from classes0210 import Animal, Especie
if __name__ == '__main__':
    animal1 = Animal("Lola", 1)
    animal2 = Animal("Minnie", 8)
    animal3 = Animal("Lion", 16)

    print(f"Animal 1: {animal1.get_nome()}\nIdade: {animal1.get_idade()}\n")
    print(f"Animal 2: {animal2.get_nome()}\nIdade: {animal2.get_idade()}\n")
    print(f"Animal 3: {animal3.get_nome()}\nIdade: {animal2.get_idade()}\n")

    print("--------ESPECIES--------")
    especie1 = Especie("Lola", 1, "Mammmífero", "cachorro")
    especie2 = Especie("Minnie", 8, "Mamífero", "gato")
    especie3 = Especie("Lion", 16, "Reptil", "tartaruga")

    print(f"Especie  1: {especie1.get_nome()}\nIdade: {especie1.get_idade()}\nClasse: {especie1.get_classe()}\nEspécie: {especie1.get_nomeEspecie()}")
    print(f"Especie  2: {especie2.get_nome()}\nIdade: {especie2.get_idade()}\nClasse: {especie2.get_classe()}\nEspécie: {especie2.get_nomeEspecie()}")
    print(f"Especie  3: {especie3.get_nome()}\nIdade: {especie3.get_idade()}\nClasse: {especie3.get_classe()}\nEspécie: {especie3.get_nomeEspecie()}")

    print("\n--------ALTERAÇÕES--------\n")
    animal1.set_nome("Lolla")
    animal2.set_idade(9)
    especie1.set_nomeEspecie("Mamífero")
    especie2.set_nomeClasse("Gato")

    print(f"Animal 1: {animal1.get_nome()}\nIdade: {animal1.get_idade()}\n")
    print(f"Animal 2: {animal2.get_nome()}\nIdade: {animal2.get_idade()}\n")
    print(f"Animal 3: {animal3.get_nome()}\nIdade: {animal2.get_idade()}\n")

    print(f"Especie  1: {especie1.get_nome()}\nIdade: {especie1.get_idade()}\nClasse: {especie1.get_classe()}\nEspécie: {especie1.get_nomeEspecie()}\n")
    print(f"Especie  2: {especie2.get_nome()}\nIdade: {especie2.get_idade()}\nClasse: {especie2.get_classe()}\nEspécie: {especie2.get_nomeEspecie()}\n")
    print(f"Especie  3: {especie3.get_nome()}\nIdade: {especie3.get_idade()}\nClasse: {especie3.get_classe()}\nEspécie: {especie3.get_nomeEspecie()}\n")
