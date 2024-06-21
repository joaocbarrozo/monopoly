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
screen_width = tabuleiroMonopoly.screen_width
screen_height = tabuleiroMonopoly.screen_height
#Definindo o ponto x inicial do tabuleiro 
pontoInicial = tabuleiroMonopoly.pontoInicial
# Calcular o tamanho dos quadrados proporcionalmente
square_size = tabuleiroMonopoly.square_size
#Largura e altura do tabuleiro
board_size = square_size * 10
board_center = pontoInicial + board_size / 2
#Definir a posição x do painel
painel_x = pontoInicial + board_size
#Definir o centro do painel do jogo
painel_center = (screen_width - pontoInicial - board_size) / 2 + pontoInicial + board_size
#definir o tamanho do painel
painel_size = screen_width - painel_x
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
dark_gray = (120, 120, 120)

# Criar a tela
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Mundo dos Negócios")

#Inicia os jogadores
jogador1 = classesMonopoly.Jogador("Dé", 1500, orange, 1500)
jogador2 = classesMonopoly.Jogador("Gla", 1500, red, 1500)
jogador3 = classesMonopoly.Jogador("Galinari", 1500, blue, 1500)
jogador4 = classesMonopoly.Jogador("Tata", 1500, purple, 1500)
jogadores = [jogador1, jogador2, jogador3, jogador4]

#Instanciar cada casa do tabuleiro
casas = tabuleiroMonopoly.casas

imagens = tabuleiroMonopoly.carregar_imagens()

#Variaveis globais
partida = classesMonopoly.Partida(jogadores)
resultado = [1, 6]
tela = ""
estado = 0
rodada = 1
ranking = []
inputText_array = []

#Botões
botao_jogar_dados = classesMonopoly.Button(painel_center - 60, 3 * screen_height/4, 120, 50,
                                           "Jogar Dados", pygame.font.Font(None, font_size), green, red, blue)
botao_mover = classesMonopoly.Button(painel_center - 60, 3 * screen_height/4 + 60, 120, 50,
                                           "Mover", pygame.font.Font(None, font_size), green, red, blue)
botao_comprar = classesMonopoly.Button(painel_center - 60, 3 * screen_height/4, 120, 50,
                                           "Comprar", pygame.font.Font(None, font_size), green, red, blue)
botao_melhorar = classesMonopoly.Button(painel_center - 60, 3 * screen_height/4, 120, 50,
                                           "Melhorar", pygame.font.Font(None, font_size), green, red, blue)
botao_terminar = classesMonopoly.Button(painel_center - 60, 3 * screen_height/4 + 120, 120, 50,
                                           "Terminar", pygame.font.Font(None, font_size), green, red, blue)
botao_pagar = classesMonopoly.Button(painel_center - 60, 3 * screen_height/4, 120, 50,
                                           "Pagar", pygame.font.Font(None, font_size), green, red, blue)
botao_pegar_carta = classesMonopoly.Button(painel_center - 60, 3 * screen_height/4, 120, 50,
                                           "Pegar Carta", pygame.font.Font(None, font_size), green, red, blue)
botao_ok = classesMonopoly.Button(painel_center - 60, 3 * screen_height/4, 120, 50,
                                           "Ok", pygame.font.Font(None, font_size), green, red, blue)
botao_novoJogo = classesMonopoly.Button(screen_width / 2 - 60, screen_height * 0.2, 120, 50, 
                                        "Novo", pygame.font.Font(None, font_size), green, red, blue)
botao_carregarJogo = classesMonopoly.Button(screen_width / 2 - 60, screen_height * 0.4, 120, 50, 
                                        "Carregar", pygame.font.Font(None,font_size), green, red, blue)
botao_sair = classesMonopoly.Button(screen_width / 2 - 60, screen_height * 0.6, 120, 50, 
                                        "Sair", pygame.font.Font(None, font_size), green, red, blue)
seletor_jogadores = classesMonopoly.NumberSelector(screen_width / 2 - 30, screen_height / 4, 60, 30, [2,3,4,5,6])

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

def desenhar_menu():
    draw_text_in_rect("Mundo dos Negócios", pygame.Rect(0, 15, screen_width, 100), pygame.font.Font(None,2 * font_size),red)
    botao_novoJogo.draw(screen)
    botao_carregarJogo.draw(screen)
    botao_sair.draw(screen)

def desenhar_novoJogo(qtd):
    #inputText_array = []
    screen.fill(white)
    draw_text_in_rect("Novo Jogo", pygame.Rect(0, 15, screen_width, 100), pygame.font.Font(None,2 * font_size),red)
    seletor_jogadores.draw(screen)
    for i in range(1, qtd + 1):
        inputText_array.append(classesMonopoly.InputText(screen_width / 2 - 120, screen_height / 2 + i * 60, 240, 50))
    for inputText in inputText_array:
        inputText.draw(screen)
# Função para desenhar casa a casa do tabuleiro
def desenhar_casas_tabuleiro():
    for casa in casas:
        pygame.draw.rect(screen, casa.propriedade.borda_cor, (casa.posicao_x, casa.posicao_y, casa.width, casa.height), 4)
        if (casa.numero % 9 == 0 or casa.numero % 9 == 4 ):
            pygame.draw.rect(screen, casa.propriedade.cor, (casa.posicao_x + 4, casa.posicao_y + 4, casa.width - 8, casa.height - 8))
        else:    
            pygame.draw.rect(screen, casa.propriedade.cor, (casa.posicao_x + 4, casa.posicao_y + 4, casa.width - 8, casa.height / 3))
        # Desenha o titulo dentro do retângulo superior
        #draw_text_in_rect(casa.propriedade.titulo, pygame.Rect(casa.posicao_x, casa.posicao_y, casa.width, casa.height / 3), pygame.font.Font(None, int(font_size * 0.7)), black)
        #draw_text_in_rect(casa.propriedade.texto, pygame.Rect(casa.posicao_x, casa.posicao_y, casa.width, casa.height), pygame.font.Font(None, font_size), black)
        for imagem in imagens:
            screen.blit(pygame.transform.scale(imagem[0], (square_size - 8, square_size - 8)), imagem[1])

def desenhar_estatisticas_jogadores():
    for i in range(0,len(jogadores)):
        pygame.draw.rect(screen, black, (5, (screen_height // len(jogadores)) * i, pontoInicial - 5, screen_height // len(jogadores)), 2)
        draw_text_in_rect(jogadores[i].nome, pygame.Rect(5, ((screen_height // len(jogadores)) * i) + 5, pontoInicial - 5, screen_height // len(jogadores) * 0.1), 
                          pygame.font.Font(None, int(font_size * 1.2)), jogadores[i].cor)
        draw_text_in_rect("Saldo: R$ " + str(jogadores[i].dinheiro) + ",00", pygame.Rect(5, ((screen_height // len(jogadores)) * i) + 5, pontoInicial - 5, screen_height // len(jogadores) * 0.3), 
                          pygame.font.Font(None, int(font_size * 1.1)), jogadores[i].cor)
        draw_text_in_rect("Quantidade Propriedades: " + str(len(jogadores[i].propriedades)), pygame.Rect(5, ((screen_height // len(jogadores)) * i) + 5, pontoInicial - 5, screen_height // len(jogadores) * 0.5), 
                          pygame.font.Font(None, int(font_size * 1.1)), jogadores[i].cor)
        draw_text_in_rect("Patrimonio: R$ " + str(jogadores[i].patrimonio) + ",00", pygame.Rect(5, ((screen_height // len(jogadores)) * i) + 5, pontoInicial - 5, screen_height // len(jogadores) * 0.7), 
                          pygame.font.Font(None, int(font_size * 1.1)), jogadores[i].cor)
        
#Desenha os botoes de acordo com o estado do jogo
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
    #Escreve o nome do jogador no topo da tela
    draw_text_in_rect("Jogador: " + jogador.nome, pygame.Rect(px, 5, screen_width - px, screen_height * 0.05), 
                          pygame.font.Font(None, font_size), jogador.cor)
    draw_text_in_rect(f"{propriedade.titulo}", 
                          pygame.Rect(pontoInicial + board_size + 5, screen_height * 0.03, screen_width - pontoInicial - board_size - 10, screen_height * 0.1), 
                        pygame.font.Font(None, font_size), black)
    #Coloca a imagem da casa atual abaixo do nome
    screen.blit(pygame.transform.scale(imagens[posicao][0], (painel_size / 2, painel_size / 2)), (painel_x + painel_size / 4, screen_height * 0.1))
    if casas[posicao].propriedade.info != None:
        '''draw_text_in_rect(propriedade.info, pygame.Rect(pontoInicial + board_size + 5, screen_height * 0.4, 
                                                                       screen_width - pontoInicial - board_size - 10, screen_height * 0.5), 
                                                                        pygame.font.Font(None, font_size), black)'''
    else:
        draw_text_in_rect(f"Valor Compra: R$ {propriedade.valor_compra},00", 
                          pygame.Rect(pontoInicial + board_size + 5, screen_height * 0.4, screen_width - pontoInicial - board_size - 10, screen_height * 0.1), 
                        pygame.font.Font(None, font_size), black)
        draw_text_in_rect(f"Proprietario: {propriedade.proprietario}", 
                          pygame.Rect(pontoInicial + board_size + 5, screen_height * 0.425, screen_width - pontoInicial - board_size - 10, screen_height * 0.1), 
                        pygame.font.Font(None, font_size), black)
        draw_text_in_rect(f"Nivel Atual: {propriedade.nivel}", 
                          pygame.Rect(pontoInicial + board_size + 5, screen_height * 0.45, screen_width - pontoInicial - board_size - 10, screen_height * 0.1), 
                        pygame.font.Font(None, font_size), black)
        draw_text_in_rect(f"Aluguel Nivel 1: R$ {propriedade.valor_aluguel[0]},00", 
                          pygame.Rect(pontoInicial + board_size + 5, screen_height * 0.475, screen_width - pontoInicial - board_size - 10, screen_height * 0.1), 
                        pygame.font.Font(None, font_size), black)
        draw_text_in_rect(f"Aluguel Nivel 2: R$ {propriedade.valor_aluguel[1]},00", 
                          pygame.Rect(pontoInicial + board_size + 5, screen_height * 0.5, screen_width - pontoInicial - board_size - 10, screen_height * 0.1), 
                        pygame.font.Font(None, font_size), black)
        draw_text_in_rect(f"Aluguel Nivel 3: R$ {propriedade.valor_aluguel[2]},00", 
                          pygame.Rect(pontoInicial + board_size + 5, screen_height * 0.525, screen_width - pontoInicial - board_size - 10, screen_height * 0.1), 
                        pygame.font.Font(None, font_size), black)
        draw_text_in_rect(f"Aluguel Nivel 4: R$ {propriedade.valor_aluguel[3]},00", 
                          pygame.Rect(pontoInicial + board_size + 5, screen_height * 0.55, screen_width - pontoInicial - board_size - 10, screen_height * 0.1), 
                        pygame.font.Font(None, font_size), black)
        draw_text_in_rect(f"Aluguel Nivel 5: R$ {propriedade.valor_aluguel[4]},00", 
                          pygame.Rect(pontoInicial + board_size + 5, screen_height * 0.575, screen_width - pontoInicial - board_size - 10, screen_height * 0.1), 
                        pygame.font.Font(None, font_size), black)
        draw_text_in_rect(f"Ranking: {propriedade.ranking}", 
                          pygame.Rect(pontoInicial + board_size + 5, screen_height * 0.6, screen_width - pontoInicial - board_size - 10, screen_height * 0.1), 
                        pygame.font.Font(None, font_size), black)

def exibir_mensagem(mensagem):
    #print(f"Mensagem {mensagem}")
    #Desenhar retangulo preenchido do titulo da caixa de texto
    pygame.draw.rect(screen, dark_gray, (pontoInicial + square_size * 3, square_size * 2 - 20, square_size * 4, square_size * 0.25))
    #Desenhar borda da caixa de texto
    pygame.draw.rect(screen, dark_gray, (pontoInicial + square_size * 3, square_size * 2, square_size * 4, square_size * 2), 2)
    #Escrever no retangulo preenchido do titulo
    draw_text_in_rect(f"Mensagem para {partida.jogador_Atual.nome}", 
                          pygame.Rect(pontoInicial + square_size * 3, square_size * 2 - 16, square_size * 4, square_size * 0.2), 
                        pygame.font.Font(None, font_size), white)
    text  = classesMonopoly.TextBox(pontoInicial + square_size * 3 + 4, square_size * 2 + 4, square_size * 4, square_size * 2, font_size, mensagem, black)
    text.draw(screen)
    
def exibir_informações():
    #Desenhar retangulo preenchido do titulo da caixa de texto
    pygame.draw.rect(screen, dark_gray, (pontoInicial + square_size * 3, square_size * 6 - 20, square_size * 4, square_size * 0.25))
    #Desenhar borda da caixa de texto
    pygame.draw.rect(screen, dark_gray, (pontoInicial + square_size * 3, square_size * 6, square_size * 4, square_size * 2), 2)
    #Escrever no retangulo preenchido do titulo
    draw_text_in_rect(f"Rodada {partida.jogada // 4 + 1}", 
                          pygame.Rect(pontoInicial + square_size * 3, square_size * 6 - 16, square_size * 4, square_size * 0.2), 
                        pygame.font.Font(None, font_size), white)
    text  = classesMonopoly.TextBox(pontoInicial + square_size * 3 + 4, square_size * 6 + 4, square_size * 4, square_size * 2, font_size, f"Informaçoes da partida", black)
    text.draw(screen)

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
                                                         casas[0].height * 0.15)

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
    dado1_px = board_center - dado_size - square_size*0.4
    dado1_py = screen_height /2 - dado_size
    dado2_px = board_center + dado_size- square_size*0.4
    dado2_py = screen_height /2 - dado_size
    pygame.draw.rect(screen, black,(dado1_px, dado1_py, dado_size, dado_size), 2)
    pygame.draw.rect(screen, black,(dado2_px, dado2_py, dado_size, dado_size), 2)
    desenhar_numeros_dado(dado1_px, dado1_py, dado_size, resultado[0])
    desenhar_numeros_dado(dado2_px, dado2_py, dado_size, resultado[1])

def rankPopularidade(casas):
        # Ordenar as casas de acordo com a popularidade de forma decrescente
        ranking = sorted(casas, key=lambda x: x.propriedade.popularidade, reverse=True)
        # Remover as propriedades do banco do ranking 
        for casa in ranking:
            print(casa.propriedade.titulo)
            if casa.propriedade.proprietario == "Banco":
                ranking.remove(casa)
                print(f"{casa.propriedade.titulo} removida")
        # Preencher o ranking atualizado de cada propriedade
        for i in range(0, len(ranking)):
            for casa in casas:
                if ranking[i].propriedade.titulo == casa.propriedade.titulo:
                    casa.propriedade.ranking = i + 1
                    print(f"{i + 1}º {casa.propriedade.titulo} {casa.propriedade.popularidade}")
                    if casa.propriedade.proprietario in jogadores:
                        casa.propriedade.calculaReceitasDespesas()
    
        return ranking

#Loop principal
while True:
    while tela == "menu":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit() 
            if botao_novoJogo.handle_event(event):
                tela = "novoJogo"
            if botao_carregarJogo.handle_event(event):
                print("Carregar jogo")
            if botao_sair.handle_event(event):
                pygame.quit()
                sys.exit()
    
        screen.fill(white)
        #Posição do mouse
        pos = pygame.mouse.get_pos()
        desenhar_menu()
        # Atualizar a tela
        pygame.display.update()
    
    while tela == "novoJogo":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit() 
            seletor_jogadores.handle_event(event)
            for i in range(0, seletor_jogadores.selected):
                inputText_array[i].handle_event(event)
                
        screen.fill(white)
        #Posição do mouse
        pos = pygame.mouse.get_pos()
        desenhar_novoJogo(seletor_jogadores.selected)
        # Atualizar a tela
        pygame.display.update()

    # Loop do jogo
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
                partida.mensagem = f"{jogador.nome} é a sua vez! Jogue os dados para se movimentar."
                #Caso o jogador tenha caido nas ferias na rodada anterior fica uma vez sem jogar
                if partida.jogador_Atual.ferias > 0:
                    partida.mensagem = ("Voce está de ferias e não jogará nessa rodada")
                    jogador.rodadasFerias += 1
                    jogador.ferias -= 1
                    estado = 9
                if botao_jogar_dados.handle_event(event):
                    resultado = jogar_dados()
                    partida.mensagem = f"A soma dos dados deu {resultado[0] + resultado[1]}."
                    #Se o jogador está na prisão verificar se tirou numeros iguais no dado para sair
                    if jogador.posicao == 9 and jogador.congelamento > 0:
                        if jogador.congelamento < 4:
                            if resultado[0] == resultado[1]:
                                partida.mensagem += "Você estava no congelamento mas como tirou números iguais nos dados conseguiu descongelar os seus negócios!"
                                jogador.congelamento = 0
                                estado = 1
                            else:
                                partida.mensagem += (f"Voce não conseguiu sair! è necessário tirar valores iguais nos dados para descongelar seus negócios.")
                                partida.mensagem += (f"Essa foi sua tentativa número {jogador.congelamento}.")
                                jogador.rodadasCongelamento += 1
                                jogador.congelamento +=1
                                estado = 9
                        else:
                            partida.mensagem += ("Você pagou R$ 200,00 pra poder sair! Na próxima rodada seus negócios estarão descongelados!")
                            jogador.remover_dinheiro(200)
                            estado = 1
                            '''else:
                                partida.mensagem += "Você não tem dinheiro suficiente para descongelar seus negócios tente novamente nos dados na próxima rodada."
                                jogador.congelamento -= 1
                                estado = 9'''
                    else:
                        estado = 1
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            #Mover pino
            if estado == 1:
                if botao_mover.handle_event(event):
                    jogador.mover(resultado[0] + resultado[1])
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                    pos_atual = jogador.posicao
                    #Propriedade em que o jogador está
                    propriedade = casas[jogador.posicao].propriedade
                    #Calcular popularidade
                    casas[pos_atual].calcularPopularidade(casas)

                    #Verificar se o jogador passou pelo inicio
                    if pos_atual < pos_inicial:
                        partida.mensagem = ("Voce passou pelo inicio e recebeu R$ 200,00")
                        jogador.voltas =+ 1
                        jogador.adicionar_dinheiro(200)
                    #Possibilidade de compra
                    if propriedade.proprietario == None:
                        partida.mensagem += f"Esta propriedade ainda não foi adquirida por nenhum jogador. Gostaria de comprá-la?"
                        estado = 2
                    #Possibilidade de aumentar o nivel da propriedade
                    elif propriedade.proprietario == jogador:
                        partida.mensagem += "Essa propriedade já é sua. Deseja melhorá-la"
                        estado = 3 
                    #E agora ?
                    elif jogador.posicao % 9 == 4:
                        partida.mensagem += "E agora? Retire uma carta e descubra se hoje é seu dia de sorte."
                        estado = 4
                    #Nada a fazer
                    elif jogador.posicao == 0 or jogador.posicao == 9:
                        partida.mensagem += "Nada a fazer aqui."
                        estado = 5
                    #Férias, uma rodada sem jogar
                    elif jogador.posicao == 18:
                        partida.mensagem += ("Voce está de férias e ficará uma vez sem jogar!")
                        jogador.ferias = 1
                        estado = 6
                    #Vá para o congelamento
                    elif jogador.posicao == 27:
                        partida.mensagem += ("Vá para o congelamento sem receber nada!")
                        estado = 7
                    #Propriedade de outro jogador
                    else:
                        partida.mensagem += f"Essa propriedade pertence a {propriedade.proprietario.nome}"
                        estado = 8
            #Possibilidade de compra
            if estado == 2:
                if botao_comprar.handle_event(event):
                    if jogador.comprar_propriedade(propriedade):
                        partida.mensagem = (f"{jogador.nome} comprou {propriedade.titulo}")
                    else:
                        partida.mensagem = (f"Você não tem dinheiro suficiente")
                    estado = 9
                if botao_terminar.handle_event(event):
                    partida.jogada += 1
                    rodada = partida.jogada // 4
                    partida.mensagem = (f"Jogada: {partida.jogada} Rodada: {rodada}")
                    partida.jogador_Atual = partida.jogadores[partida.jogada % 4]
                    estado = 0
            #Possibilidade de aumentar o nivel da propriedade
            if estado == 3:
                if botao_melhorar.handle_event(event):
                    if propriedade.melhorar_propriedade():
                        partida.mensagem = (f"{propriedade.titulo} melhorada para o nivel {propriedade.nivel}")
                    else:
                        if(propriedade.nivel == 5):
                            partida.mensagem = f"{propriedade.titulo} já está no nivel máximo."
                        else:
                            partida.mensagem = (f"Você não tem dinheiro suficiente")
                    estado = 9
                if botao_terminar.handle_event(event):
                    partida.jogada += 1
                    rodada = partida.jogada // 4
                    partida.mensagem = (f"Jogada: {partida.jogada} Rodada: {rodada}")
                    partida.jogador_Atual = partida.jogadores[partida.jogada % 4]
                    estado = 0
            #E agora ?
            if estado == 4:
                if botao_pegar_carta.handle_event(event):
                    mensagem = propriedade.sorteio_eAgora(jogador)
                    partida.mensagem = (mensagem)
                    estado = 9
            #Nada a fazer
            if estado == 5:
                if botao_ok.handle_event(event):
                    estado = 9
            #Férias, uma rodada sem jogar
            if estado == 6:
                if botao_ok.handle_event(event):
                    estado = 9
            #Vá para o congelamento
            if estado == 7:
                if botao_ok.handle_event(event):
                    jogador.congelamento = 1
                    jogador.posicao = 9
                    estado = 9
            #Propriedade de outro jogador
            if estado == 8:
                if botao_pagar.handle_event(event):
                    if propriedade.proprietario.congelamento == 0:
                        jogador.pagar_aluguel(propriedade.proprietario, propriedade.valor_aluguel[propriedade.nivel - 1])
                        partida.mensagem = (f"Você pagou R$ {propriedade.valor_aluguel[propriedade.nivel - 1]},00 para {propriedade.proprietario.nome}")
                        estado = 9
                    else:
                        partida.mensagem = (f"{propriedade.proprietario.nome} está com os negócios congelados!")
                        partida.mensagem += "Você não precisará pagar nada!"
                        estado = 9
            #Terminar a vez
            if estado == 9:
                if botao_terminar.handle_event(event):
                    partida.jogada +=1
                    rodada = partida.jogada // 4
                    partida.mensagem = (f"Jogada: {partida.jogada} Rodada: {rodada}")
                    partida.jogador_Atual = partida.jogadores[partida.jogada % 4]
                    if rodada - 1 > 0 and (rodada - 1) % 4 == 0:
                        ranking = rankPopularidade(casas)
                        print("Rank de propriedades atualizado! " + str(rodada))

                    estado = 0
                
        # Preencher a tela com a cor branca
        screen.fill(white)
        #Calcular ranking de popularidade a cada 4 rodadas
        
        # Desenhar o tabuleiro
        desenhar_casas_tabuleiro()
        desenhar_dados(resultado)
        desenhar_pinos()
        desenhar_estatisticas_jogadores()
        #Verificar estado da jogada, jogar dados, mover, decidir, terminar
        desenhar_painel_jogo()
        exibir_info_posicao_atual()
        exibir_mensagem(partida.mensagem)
        exibir_informações()

        # Atualizar a tela
        pygame.display.update()
