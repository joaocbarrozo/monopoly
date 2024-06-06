import pygame
import sys
import classesMonopoly
import random

# Inicializar o Pygame
pygame.init()

# Obter informações sobre a tela
screen_info = pygame.display.Info()

# Definir as dimensões da tela com base na resolução do sistema
screen_width = int(screen_info.current_w * 0.9)
screen_height = int(screen_info.current_h * 0.9)
#Definindo o ponto x inicial do tabuleiro 
pontoInicial = (max(screen_width, screen_height) - min(screen_width, screen_height)) / 2
# Calcular o tamanho dos quadrados proporcionalmente
square_size = min(screen_width, screen_height) // 10  # 1/10 da menor dimensão da tela
#Largura e altura do tabuleiro
board_size = square_size * 10
#Definir o centro do painel do jogo
painel_center = (screen_width - pontoInicial - board_size) / 2 + pontoInicial + board_size

# Definir as cores
white = (255, 255, 255)
black = (0, 0, 0)
yellow = (255, 255, 0)
orange = (255, 165, 0)
red = (255, 0, 0)
green = (0, 128, 0)
purple = (128, 0, 128)
blue = (0, 0, 255)
gray = (220, 220, 220)

# Criar a tela
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Tela com Quadrados na Borda")

#Inicia os jogadores
jogador1 = classesMonopoly.Jogador("Dé", 1500, orange)
jogador2 = classesMonopoly.Jogador("Gla", 1500, red)
jogador3 = classesMonopoly.Jogador("Galinari", 1500, blue)
jogador4 = classesMonopoly.Jogador("Tata", 1500, purple)
jogadores = [jogador1, jogador2, jogador3, jogador4]


#Criar propriedades e outras casas do tabuleiro
propriedades = [classesMonopoly.Propriedade(yellow, black, "Inicio", "0", 1, "Banco", 150, [150, 200, 250, 300, 350], 
                                            "Inicio do jogo, sempre que passar por esse ponto\n você receberá um valor em dinheiro"),
                classesMonopoly.Propriedade(yellow, black, "Inicio", "1", 1, None, 0, [150, 200, 250, 300, 350]),
                classesMonopoly.Propriedade(yellow, black, "Inicio", "2", 1, None, 0, [150, 200, 250, 300, 350]),
                classesMonopoly.Propriedade(yellow, black, "Inicio", "3", 1, None, 0, [150, 200, 250, 300, 350]),
                classesMonopoly.Propriedade(gray, black, "E Agora?", "4", 1, "Banco", 0, [150, 200, 250, 300, 350],
                                             "Tire uma carta será que hoje é seu dia de sorte?"),
                classesMonopoly.Propriedade(yellow, black, "Inicio", "5", 1, None, 0, [150, 200, 250, 300, 350]),
                classesMonopoly.Propriedade(yellow, black, "Inicio", "6", 1, None, 0, [150, 200, 250, 300, 350]),
                classesMonopoly.Propriedade(yellow, black, "Inicio", "7", 1, None, 0, [150, 200, 250, 300, 350]),
                classesMonopoly.Propriedade(yellow, black, "Inicio", "8", 1, None, 0, [150, 200, 250, 300, 350]),
                classesMonopoly.Propriedade(yellow, black, "Prisão", "9", 1, None, 0, [150, 200, 250, 300, 350], 
                                            "Você está apenas fazendo uma visita."),
                classesMonopoly.Propriedade(yellow, black, "Inicio", "10", 1, None, 0, [150, 200, 250, 300, 350]),
                classesMonopoly.Propriedade(yellow, black, "Inicio", "11", 1,None, 0, [150, 200, 250, 300, 350]),
                classesMonopoly.Propriedade(yellow, black, "Inicio", "12", 1, None, 0, [150, 200, 250, 300, 350]),
                classesMonopoly.Propriedade(gray, black, "E Agora?", "13", 1, "Banco", 0, [150, 200, 250, 300, 350],
                                            "Tire uma carta será que hoje é seu dia de sorte?"),
                classesMonopoly.Propriedade(yellow, black, "Inicio", "14", 1, None, 0, [150, 200, 250, 300, 350]),
                classesMonopoly.Propriedade(yellow, black, "Inicio", "15", 1, None, 0, [150, 200, 250, 300, 350]),
                classesMonopoly.Propriedade(yellow, black, "Inicio", "16", 1, None, 0, [150, 200, 250, 300, 350]),
                classesMonopoly.Propriedade(yellow, black, "Inicio", "17", 1, None, 0, [150, 200, 250, 300, 350]),
                classesMonopoly.Propriedade(yellow, black, "Férias", "18", 1, None, 0, [150, 200, 250, 300, 350], 
                                            "VocÊ está de ferias, fique uma vez sem jogar"),
                classesMonopoly.Propriedade(yellow, black, "Inicio", "19", 1, None, 0, [150, 200, 250, 300, 350]),
                classesMonopoly.Propriedade(yellow, black, "Inicio", "20", 1, None, 0, [150, 200, 250, 300, 350]),
                classesMonopoly.Propriedade(yellow, black, "Inicio", "21", 1, None, 0, [150, 200, 250, 300, 350]),
                classesMonopoly.Propriedade(gray, black, "E Agora?", "22", 1, "Banco", 0, [150, 200, 250, 300, 350],
                                            "Tire uma carta será que hoje é seu dia de sorte?"),
                classesMonopoly.Propriedade(yellow, black, "Inicio", "23", 1, None, 0, [150, 200, 250, 300, 350]),
                classesMonopoly.Propriedade(yellow, black, "Inicio", "24", 1, None, 0, [150, 200, 250, 300, 350]),
                classesMonopoly.Propriedade(yellow, black, "Inicio", "25", 1, None, 0, [150, 200, 250, 300, 350]),
                classesMonopoly.Propriedade(yellow, black, "Inicio", "26", 1, None, 0, [150, 200, 250, 300, 350]),
                classesMonopoly.Propriedade(yellow, black, "Vá p/ Prisão", "27", 1, "Banco", 0, [150, 200, 250, 300, 350], 
                                            "Vá para a prisão!"),
                classesMonopoly.Propriedade(yellow, black, "Inicio", "28", 1, None, 0, [150, 200, 250, 300, 350]),
                classesMonopoly.Propriedade(yellow, black, "Inicio", "29", 1, None, 0, [150, 200, 250, 300, 350]),
                classesMonopoly.Propriedade(yellow, black, "Inicio", "30", 1, None, 0, [150, 200, 250, 300, 350]),
                classesMonopoly.Propriedade(gray, black, "E Agora?", "31", 1, "Banco", 0, [150, 200, 250, 300, 350],
                                            "Tire uma carta será que hoje é seu dia de sorte?"),
                classesMonopoly.Propriedade(yellow, black, "Inicio", "32", 1, None, 0, [150, 200, 250, 300, 350]),
                classesMonopoly.Propriedade(yellow, black, "Inicio", "33", 1, None, 0, [150, 200, 250, 300, 350]),
                classesMonopoly.Propriedade(yellow, black, "Inicio", "34", 1, None, 0, [150, 200, 250, 300, 350]),
                classesMonopoly.Propriedade(yellow, black, "Inicio", "35", 1, None, 0, [150, 200, 250, 300, 350])]

#Instanciar cada casa do tabuleiro
casas = []
for i in range(0,10):
    casas.append(classesMonopoly.CasaTabuleiro(i, pontoInicial + i*square_size, 0, square_size, square_size, propriedades[i]))
    
for i in range(10,19):
    casas.append(classesMonopoly.CasaTabuleiro(i, pontoInicial + square_size*9, (i-9)*square_size, square_size, square_size, propriedades[i]))

for i in range(19,28):
    casas.append(classesMonopoly.CasaTabuleiro(i, pontoInicial + square_size*9 - (i-18)*square_size, square_size*9, square_size, square_size, propriedades[i]))

for i in range(28,36):
    casas.append(classesMonopoly.CasaTabuleiro(i, pontoInicial, 9*square_size - (i-27)*square_size, square_size, square_size, propriedades[i]))

partida = classesMonopoly.Partida(jogadores)

estado = 0

botao_jogar_dados = classesMonopoly.Button(green, painel_center, screen_height * 0.3, 120, 50, "Jogar Dados")


# Função para renderizar o texto em uma superfície separada
def render_text(text, font, color):
    text_surface = font.render(text, True, color)
    return text_surface, text_surface.get_rect()

# Função para exibir texto dentro de um retângulo
def draw_text_in_rect(text, rect, font, color):
    text_surface, text_rect = render_text(text, font, color)
    text_rect.center = rect.center
    screen.blit(text_surface, text_rect)

# Função para desenhar casa a casa do tabuleiro
def desenhar_casas_tabuleiro():
    for casa in casas:
        pygame.draw.rect(screen, casa.propriedade.borda_cor, (casa.posicao_x, casa.posicao_y, casa.width, casa.height), 2)
        if (casa.numero % 9 == 0 or casa.numero % 9 == 4 ):
            pygame.draw.rect(screen, casa.propriedade.cor, (casa.posicao_x + 2, casa.posicao_y + 2, casa.width - 4, casa.height - 4))
        else:    
            pygame.draw.rect(screen, casa.propriedade.cor, (casa.posicao_x + 2, casa.posicao_y + 2, casa.width - 4, casa.height / 3))
        # Desenha o titulo dentro do retângulo superior
        draw_text_in_rect(casa.propriedade.titulo, pygame.Rect(casa.posicao_x, casa.posicao_y, casa.width, casa.height / 3), pygame.font.Font(None, 24), black)
        draw_text_in_rect(casa.propriedade.texto, pygame.Rect(casa.posicao_x, casa.posicao_y, casa.width, casa.height), pygame.font.Font(None, 24), black)

def desenhar_estatisticas_jogadores():
    for i in range(0,len(jogadores)):
        pygame.draw.rect(screen, black, (5, (screen_height // len(jogadores)) * i, pontoInicial - 5, screen_height // len(jogadores)), 2)
        draw_text_in_rect(jogadores[i].nome, pygame.Rect(5, ((screen_height // len(jogadores)) * i) + 5, pontoInicial - 5, screen_height // len(jogadores) * 0.1), 
                          pygame.font.Font(None, 24), jogadores[i].cor)
        draw_text_in_rect("Saldo: R$ " + str(jogadores[i].dinheiro) + ",00", pygame.Rect(5, ((screen_height // len(jogadores)) * i) + 5, pontoInicial - 5, screen_height // len(jogadores) * 0.3), 
                          pygame.font.Font(None, 24), jogadores[i].cor)
        draw_text_in_rect("Quantidade Propriedades: " + str(len(jogadores[i].propriedades)), pygame.Rect(5, ((screen_height // len(jogadores)) * i) + 5, pontoInicial - 5, screen_height // len(jogadores) * 0.5), 
                          pygame.font.Font(None, 24), jogadores[i].cor)

def desenhar_painel_jogo():
    #Posição x do painel do lado direito do tabuleiro
    px = pontoInicial + board_size
    jogador = partida.jogador_Atual
    
    if estado == 0:
        draw_text_in_rect("Jogador: " + jogador.nome, pygame.Rect(px, 5, screen_width - px, screen_height * 0.1), 
                          pygame.font.Font(None, 24), jogador.cor)
        botao_jogar_dados.draw(screen)

def exibir_info_posicao_atual():
    posicao = partida.jogador_Atual.posicao
    propriedade = casas[posicao].propriedade
    if casas[posicao].propriedade.info != None:
        draw_text_in_rect(propriedade.info, pygame.Rect(pontoInicial + board_size + 5, screen_height * 0.5, 
                                                                       screen_width - pontoInicial - board_size - 10, screen_height * 0.5), 
                                                                        pygame.font.Font(None, 24), black) 
    else:
        draw_text_in_rect(f"{propriedade.titulo} valor R$ {propriedade.valor_compra},00", 
                          pygame.Rect(pontoInicial + board_size + 5, screen_height * 0.5, screen_width - pontoInicial - board_size - 10, screen_height * 0.5), 
                        pygame.font.Font(None, 24), black)

def desenhar_pinos():
    #Os pinos ocuparão apenas a parte branca dos quadrados
    #A posição x e y do ponto superior esquerdo da parte branca é px e py
    for i in range(0, len(jogadores)):
        px = casas[jogadores[i].posicao].posicao_x
        py = casas[jogadores[i].posicao].posicao_y
        #Dividindo a parte branca em quatro quadrantes transformando i em ix e iy
        ix = 1 if i < 2 else 3
        iy = 1 if i % 2 == 0 else 3 
        pygame.draw.circle(screen, jogadores[i].cor, (px + ix * square_size//4, py + iy * square_size//4),
                                                         casas[0].height * 0.1)

def jogar_dados():
    dado1 = random.randint(0,6000) % 6 + 1
    dado2 = random.randint(0,6000) % 6 + 1
    print(partida.jogador_Atual.posicao)
    print()
    dados = [dado1, dado2]
    return dados

# Loop principal do jogo
while partida.status == "Jogando":
    #Posição do mouse
    pos = pygame.mouse.get_pos()
    # Verificar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit() 
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if botao_jogar_dados.is_over(pos):
                resultado = jogar_dados()
                print(resultado)
                partida.jogador_Atual.mover(resultado[0] + resultado[1])

    
    # Altera o cursor quando o mouse estiver sobre o botão
    if botao_jogar_dados.is_over(pos):
        botao_jogar_dados.hover(screen)
    else:
        pygame.mouse.set_cursor(*pygame.cursors.arrow)
    # Preencher a tela com a cor branca
    screen.fill(white)
    
    # Desenhar o tabuleiro
    desenhar_casas_tabuleiro()
    
    desenhar_pinos()
    desenhar_estatisticas_jogadores()
    #Verificar estado da jogada, jogar dados, mover, decidir, terminar
    desenhar_painel_jogo()
    exibir_info_posicao_atual()

    # Atualizar a tela
    pygame.display.update()
