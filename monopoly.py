import pygame
import sys
import classesMonopoly

# Inicializar o Pygame
pygame.init()

# Obter informações sobre a tela
screen_info = pygame.display.Info()

# Definir as dimensões da tela com base na resolução do sistema
screen_width = int(screen_info.current_w * 0.9)
screen_height = int(screen_info.current_h * 0.9)
pontoInicial = (max(screen_width, screen_height) - min(screen_width, screen_height)) / 2

# Calcular o tamanho dos quadrados proporcionalmente
square_size = min(screen_width, screen_height) // 10  # 1/20 da menor dimensão da tela

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

#Criar propriedades e outras casas do tabuleiro
propriedades = [classesMonopoly.Propriedade(yellow, black, "Inicio", "0", 1, "Banco", 0, [150, 200, 250, 300, 350]),
                classesMonopoly.Propriedade(yellow, black, "Inicio", "1", 1, None, 0, [150, 200, 250, 300, 350]),
                classesMonopoly.Propriedade(yellow, black, "Inicio", "2", 1, None, 0, [150, 200, 250, 300, 350]),
                classesMonopoly.Propriedade(yellow, black, "Inicio", "3", 1, None, 0, [150, 200, 250, 300, 350]),
                classesMonopoly.Propriedade(gray, black, "E Agora?", "4", 1, "Banco", 0, [150, 200, 250, 300, 350]),
                classesMonopoly.Propriedade(yellow, black, "Inicio", "5", 1, None, 0, [150, 200, 250, 300, 350]),
                classesMonopoly.Propriedade(yellow, black, "Inicio", "6", 1, None, 0, [150, 200, 250, 300, 350]),
                classesMonopoly.Propriedade(yellow, black, "Inicio", "7", 1, None, 0, [150, 200, 250, 300, 350]),
                classesMonopoly.Propriedade(yellow, black, "Inicio", "8", 1, None, 0, [150, 200, 250, 300, 350]),
                classesMonopoly.Propriedade(yellow, black, "Prisão", "9", 1, None, 0, [150, 200, 250, 300, 350]),
                classesMonopoly.Propriedade(yellow, black, "Inicio", "10", 1, None, 0, [150, 200, 250, 300, 350]),
                classesMonopoly.Propriedade(yellow, black, "Inicio", "11", 1,None, 0, [150, 200, 250, 300, 350]),
                classesMonopoly.Propriedade(yellow, black, "Inicio", "12", 1, None, 0, [150, 200, 250, 300, 350]),
                classesMonopoly.Propriedade(gray, black, "E Agora?", "13", 1, "Banco", 0, [150, 200, 250, 300, 350]),
                classesMonopoly.Propriedade(yellow, black, "Inicio", "14", 1, None, 0, [150, 200, 250, 300, 350]),
                classesMonopoly.Propriedade(yellow, black, "Inicio", "15", 1, None, 0, [150, 200, 250, 300, 350]),
                classesMonopoly.Propriedade(yellow, black, "Inicio", "16", 1, None, 0, [150, 200, 250, 300, 350]),
                classesMonopoly.Propriedade(yellow, black, "Inicio", "17", 1, None, 0, [150, 200, 250, 300, 350]),
                classesMonopoly.Propriedade(yellow, black, "Férias", "18", 1, None, 0, [150, 200, 250, 300, 350]),
                classesMonopoly.Propriedade(yellow, black, "Inicio", "19", 1, None, 0, [150, 200, 250, 300, 350]),
                classesMonopoly.Propriedade(yellow, black, "Inicio", "20", 1, None, 0, [150, 200, 250, 300, 350]),
                classesMonopoly.Propriedade(yellow, black, "Inicio", "21", 1, None, 0, [150, 200, 250, 300, 350]),
                classesMonopoly.Propriedade(gray, black, "E Agora?", "22", 1, "Banco", 0, [150, 200, 250, 300, 350]),
                classesMonopoly.Propriedade(yellow, black, "Inicio", "23", 1, None, 0, [150, 200, 250, 300, 350]),
                classesMonopoly.Propriedade(yellow, black, "Inicio", "24", 1, None, 0, [150, 200, 250, 300, 350]),
                classesMonopoly.Propriedade(yellow, black, "Inicio", "25", 1, None, 0, [150, 200, 250, 300, 350]),
                classesMonopoly.Propriedade(yellow, black, "Inicio", "26", 1, None, 0, [150, 200, 250, 300, 350]),
                classesMonopoly.Propriedade(yellow, black, "Vá p/ Prisão", "27", 1, "Banco", 0, [150, 200, 250, 300, 350]),
                classesMonopoly.Propriedade(yellow, black, "Inicio", "28", 1, None, 0, [150, 200, 250, 300, 350]),
                classesMonopoly.Propriedade(yellow, black, "Inicio", "29", 1, None, 0, [150, 200, 250, 300, 350]),
                classesMonopoly.Propriedade(yellow, black, "Inicio", "30", 1, None, 0, [150, 200, 250, 300, 350]),
                classesMonopoly.Propriedade(gray, black, "E Agora?", "31", 1, "Banco", 0, [150, 200, 250, 300, 350]),
                classesMonopoly.Propriedade(yellow, black, "Inicio", "32", 1, None, 0, [150, 200, 250, 300, 350]),
                classesMonopoly.Propriedade(yellow, black, "Inicio", "33", 1, None, 0, [150, 200, 250, 300, 350]),
                classesMonopoly.Propriedade(yellow, black, "Inicio", "34", 1, None, 0, [150, 200, 250, 300, 350]),
                classesMonopoly.Propriedade(yellow, black, "Inicio", "35", 1, None, 0, [150, 200, 250, 300, 350])]

#Instanciar cada casa do tabuleiro
casas = []
for i in range(0,10):
    casas.append(classesMonopoly.CasaTabuleiro(i, pontoInicial + i*square_size, 0, square_size, square_size, propriedades[i]))
    print(i)
print()
for i in range(10,19):
    casas.append(classesMonopoly.CasaTabuleiro(i, pontoInicial + square_size*9, (i-9)*square_size, square_size, square_size, propriedades[i]))
    print(i)
print()
for i in range(19,28):
    casas.append(classesMonopoly.CasaTabuleiro(i, pontoInicial + square_size*9 - (i-18)*square_size, square_size*9, square_size, square_size, propriedades[i]))
    print(i)
print()
for i in range(28,36):
    casas.append(classesMonopoly.CasaTabuleiro(i, pontoInicial, 9*square_size - (i-27)*square_size, square_size, square_size, propriedades[i]))
    print(i)

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

# Loop principal do jogo
while True:
    # Verificar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit() 

    # Preencher a tela com a cor branca
    screen.fill(white)
    
    # Desenhar o tabuleiro
    desenhar_casas_tabuleiro()

    # Atualizar a tela
    pygame.display.update()
