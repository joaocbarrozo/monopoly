class Jogador:
    def __init__(self, nome, saldoInicial, cor):
        self.nome = nome
        self.posicao = 0  # Posição inicial do jogador no tabuleiro
        self.dinheiro = saldoInicial  # Dinheiro inicial do jogador
        self.propriedades = []  # Lista para armazenar as propriedades do jogador
        self.cor = cor

    def mover(self, casas):
        self.posicao = (self.posicao + casas) % 40  # Há 40 casas no tabuleiro do Monopoly

    def adicionar_dinheiro(self, quantidade):
        self.dinheiro += quantidade

    def remover_dinheiro(self, quantidade):
        self.dinheiro -= quantidade

    def comprar_propriedade(self, propriedade):
        self.propriedades.append(propriedade)
        self.remover_dinheiro(propriedade.preco)

    def pagar_aluguel(self, proprietario, aluguel):
        if self.dinheiro >= aluguel:
            self.remover_dinheiro(aluguel)
            proprietario.adicionar_dinheiro(aluguel)
        else:
            # Se o jogador não tiver dinheiro suficiente para pagar o aluguel, ele está falido
            # e deve sair do jogo
            print(f"{self.nome} faliu!")
            # Aqui você pode adicionar a lógica para remover o jogador do jogo

    def __str__(self):
        return f"Nome: {self.nome}, Posição: {self.posicao}, Dinheiro: {self.dinheiro}, Propriedades: {self.propriedades}"

class Propriedade:
    def __init__(self, cor, borda_cor, titulo, texto, nivel, proprietario, valor_compra, array_aluguel):
        self.cor = cor
        self.borda_cor = borda_cor
        self.titulo = titulo
        self.texto = texto
        self.nivel = nivel
        self.prorpietario = proprietario# Definir banco para as posições especiais do tabuleiro como inicio, prisão sorte e revez e etc
        self.valor_compra = valor_compra
        self.valor_aluguel = array_aluguel # Array com o valor do aluguel para cada nivel 5 posições

class CasaTabuleiro:
    def __init__(self, numero, posicao_x, posicao_y, width, height, propriedade):
        self.numero = numero
        self.posicao_x = posicao_x
        self.posicao_y = posicao_y
        self.width = width
        self.height = height
        self.propriedade = propriedade

class Partida:
    def __init__(self, jogadores):
        self.status = "Jogando"
        self.jogada = 0
        self.inflacao = 0
        self.selic = 0.05
        self.jogadores = jogadores#Array com os jogadores