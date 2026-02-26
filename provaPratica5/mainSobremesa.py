from classesSobremesa import Sobremesa, Bolo, Cookie
if __name__ == '__main__':
    sobremesa1= Sobremesa("pudim", 17102025)
    sobremesa2 = Sobremesa("Mousse", 18102025)

    print(f"Sobremesa 1: {sobremesa1.get_nome()}\nData de Fabricação: {sobremesa1.get_dataFabric()}\n")
    print(f"Sobremesa 2: {sobremesa2.get_nome()}\nData de Fabricação: {sobremesa2.get_dataFabric()}\n")

    print("ALTERAÇÕES-------")
    sobremesa1.set_nome("Pudim")
    print(f"Sobremesa 1: {sobremesa1.get_nome()}\nData de Fabricação: {sobremesa1.get_dataFabric()}\n")

    print("\n--------SUBCLASSES--------")
    bolo1= Bolo("Chocolate", 18102025, 10)
    bolo2 = Bolo("Red Velvet", 19102025, 15, 3)

    cookie1= Cookie("Kinder Bueno", 16102025, "Ao leite")
    cookie2= Cookie("Pistache", 19102025, "Branco", 18)

    print(f"Bolo 1: {bolo1.get_nome()}\nData de Fabricação: {bolo1.get_dataFabric()}\nQnt de Fatias: {bolo1.get_qntFatias()}\nQnt de Recheio: {bolo1.get_qntRecheio()}\n")
    print(f"Bolo 2: {bolo2.get_nome()}\nData de Fabricação: {bolo2.get_dataFabric()}\nQnt de Fatias: {bolo2.get_qntFatias()}\nQnt de Recheio: {bolo2.get_qntRecheio()}\n")

    print(f"Cookie 1: {cookie1.get_nome()}\nData de Fabricação: {cookie1.get_dataFabric()}\nSabor Chocolate: {cookie1.get_saborChocolate()}\nQnt Feito: {cookie1.get_qntFeito()}\n")
    print(f"Cookie 2: {cookie2.get_nome()}\nData de Fabricação: {cookie2.get_dataFabric()}\nSabor Chocolate: {cookie2.get_saborChocolate()}\nQnt Feito: {cookie2.get_qntFeito()}\n")

    print("ALTERAÇÕES-------")
    bolo1.set_qntFatias(14)
    print(f"Bolo 1: {bolo1.get_nome()}\nData de Fabricação: {bolo1.get_dataFabric()}\nQnt de Fatias: {bolo1.get_qntFatias()}\n Qnt de Recheio: {bolo1.get_qntRecheio()}\n")

    cookie2.set_qntFeito(20)
    cookie2.aumentarAno()
    print(f"Cookie 2: {cookie2.get_nome()}\nData de Fabricação: {cookie2.get_dataFabric()}\nSabor Chocolate: {cookie2.get_saborChocolate()}\nQnt Feito: {cookie2.get_qntFeito()}\n")
