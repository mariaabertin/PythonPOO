from classesProva6 import Familia, Filho, Agregados

if __name__ == '__main__':
    membro1 = Familia("Ana", 45)
    membro2 = Familia("Carlos", 48)

    membro1.set_nome("Ana Maria")
    membro1.fazerAniversario()

    print("\n-------- SUBCLASSES --------")
    print(f"Membro 1: {membro1.get_nome()}\nIdade: {membro1.get_idade()}\n")
    print(f"Membro 2: {membro2.get_nome()}\nIdade: {membro2.get_idade()}\n")

    print("\n-------- SUBCLASSES --------")
    filho1 = Filho("Pedro", 15, "Ana")
    filho2 = Filho("Julia", 18, "Maria", 2)

    agregado1 = Agregados("João", 30, "Silva")
    agregado2 = Agregados("Mariana", 25, "Santos", "Namorada")

    print(f"Filho 1: {filho1.get_nome()}\nIdade: {filho1.get_idade()}\nNome da Mãe: {filho1.get_nomeDaMae()}\nQuantidade de Irmãos: {filho1.get_qntIrmaos()}\n")
    print(f"Filho 2: {filho2.get_nome()}\nIdade: {filho2.get_idade()}\nNome da Mãe: {filho2.get_nomeDaMae()}\nQuantidade de Irmãos: {filho2.get_qntIrmaos()}\n")

    print(f"Agregado 1: {agregado1.get_nome()}\nIdade: {agregado1.get_idade()}\nSobrenome: {agregado1.get_sobrenome()}\nParentesco: {agregado1.get_parentesco()}\n")
    print(f"Agregado 2: {agregado2.get_nome()}\nIdade: {agregado2.get_idade()}\nSobrenome: {agregado2.get_sobrenome()}\nParentesco: {agregado2.get_parentesco()}\n")

    print("---ALTERAÇÕES NAS SUBCLASSES---")
    filho1.set_qntIrmaos(1)
    filho1.fazerAniversario()
    agregado2.set_parentesco("Esposa")

    print(f"Filho 1: {filho1.get_nome()}\nIdade: {filho1.get_idade()}\nNome da Mãe: {filho1.get_nomeDaMae()}\nQuantidade de Irmãos: {filho1.get_qntIrmaos()}\n")
    print(f"Agregado 2: {agregado2.get_nome()}\nIdade: {agregado2.get_idade()}\nSobrenome: {agregado2.get_sobrenome()}\nParentesco: {agregado2.get_parentesco()}\n")

    agregado1.apresentar()