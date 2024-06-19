import pygame
import random

black = (0, 0, 0)
white = (255, 255, 255)
yellow = (255, 255, 0)
orange = (255, 165, 0)
red = (255, 0, 0)
green = (0, 128, 0)
purple = (128, 0, 128)
blue = (0, 0, 255)
gray = (220, 220, 220)
dark_gray = (120, 120, 120)


class Jogador:
    def __init__(self, nome,  saldoInicial, cor, patrimonioInicial, posicao=0, ferias=0, congelamento=0, 
                 distancia=0, rodadasCongelamento=0, rodadasFerias=0, voltas=0, premios=0, multas=0):
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
        self.distancia += casas

    def adicionar_dinheiro(self, quantidade):
        self.dinheiro += quantidade
        self.patrimonio += quantidade
    
    def remover_dinheiro(self, quantidade):
        self.dinheiro -= quantidade
        self.patrimonio -= quantidade
    
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
        self.remover_dinheiro(aluguel)
        proprietario.adicionar_dinheiro(aluguel)

    def calcularMultas(self, valor):
        self.multas += valor

    def calcularPremios(self, valor):
        self.premios += valor

    def __str__(self):
        return self.nome

class Propriedade:
    def __init__(self, cor, borda_cor, titulo, texto, nivel, proprietario, 
                 valor_compra, info=None, visitas=0, vizinhanca=0, alugueis_recebidos=0):
        #Calculo da taxa de retorno de aluguel
        taxa = random.randint(1, (1000 - valor_compra) // 10)
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
        custo_mensal = []
        for valor in array_aluguel:
            custo_mensal.append(valor * 0.8) 
            
        self.custo_mensal = custo_mensal
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
        self.visitas = visitas #Contabiliza as vezes que um jogador caiu nessa casa
        self.vizinhanca = vizinhanca #Contabiliza as vezes que um jogador caiu nas casas vizinhas
        self.alugueis_recebidos = alugueis_recebidos #Vlores recebidos dealuguel
        
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
            jogador.premios += premio
        elif revez > sorte:
            multa = (revez - sorte) // 10 * 10
            mensagem = f"Multa: {multa}"
            jogador.remover_dinheiro(multa)
            jogador.multas += multa
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

class InputText:
    def __init__(self, x, y, width, height, font=None, font_size=32, text_color=black, cursor_color=black):
        self.rect = pygame.Rect(x, y, width, height)
        self.font = pygame.font.Font(font, font_size)
        self.text_color = text_color
        self.cursor_color = cursor_color
        self.text = ''
        self.active = False
        self.cursor_visible = True
        self.cursor_timer = 0

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Verifica se o campo de input foi clicado
            self.active = self.rect.collidepoint(event.pos)
        elif event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_RETURN:
                # Ação ao pressionar Enter (opcional)
                print(self.text)
                self.text = ''
            elif event.key == pygame.K_BACKSPACE:
                # Remove último caractere
                self.text = self.text[:-1]
            else:
                # Adiciona caractere ao texto
                self.text += event.unicode

    def update(self):
        # Atualiza o cursor piscante
        self.cursor_timer += 1
        if self.cursor_timer % 30 == 0:
            self.cursor_visible = not self.cursor_visible

    def draw(self, screen):
        # Desenha o campo de input e o texto
        pygame.draw.rect(screen, red, self.rect, 2)
        
        # Renderiza o texto
        text_surface = self.font.render(self.text, True, self.text_color)
        screen.blit(text_surface, (self.rect.x + 5, self.rect.y + 5))

        # Desenha o cursor piscante
        if self.active and self.cursor_visible:
            cursor_x = self.rect.x + 5 + text_surface.get_width()
            cursor_y = self.rect.y + 5
            pygame.draw.line(screen, self.cursor_color, (cursor_x, cursor_y), (cursor_x, cursor_y + self.font.get_height()), 2)

class NumberSelector:
    def __init__(self, x, y, width, height, options):
        self.rect = pygame.Rect(x, y, width, height)
        self.options = options
        self.selected = 2
        self.buttons = []
        self.create_buttons()

    def create_buttons(self):
        button_width = self.rect.width // len(self.options)
        button_height = self.rect.height
        
        for idx, option in enumerate(self.options):
            button_rect = pygame.Rect(self.rect.x + idx * button_width, self.rect.y, button_width, button_height)
            self.buttons.append((option, button_rect))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for option, button_rect in self.buttons:
                if button_rect.collidepoint(event.pos):
                    self.selected = option
                    print(f'Número selecionado: {self.selected}')

    def draw(self, screen):
        for option, button_rect in self.buttons:
            color = red if self.selected == option else gray
            pygame.draw.rect(screen, color, button_rect)
            font = pygame.font.Font(None, 36)
            text_surface = font.render(str(option), True, red)
            text_rect = text_surface.get_rect(center=button_rect.center)
            screen.blit(text_surface, text_rect)