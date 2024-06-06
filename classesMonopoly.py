import pygame

black = (0, 0, 0)
white = (255, 255, 255)

class Jogador:
    def __init__(self, nome, saldoInicial, cor):
        self.nome = nome
        self.posicao = 0  # Posição inicial do jogador no tabuleiro
        self.dinheiro = saldoInicial  # Dinheiro inicial do jogador
        self.propriedades = []  # Lista para armazenar as propriedades do jogador
        self.cor = cor

    def mover(self, casas):
        self.posicao = (self.posicao + casas) % 36  # Há 40 casas no tabuleiro do Monopoly

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
    def __init__(self, cor, borda_cor, titulo, texto, nivel, proprietario, valor_compra, array_aluguel, info=None):
        self.cor = cor
        self.borda_cor = borda_cor
        self.titulo = titulo
        self.texto = texto
        self.nivel = nivel
        self.prorpietario = proprietario# Definir banco para as posições especiais do tabuleiro como inicio, prisão sorte e revez e etc
        self.valor_compra = valor_compra
        self.valor_aluguel = array_aluguel # Array com o valor do aluguel para cada nivel 5 posições
        self.info = info


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
        self.jogador_Atual = jogadores[0]

class Button:
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, screen, outline=None):
        if outline:
            pygame.draw.rect(screen, outline, (self.x-2, self.y-2, self.width+4, self.height+4), 0)

        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            font = pygame.font.SysFont(None, 20)
            text = font.render(self.text, 1, black)
            screen.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def is_over(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False
    
    def hover(self, screen):
 
        pygame.mouse.set_cursor(*pygame.cursors.tri_left)

# Classe TextBox
class TextBox:
    def __init__(self, x, y, width, height, font_size=20, text='', color=black):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.font = pygame.font.SysFont(None, font_size)
        self.text = text
        self.color = color

    def draw(self, screen):
        lines = []
        words = self.text.split()

        # Dividindo o texto em linhas
        line = ''
        for word in words:
            if self.font.size(line + word)[0] < self.width:
                line += word + ' '
            else:
                lines.append(line)
                line = word + ' '
        lines.append(line)

        # Desenha o texto na tela
        y = self.y
        for line in lines:
            text_surface = self.font.render(line, True, self.color)
            screen.blit(text_surface, (self.x, y))
            y += self.font.get_linesize()