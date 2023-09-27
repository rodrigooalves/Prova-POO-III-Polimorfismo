class BombaDeCombustivel:
    def __init__(self, tipo_combustivel, valor_litro, quantidade_combustivel):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.quantidade_combustivel = quantidade_combustivel

    def abastecer_por_valor(self, valor_abastecido):
        if self.quantidade_combustivel == 0:
            print("A bomba está vazia. Não é possível abastecer.")
            return
        litros_abastecidos = valor_abastecido / self.valor_litro
        if litros_abastecidos > self.quantidade_combustivel:
            print("Quantidade insuficiente de combustível na bomba.")
            return
        self.quantidade_combustivel -= litros_abastecidos
        print(f"Abastecimento de R${valor_abastecido:.2f}. Foram abastecidos {litros_abastecidos:.2f} litros de {self.tipo_combustivel}.")

    def abastecer_por_litro(self, litros_abastecidos):
        if self.quantidade_combustivel == 0:
            print("A bomba está vazia. Não é possível abastecer.")
            return
        valor_a_pagar = litros_abastecidos * self.valor_litro
        if litros_abastecidos > self.quantidade_combustivel:
            print("Quantidade insuficiente de combustível na bomba.")
            return
        self.quantidade_combustivel -= litros_abastecidos
        print(f"Abastecimento de {litros_abastecidos:.2f} litros de {self.tipo_combustivel}. Valor a pagar: R${valor_a_pagar:.2f}")

    def alterar_valor(self, novo_valor_litro):
        self.valor_litro = novo_valor_litro
        print(f"O novo valor do litro de {self.tipo_combustivel} é R${novo_valor_litro:.2f}.")

    def alterar_combustivel(self, novo_tipo_combustivel):
        self.tipo_combustivel = novo_tipo_combustivel
        print(f"O tipo de combustível foi alterado para {novo_tipo_combustivel}.")

    def alterar_quantidade_combustivel(self, nova_quantidade_combustivel):
        self.quantidade_combustivel = nova_quantidade_combustivel
        print(f"A quantidade de combustível na bomba foi alterada para {nova_quantidade_combustivel:.2f} litros.")
