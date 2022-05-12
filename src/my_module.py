# Cria a classe Hotel, com cada um dos hoteis, e devolve uma lista com os hoteis criados.
def cria_hoteis():
    class Hotel:
        def __init__(self, nome, preco_semana, preco_fim_de_semana, classificacao):
            self.nome = nome
            self.preco_semana = preco_semana  # uso: [preco cliente normal, preco programa de fidelidade]
            self.preco_fim_de_semana = preco_fim_de_semana  # uso: [preco cliente normal, preco programa de fidelidade]
            self.classificacao = classificacao
            return

    # Criacao de cada um dos hoteis e o conjunto com todos eles
    lakewood = Hotel("Lakewood", [110, 80], [90, 80], 3)
    bridgewood = Hotel("Bridgewood", [160, 110], [60, 50], 4)
    ridgewood = Hotel("Ridgewood", [220, 100], [150, 40], 5)

    hoteis = [lakewood, bridgewood, ridgewood]
    return hoteis


def get_cheapest_hotel(informacoes):  # DO NOT change the function's name

    hoteis = cria_hoteis()

    # Defineicao dos dias da semana e dias de final de semana
    dias_da_semana = ["mon", "tues", "wed", "thur", "fri"]
    dias_do_fim_de_semana = ["sat", "sun"]

    # Tratamento da entrada, definindo tipo de cliente e datas da hospedagem
    informacoes = informacoes.split(": ")
    tipo_de_cliente = informacoes.pop(0)
    dias_de_estadia: list[str] = informacoes[0].split(", ")

    # Filtragem do dia da semana de cada um dos dados
    # Nota-se que esta filtragem funciona para datas no modelo DDMMMYYYY(%a)
    for i in range(len(dias_de_estadia)):
        dias_de_estadia[i] = dias_de_estadia[i][10:14]
        if dias_de_estadia[i].endswith(")"):
            dias_de_estadia[i] = dias_de_estadia[i][0:3]

    # Define o indice de cliente a ser usado para calculo dos precos
    if tipo_de_cliente == "Regular":
        indice_de_cliente = 0
    else:
        indice_de_cliente = 1

    # Prepara uma lista para receber os custos de cada um dos hoteis
    custos = []
    for hotel in hoteis:
        custos.append(0)

    # Calcula custos para cada um dos hoteis
    for hotel in hoteis:
        for x in range(len(dias_de_estadia)):
            if dias_de_estadia[x] in dias_do_fim_de_semana:
                custos[hoteis.index(hotel)] += hotel.preco_fim_de_semana[indice_de_cliente]
            elif dias_de_estadia[x] in dias_da_semana:
                custos[hoteis.index(hotel)] += hotel.preco_semana[indice_de_cliente]

    # Compara o custo total e a classificacao dos hoteis
    minimo = custos[0]
    melhor_classificacao = hoteis[0].classificacao
    cheapest_hotel = ""
    for i in range(len(custos)):
        if (custos[i] <= minimo and hoteis[i].classificacao >= melhor_classificacao):
            minimo = custos[i]
            melhor_classificacao = hoteis[i].classificacao
            cheapest_hotel = hoteis[i].nome
    return cheapest_hotel
