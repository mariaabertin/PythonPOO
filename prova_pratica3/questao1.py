class Surfista:
    def __init__(self, surfista, prancha, tamanho, quantidade, valor):
        self.surfista = surfista
        self.prancha = prancha
        self.tamanho = tamanho
        self.quantidade = quantidade
        self.valor = valor

    def get_surfista(self):
        return self.surfista

    def get_prancha(self):
        return self.prancha

    def get_tamanho(self):
        return self.tamanho

    def get_quantidade(self):
        return self.quantidade

    def get_valor(self):
        return self.valor

    def set_surfista(self, surfista_novo):
        self.surfista = surfista_novo

    def set_prancha(self, prancha_novo):
        self.prancha = prancha_novo

    def set_tamanho(self, tamanho_novo):
        self.tamanho = tamanho_novo

    def set_quantidade(self, quantidade_novo):
        self.quantidade = quantidade_novo

    def set_valor(self, valor_novo):
        self.valor = valor_novo

    def mostrar_dados1(self):
        print(f"Surfista: {self.surfista}")
        print(f"Prancha: {self.prancha}")
        print(f"Tamanho: {self.tamanho}")
        print(f"Quantidade: {self.quantidade}")
        print(f"Valor: {self.valor}\n")

    def mostra_dados2(self):
        print(f"Surfista: {self.get_surfista()}\nPrancha: {self.get_prancha()}\nTamanho: {self.get_tamanho()}\nQuantidade: {self.get_quantidade()}\nValor: {self.get_valor()}\n")

    def aumenta_valor(self, aumento):
        self.valor = self.valor + aumento

    def aumenta_quantidade(self, quantidade):
        self.quantidade = self.quantidade + quantidade


if __name__ == '__main__':
    surfista1 = Surfista("Liz", "Longboard", 5.5, 1, 718.00)
    surfista2 = Surfista("Lucas", "Shortboard", 7.1, 2, 560.50)
    surfista3 = Surfista("Gabriel", "Funboard", 8.0, 3, 699.99)
    surfista4 = Surfista("Maristela", "Evolution", 6.4, 2,1200.00)

    print("--- mostra_dados1 ---")
    surfista1.mostrar_dados1()
    surfista2.mostrar_dados1()
    surfista3.mostrar_dados1()
    surfista4.mostrar_dados1()

    print("\n--- mostra_dados2 ---")
    surfista1.mostra_dados2()
    surfista2.mostra_dados2()
    surfista3.mostra_dados2()
    surfista4.mostra_dados2()

    print("\n-----------------")
    aumento = float(input("Favor digite o aumento de valor das pranchas: "))
    surfista1.aumenta_valor(aumento)
    surfista2.aumenta_valor(aumento)
    surfista3.aumenta_valor(aumento)
    surfista4.aumenta_valor(aumento)

    # elabore o enunciado (o problema) e implemente mais um método funcional neste sistema.
    quantidade = int(input("Compraram mais pranchas, que maneiro! Favor digitar a quantidade adiquirida: "))
    surfista1.aumenta_quantidade(quantidade)
    surfista2.aumenta_quantidade(quantidade)
    surfista3.aumenta_quantidade(quantidade)
    surfista4.aumenta_quantidade(quantidade)

    print("\n-----------------")
    surfista1.mostrar_dados1()
    surfista2.mostrar_dados1()
    surfista3.mostrar_dados1()
    surfista4.mostrar_dados1()