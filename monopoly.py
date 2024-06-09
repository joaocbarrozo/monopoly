import pygame
import sys
import classesMonopoly
import random
import time
import tabuleiroMonopoly

# Inicializar o Pygame
pygame.init()

# Obter informações sobre a tela
screen_info = pygame.display.Info()

# Definir as dimensões da tela com base na resolução do sistema
screen_width = int(screen_info.current_w * 0.95)
screen_height = int(screen_info.current_h * 0.7)
#Definindo o ponto x inicial do tabuleiro 
pontoInicial = (max(screen_width, screen_height) - min(screen_width, screen_height)) / 2
# Calcular o tamanho dos quadrados proporcionalmente
square_size = min(screen_width, screen_height) // 10  # 1/10 da menor dimensão da tela
#Largura e altura do tabuleiro
board_size = square_size * 10
#Definir o centro do painel do jogo
painel_center = (screen_width - pontoInicial - board_size) / 2 + pontoInicial + board_size
#Tamanho padrao das fontes
font_size = int(square_size * 0.3)
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
pygame.display.set_caption("Mundo dos Negócios")

#Inicia os jogadores
jogador1 = classesMonopoly.Jogador("Dé", 1500, orange)
jogador2 = classesMonopoly.Jogador("Gla", 1500, red)
jogador3 = classesMonopoly.Jogador("Galinari", 1500, blue)
jogador4 = classesMonopoly.Jogador("Tata", 1500, purple)
jogadores = [jogador1, jogador2, jogador3, jogador4]

#Instanciar cada casa do tabuleiro
casas = tabuleiroMonopoly.casas

imagens = tabuleiroMonopoly.carregar_imagens()

#Variaveis globais
partida = classesMonopoly.Partida(jogadores)
resultado = [1, 6]
estado = 0
rodada = 1

botao_jogar_dados = classesMonopoly.Button(painel_center - 60, screen_height/2, 120, 50,
                                           "Jogar Dados", pygame.font.Font(None, font_size), green, red, blue)
botao_mover = classesMonopoly.Button(painel_center - 60, screen_height/2 + 60, 120, 50,
                                           "Mover", pygame.font.Font(None, font_size), green, red, blue)
botao_comprar = classesMonopoly.Button(painel_center - 60, screen_height/2, 120, 50,
                                           "Comprar", pygame.font.Font(None, font_size), green, red, blue)
botao_melhorar = classesMonopoly.Button(painel_center - 60, screen_height/2, 120, 50,
                                           "Melhorar", pygame.font.Font(None, font_size), green, red, blue)
botao_terminar = classesMonopoly.Button(painel_center - 60, screen_height/2 + 120, 120, 50,
                                           "Terminar", pygame.font.Font(None, font_size), green, red, blue)
botao_pagar = classesMonopoly.Button(painel_center - 60, screen_height/2, 120, 50,
                                           "Pagar", pygame.font.Font(None, font_size), green, red, blue)
botao_pegar_carta = classesMonopoly.Button(painel_center - 60, screen_height/2, 120, 50,
                                           "Pegar Carta", pygame.font.Font(None, font_size), green, red, blue)
botao_ok = classesMonopoly.Button(painel_center - 60, screen_height/2, 120, 50,
                                           "Ok", pygame.font.Font(None, font_size), green, red, blue)

#textBox_info = classesMonopoly.TextBox(pontoInicial + board_size + 5, )


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
        pygame.draw.rect(screen, casa.propriedade.borda_cor, (casa.posicao_x, casa.posicao_y, casa.width, casa.height), 4)
        if (casa.numero % 9 == 0 or casa.numero % 9 == 4 ):
            pygame.draw.rect(screen, casa.propriedade.cor, (casa.posicao_x + 4, casa.posicao_y + 4, casa.width - 8, casa.height - 8))
        else:    
            pygame.draw.rect(screen, casa.propriedade.cor, (casa.posicao_x + 4, casa.posicao_y + 4, casa.width - 8, casa.height / 3))
        # Desenha o titulo dentro do retângulo superior
        draw_text_in_rect(casa.propriedade.titulo, pygame.Rect(casa.posicao_x, casa.posicao_y, casa.width, casa.height / 3), pygame.font.Font(None, int(font_size * 0.7)), black)
        draw_text_in_rect(casa.propriedade.texto, pygame.Rect(casa.posicao_x, casa.posicao_y, casa.width, casa.height), pygame.font.Font(None, font_size), black)
        for imagem in imagens:
            screen.blit(imagem[0], imagem[1])

def desenhar_estatisticas_jogadores():
    for i in range(0,len(jogadores)):
        pygame.draw.rect(screen, black, (5, (screen_height // len(jogadores)) * i, pontoInicial - 5, screen_height // len(jogadores)), 2)
        draw_text_in_rect(jogadores[i].nome, pygame.Rect(5, ((screen_height // len(jogadores)) * i) + 5, pontoInicial - 5, screen_height // len(jogadores) * 0.1), 
                          pygame.font.Font(None, int(font_size * 1.2)), jogadores[i].cor)
        draw_text_in_rect("Saldo: R$ " + str(jogadores[i].dinheiro) + ",00", pygame.Rect(5, ((screen_height // len(jogadores)) * i) + 5, pontoInicial - 5, screen_height // len(jogadores) * 0.3), 
                          pygame.font.Font(None, int(font_size * 1.1)), jogadores[i].cor)
        draw_text_in_rect("Quantidade Propriedades: " + str(len(jogadores[i].propriedades)), pygame.Rect(5, ((screen_height // len(jogadores)) * i) + 5, pontoInicial - 5, screen_height // len(jogadores) * 0.5), 
                          pygame.font.Font(None, int(font_size * 1.1)), jogadores[i].cor)

def desenhar_painel_jogo():
    #Jogar dados
    if estado == 0:
        botao_jogar_dados.draw(screen)
    #Mover o jogador
    elif estado == 1:
        botao_mover.draw(screen)
    #Possibilidade de compra
    elif estado == 2:
        botao_comprar.draw(screen)
        botao_terminar.draw(screen)
    #Possibilidade de aumentar o nivel da propriedade
    elif estado == 3:
        botao_melhorar.draw(screen)
        botao_terminar.draw(screen)
    #E agora ?
    elif estado == 4:
        botao_pegar_carta.draw(screen)
    #Nada a fazer
    elif estado == 5:
        botao_ok.draw(screen)
    #Férias, uma rodada sem jogar
    elif estado == 6:
        botao_ok.draw(screen)
    #Vá para prisão
    elif estado == 7:
        botao_ok.draw(screen)
    #Propriedade de outro jogador
    elif estado == 8:
        botao_pagar.draw(screen)
    #Terminar a vez
    else:  
        botao_terminar.draw(screen)

def exibir_info_posicao_atual():
    #Posição x do painel do lado direito do tabuleiro
    px = pontoInicial + board_size
    jogador = partida.jogador_Atual
    posicao = partida.jogador_Atual.posicao
    propriedade = casas[posicao].propriedade
    draw_text_in_rect("Jogador: " + jogador.nome, pygame.Rect(px, 5, screen_width - px, screen_height * 0.05), 
                          pygame.font.Font(None, font_size), jogador.cor)
    if casas[posicao].propriedade.info != None:
        draw_text_in_rect(propriedade.info, pygame.Rect(pontoInicial + board_size + 5, screen_height * 0.5, 
                                                                       screen_width - pontoInicial - board_size - 10, screen_height * 0.5), 
                                                                        pygame.font.Font(None, font_size), black) 
    else:
        draw_text_in_rect(f"{propriedade.titulo} valor R$ {propriedade.valor_compra},00", 
                          pygame.Rect(pontoInicial + board_size + 5, screen_height * 0.5, screen_width - pontoInicial - board_size - 10, screen_height * 0.5), 
                        pygame.font.Font(None, font_size), black)

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
    dados = [dado1, dado2]
    return dados

def desenhar_numeros_dado(pos_x, pos_y, dado_size, valor):
    if valor == 1:
        pygame.draw.circle(screen, black, (pos_x + dado_size/2, pos_y + dado_size/2), dado_size/12)
    elif valor == 2:
        pygame.draw.circle(screen, black, (pos_x + dado_size/4, pos_y + dado_size/4), dado_size/12)
        pygame.draw.circle(screen, black, (pos_x + 3 * dado_size/4, pos_y + 3 * dado_size/4), dado_size/12)
    elif valor == 3:
        pygame.draw.circle(screen, black, (pos_x + dado_size/4, pos_y + dado_size/4), dado_size/12)
        pygame.draw.circle(screen, black, (pos_x + dado_size/2, pos_y + dado_size/2), dado_size/12)
        pygame.draw.circle(screen, black, (pos_x + 3 * dado_size/4, pos_y + 3 * dado_size/4), dado_size/12)
    elif valor == 4:
        pygame.draw.circle(screen, black, (pos_x + dado_size/4, pos_y + dado_size/4), dado_size/12)
        pygame.draw.circle(screen, black, (pos_x + 3 * dado_size/4, pos_y + dado_size/4), dado_size/12)
        pygame.draw.circle(screen, black, (pos_x + dado_size/4, pos_y + 3 * dado_size/4), dado_size/12)
        pygame.draw.circle(screen, black, (pos_x + 3 * dado_size/4, pos_y + 3 * dado_size/4), dado_size/12)
    elif valor == 5:
        pygame.draw.circle(screen, black, (pos_x + dado_size/4, pos_y + dado_size/4), dado_size/12)
        pygame.draw.circle(screen, black, (pos_x + 3 * dado_size/4, pos_y + dado_size/4), dado_size/12)
        pygame.draw.circle(screen, black, (pos_x + dado_size/2, pos_y + dado_size/2), dado_size/12)
        pygame.draw.circle(screen, black, (pos_x + dado_size/4, pos_y + 3 * dado_size/4), dado_size/12)
        pygame.draw.circle(screen, black, (pos_x + 3 * dado_size/4, pos_y + 3 * dado_size/4), dado_size/12)
    elif valor == 6:
        pygame.draw.circle(screen, black, (pos_x + dado_size/4, pos_y + dado_size/4), dado_size/12)
        pygame.draw.circle(screen, black, (pos_x + 3 * dado_size/4, pos_y + dado_size/4), dado_size/12)
        pygame.draw.circle(screen, black, (pos_x + dado_size/4, pos_y + dado_size/2), dado_size/12)
        pygame.draw.circle(screen, black, (pos_x + 3 * dado_size/4, pos_y + dado_size/2), dado_size/12)
        pygame.draw.circle(screen, black, (pos_x + dado_size/4, pos_y + 3 * dado_size/4), dado_size/12)
        pygame.draw.circle(screen, black, (pos_x + 3 * dado_size/4, pos_y + 3 * dado_size/4), dado_size/12)
 
    
def desenhar_dados(resultado):
    dado_size = square_size * 0.6
    dado1_px = screen_width /2 - dado_size
    dado1_py = screen_height /2 - dado_size
    dado2_px = screen_width /2 + dado_size
    dado2_py = screen_height /2 - dado_size
    pygame.draw.rect(screen, black,(dado1_px, dado1_py, dado_size, dado_size), 2)
    pygame.draw.rect(screen, black,(dado2_px, dado2_py, dado_size, dado_size), 2)
    desenhar_numeros_dado(dado1_px, dado1_py, dado_size, resultado[0])
    desenhar_numeros_dado(dado2_px, dado2_py, dado_size, resultado[1])

# Loop principal do jogo
while partida.status == "Jogando":
    #Posição do mouse
    pos = pygame.mouse.get_pos()
    # Verificar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit() 
        if estado == 0:
            #Jogador atual
            jogador = partida.jogador_Atual
            #Posição anterior
            pos_inicial = jogador.posicao
            #Caso o jogador tenha caido nas ferias na rodada anterior fica uma vez sem jogar
            if partida.jogador_Atual.ferias > 0:
                print("Voce está de ferias e não jogara nessa rodada")
                partida.jogador_Atual.ferias -= 1
                estado = 9
            if botao_jogar_dados.handle_event(event):
                resultado = jogar_dados()
                #Se o jogador está na prisão verificar se tirou numeros iguais no dado para sair
                if jogador.posicao == 9 and jogador.prisao > 0:
                    if jogador.prisao < 4:
                        if resultado[0] == resultado[1]:
                            jogador.prisao = 0
                            estado = 1
                        else:
                            print(f"Voce não conseguiu sair!")
                            print(f"Essa foi sua tentativa número {jogador.prisao}")
                            jogador.prisao +=1
                            estado = 9
                    else:
                        print("Voce pagou R$ 200,00 pra poder sair!")
                        if jogador.remover_dinheiro(200):
                            estado = 1
                        else:
                            jogador.prisao -= 1
                estado = 1
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        if estado == 1:
            if botao_mover.handle_event(event):
                jogador.mover(resultado[0] + resultado[1])
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                pos_atual = jogador.posicao
                #Propriedade em que o jogador está
                propriedade = casas[jogador.posicao].propriedade
                print(f"Proprietario: {propriedade.proprietario}")
                #Verificar se o jogador passou pelo inicio
                if pos_atual < pos_inicial:
                    print("Voce passou pelo inicio e recebeu R$ 200,00")
                    jogador.adicionar_dinheiro(200)
                #Possibilidade de compra
                if propriedade.proprietario == None:
                    estado = 2
                #Possibilidade de aumentar o nivel da propriedade
                elif propriedade.proprietario == jogador:
                    estado = 3 
                #E agora ?
                elif jogador.posicao % 9 == 4:
                    estado = 4
                #Nada a fazer
                elif jogador.posicao == 0 or jogador.posicao == 9:
                    estado = 5
                #Férias, uma rodada sem jogar
                elif jogador.posicao == 18:
                    print("Voce está de férias e ficará uma vez sem jogar!")
                    jogador.ferias = 1
                    estado = 6
                #Vá para prisão
                elif jogador.posicao == 27:
                    print("Vá para a prisão sem receber nada!")
                    estado = 7
                #Propriedade de outro jogador
                else:
                    estado = 8
        #Possibilidade de compra
        if estado == 2:
            if botao_comprar.handle_event(event):
                if jogador.comprar_propriedade(propriedade):
                    print(f"{jogador.nome} comprou {propriedade.titulo}")
                else:
                    print(f"Você não tem dinheiro suficiente")
                estado = 9
            if botao_terminar.handle_event(event):
                partida.jogada +=1
                rodada = partida.jogada // 4
                print(f"Jogada: {partida.jogada} Rodada: {rodada}")
                partida.jogador_Atual = partida.jogadores[partida.jogada % 4]
                estado = 0
        #Possibilidade de aumentar o nivel da propriedade
        if estado == 3:
            if botao_melhorar.handle_event(event):
                if propriedade.melhorar_propriedade():
                    print(f"{propriedade.titulo} melhorada para o nivel {propriedade.nivel}")
                else:
                    print(f"Você não tem dinheiro suficiente")
                estado = 9
            if botao_terminar.handle_event(event):
                partida.jogada +=1
                rodada = partida.jogada // 4
                print(f"Jogada: {partida.jogada} Rodada: {rodada}")
                partida.jogador_Atual = partida.jogadores[partida.jogada % 4]
                estado = 0
        #E agora ?
        if estado == 4:
            if botao_pegar_carta.handle_event(event):
                propriedade.sorteio_eAgora(jogador)
                estado = 9
        #Nada a fazer
        if estado == 5:
            if botao_ok.handle_event(event):
                estado = 9
        #Férias, uma rodada sem jogar
        if estado == 6:
            if botao_ok.handle_event(event):
                estado = 9
        #Vá para prisão
        if estado == 7:
            if botao_ok.handle_event(event):
                jogador.prisao = 1
                jogador.posicao = 9
                estado = 9
        #Propriedade de outro jogador
        if estado == 8:
            if botao_pagar.handle_event(event):
                if jogador.pagar_aluguel(propriedade.proprietario, propriedade.valor_aluguel[propriedade.nivel - 1]):
                    print(f"Você pagou R$ {propriedade.valor_aluguel[propriedade.nivel - 1]},00 para {propriedade.proprietario.nome}")
                    estado = 9
                else:
                    print("Voce não tem dinheiro suficiente")
                    estado = 9
        #Terminar a vez
        if estado == 9:
            if botao_terminar.handle_event(event):
                partida.jogada +=1
                rodada = partida.jogada // 4
                print(f"Jogada: {partida.jogada} Rodada: {rodada}")
                partida.jogador_Atual = partida.jogadores[partida.jogada % 4]
                estado = 0
            
    # Preencher a tela com a cor branca
    screen.fill(white)
    
    # Desenhar o tabuleiro
    desenhar_casas_tabuleiro()
    desenhar_dados(resultado)
    desenhar_pinos()
    desenhar_estatisticas_jogadores()
    #Verificar estado da jogada, jogar dados, mover, decidir, terminar
    desenhar_painel_jogo()
    exibir_info_posicao_atual()
    

    # Atualizar a tela
    pygame.display.update()
