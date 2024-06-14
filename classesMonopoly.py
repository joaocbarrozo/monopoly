import pygame
import random

black = (0, 0, 0)
white = (255, 255, 255)

class Jogador:
    def __init__(self, nome, posicao, saldoInicial, cor, ferias, congelamento, patrimonioInicial,
                 distancia, rodadasCongelamento, rodadasFerias, voltas, premios, multas):
        self.nome = nome
        self.posicao = posicao  # Posição inicial do jogador no tabuleiro
        self.dinheiro = saldoInicial  # Dinheiro inicial do jogador
        self.propriedades = []  # Lista para armazenar as propriedades do jogador
        self.cor = cor
        self.ferias = ferias
        self.congelamento = congelamento
        self.patrimonio = patrimonioInicial
        self.distancia = distancia
        self.rodadasCongelamento = rodadasCongelamento
        self.rodadasFerias = rodadasFerias
        self.voltas = voltas
        self.premios = premios
        self.multas = multas

    def mover(self, casas):
        self.posicao = (self.posicao + casas) % 36  # Há 36 casas no tabuleiro do Monopoly

    def adicionar_dinheiro(self, quantidade):
        self.dinheiro += quantidade
        self.patrimonio += quantidade
    
    def remover_dinheiro(self, quantidade):
        if self.saldo_suficiente(quantidade):
            self.dinheiro -= quantidade
            self.patrimonio -= quantidade
            return True
        return False
    
    def saldo_suficiente(self, valor):
        if self.dinheiro >= valor:
            return True
        return False

    def comprar_propriedade(self, propriedade):
        if self.saldo_suficiente(propriedade.valor_compra):
            self.propriedades.append(propriedade)
            self.remover_dinheiro(propriedade.valor_compra)
            self.patrimonio += propriedade.valor_compra
            propriedade.borda_cor = self.cor
            propriedade.proprietario = self
            return True
        return False

    def pagar_aluguel(self, proprietario, aluguel):
        if self.saldo_suficiente(aluguel):
            self.remover_dinheiro(aluguel)
            proprietario.adicionar_dinheiro(aluguel)
            return True
        else:
            # Se o jogador não tiver dinheiro suficiente para pagar o aluguel, ele está falido
            # e deve sair do jogo
            print(f"{self.nome} faliu!")
            # Aqui você pode adicionar a lógica para remover o jogador do jogo
            return False

    def __str__(self):
        return self.nome

class Propriedade:
    def __init__(self, cor, borda_cor, titulo, texto, nivel, proprietario, valor_compra, info=None):
        #Calculo da taxa de retorno de aluguel
        taxa = random.randint(1, (1000 - valor_compra) / 10)
        print(f"{titulo} taxa {taxa}")
        taxa = taxa * 0.003 + 0.15
        print(f"{titulo} taxa {taxa}")
        #Criação e preenchimento do array aluguel
        array_aluguel = []
        for i in range(1,6):
            valor = i * valor_compra * (taxa + (i-1) * 0.05)
            resto = valor % 10
            if resto < 5:
                valor = int(valor - resto)
            else:
                valor = int(valor - resto + 5)
            array_aluguel.append(valor)
            print(f"aluguel i {i} {array_aluguel[i-1]}")
        print(array_aluguel)
        #Calculo do custo mensal
        self.custo_fixo = valor_compra * 0.1
        self.taxa = taxa
        self.cor = cor
        self.borda_cor = borda_cor
        self.titulo = titulo
        self.texto = texto
        self.nivel = nivel
        self.proprietario = proprietario# Definir banco para as posições especiais do tabuleiro como inicio, prisão sorte e revez e etc
        self.valor_compra = valor_compra
        self.valor_aluguel = array_aluguel # Array com o valor do aluguel para cada nivel 5 posições
        self.info = info
        
    def melhorar_propriedade(self):
        if self.proprietario.saldo_suficiente(self.valor_compra) and self.nivel < 5:
            self.proprietario.remover_dinheiro(self.valor_compra)
            self.proprietario.patrimonio += self.valor_compra
            self.nivel += 1
            return True
        return False
    
    def sorteio_eAgora(self, jogador):
        sorte = random.randint(0, 1000000) % 501
        revez = random.randint(0, 1000000) % 501
        print(f"Sorte: {sorte}, Revez: {revez}")
        if sorte > revez:
            premio = (sorte - revez)// 10 * 10
            mensagem = f"Premio: {premio}"
            jogador.adicionar_dinheiro(premio)
        elif revez > sorte:
            multa = (revez - sorte) // 10 * 10
            mensagem = f"Multa: {multa}"
            jogador.remover_dinheiro(multa)
        else:
            mensagem = "Voce não ganhou nem perdeu nada"
        return mensagem

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
        self.mensagem = ""

class Button:
    def __init__(self, x, y, width, height, text, font, base_color, hover_color, click_color):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = font
        self.base_color = base_color
        self.hover_color = hover_color
        self.click_color = click_color
        self.current_color = base_color
        self.hovered = False 

    def draw(self, screen):
        # Draw the button
        pygame.draw.rect(screen, self.current_color, self.rect)
        # Draw the text
        text_surface = self.font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def handle_event(self, event):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            if not self.hovered:  # If the mouse just started hovering
                self.hovered = True
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)  # Change to hand cursor
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    self.current_color = self.click_color
                    return True  # Button clicked
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:  # Left mouse button
                    self.current_color = self.hover_color
            else:
                self.current_color = self.hover_color
        else:
            if self.hovered:  # If the mouse just stopped hovering
                self.hovered = False
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)  # Change to arrow cursor
            self.current_color = self.base_color
        return False

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