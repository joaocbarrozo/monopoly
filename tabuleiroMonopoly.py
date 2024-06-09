import pygame
import sys
import classesMonopoly

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



#Criar propriedades e outras casas do tabuleiro
propriedades = [
    classesMonopoly.Propriedade(yellow, black, "Inicio", "0", 1, "Banco", 150, [150, 200, 250, 300, 350], "Inicio do jogo"),
    classesMonopoly.Propriedade(yellow, black, "Farmácia", "1", 1, None, 200, [150, 200, 250, 300, 350]),
    classesMonopoly.Propriedade(yellow, black, "Restaurante", "2", 1, None, 300, [150, 200, 250, 300, 350]),
    classesMonopoly.Propriedade(yellow, black, "Supermercado", "3", 1, None, 200, [150, 200, 250, 300, 350]),
    classesMonopoly.Propriedade(gray, black, "E Agora?", "4", 1, "Banco", 0, [150, 200, 250, 300, 350], "Tire uma carta será que hoje é seu dia de sorte?"),
    classesMonopoly.Propriedade(yellow, black, "P. Gasolina", "5", 1, None, 350, [150, 200, 250, 300, 350]),
    classesMonopoly.Propriedade(yellow, black, "Padaria", "6", 1, None, 250, [150, 200, 250, 300, 350]),
    classesMonopoly.Propriedade(yellow, black, "Livraria", "7", 1, None, 100, [150, 200, 250, 300, 350]),
    classesMonopoly.Propriedade(yellow, black, "L. de Roupas", "8", 1, None, 150, [150, 200, 250, 300, 350]),
    classesMonopoly.Propriedade(yellow, black, "Congelamento", "9", 1, "Banco", 0, [150, 200, 250, 300, 350], "Você está apenas fazendo uma visita."),
    classesMonopoly.Propriedade(yellow, black, "Barbearia", "10", 1, None, 150, [150, 200, 250, 300, 350]),
    classesMonopoly.Propriedade(yellow, black, "Academia", "11", 1, None, 200, [150, 200, 250, 300, 350]),
    classesMonopoly.Propriedade(yellow, black, "Sorveteria", "12", 1, None, 100, [150, 200, 250, 300, 350]),
    classesMonopoly.Propriedade(gray, black, "E Agora?", "13", 1, "Banco", 0, [150, 200, 250, 300, 350], "Tire uma carta será que hoje é seu dia de sorte?"),
    classesMonopoly.Propriedade(yellow, black, "Cafeteria", "14", 1, None, 150, [150, 200, 250, 300, 350]),
    classesMonopoly.Propriedade(yellow, black, "Cinema", "15", 1, None, 200, [150, 200, 250, 300, 350]),
    classesMonopoly.Propriedade(yellow, black, "Teatro", "16", 1, None, 150, [150, 200, 250, 300, 350]),
    classesMonopoly.Propriedade(yellow, black, "Floricultura", "17", 1, None, 100, [150, 200, 250, 300, 350]),
    classesMonopoly.Propriedade(yellow, black, "Férias", "18", 1, "Banco", 0, [150, 200, 250, 300, 350], "VocÊ está de ferias, fique uma vez sem jogar"),
    classesMonopoly.Propriedade(yellow, black, "Banco", "19", 1, None, 150, [150, 200, 250, 300, 350]),
    classesMonopoly.Propriedade(yellow, black, "Papelaria", "20", 1, None, 100, [150, 200, 250, 300, 350]),
    classesMonopoly.Propriedade(yellow, black, "Clínica Médica", "21", 1, None, 300, [150, 200, 250, 300, 350]),
    classesMonopoly.Propriedade(gray, black, "E Agora?", "22", 1, "Banco", 0, [150, 200, 250, 300, 350], "Tire uma carta será que hoje é seu dia de sorte?"),
    classesMonopoly.Propriedade(yellow, black, "Pet Shop", "23", 1, None, 200, [150, 200, 250, 300, 350]),
    classesMonopoly.Propriedade(yellow, black, "Loja de cosmeticos", "24", 1, None, 200, [150, 200, 250, 300, 350]),
    classesMonopoly.Propriedade(yellow, black, "Loja de brinquedos", "25", 1, None, 150, [150, 200, 250, 300, 350]),
    classesMonopoly.Propriedade(yellow, black, "Oficina Mecânica", "26", 1, None, 100, [150, 200, 250, 300, 350]),
    classesMonopoly.Propriedade(yellow, black, "Vá p/ Congelamento", "27", 1, "Banco", 0, [150, 200, 250, 300, 350], "Vá para a prisão!"),
    classesMonopoly.Propriedade(yellow, black, "Açougue", "28", 1, None, 300, [150, 200, 250, 300, 350]),
    classesMonopoly.Propriedade(yellow, black, "Hamburgueria", "29", 1, None, 250, [150, 200, 250, 300, 350]),
    classesMonopoly.Propriedade(yellow, black, "Auto Shopping", "30", 1, None, 200, [150, 200, 250, 300, 350]),
    classesMonopoly.Propriedade(gray, black, "E Agora?", "31", 1, "Banco", 0, [150, 200, 250, 300, 350], "Tire uma carta será que hoje é seu dia de sorte?"),
    classesMonopoly.Propriedade(yellow, black, "Loja de Esportes", "32", 1, None, 300, [150, 200, 250, 300, 350]),
    classesMonopoly.Propriedade(yellow, black, "Pizzaria", "33", 1, None, 150, [150, 200, 250, 300, 350]),
    classesMonopoly.Propriedade(yellow, black, "Hortifruti", "34", 1, None, 400, [150, 200, 250, 300, 350]),
    classesMonopoly.Propriedade(yellow, black, "Loja de Informática", "35", 1, None, 350, [150, 200, 250, 300, 350])
]


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

def carregar_imagens():
    imagens = []
    #Imagens das casas
    inicio_img = pygame.image.load("./imagens/inicio.png")
    inicio_img = pygame.transform.scale(inicio_img, (square_size - 8, square_size - 8))
    inicio_pos = (casas[0].posicao_x + 4, casas[0].posicao_y + 4)
    inicio = (inicio_img, inicio_pos)
    imagens.append(inicio)
    farmacia_img = pygame.image.load("./imagens/farmacia.png")
    farmacia_img = pygame.transform.scale(farmacia_img, (square_size - 8, square_size - 8))
    farmacia_pos = (casas[1].posicao_x + 4, casas[1].posicao_y + 4)
    farmacia = (farmacia_img, farmacia_pos)
    imagens.append(farmacia)
    restaurante_img = pygame.image.load("./imagens/restaurante.png")
    restaurante_img = pygame.transform.scale(restaurante_img, (square_size - 8, square_size - 8))
    restaurante_pos = (casas[2].posicao_x + 4, casas[2].posicao_y + 4)
    restaurante = (restaurante_img, restaurante_pos)
    imagens.append(restaurante)
    supermercado_img = pygame.image.load("./imagens/supermercado.png")
    supermercado_img = pygame.transform.scale(supermercado_img, (square_size - 8, square_size - 8))
    supermercado_pos = (casas[3].posicao_x + 4, casas[3].posicao_y + 4)
    supermercado = (supermercado_img, supermercado_pos)
    imagens.append(supermercado)
    e_agora_img = pygame.image.load("./imagens/e_agora.png")
    e_agora_img = pygame.transform.scale(e_agora_img, (square_size - 8, square_size - 8))
    e_agora_pos = (casas[4].posicao_x + 4, casas[4].posicao_y + 4)
    e_agora = (e_agora_img, e_agora_pos)
    imagens.append(e_agora)
    p_gasolina_img = pygame.image.load("./imagens/p_gasolina.png")
    p_gasolina_img = pygame.transform.scale(p_gasolina_img, (square_size - 8, square_size - 8))
    p_gasolina_pos = (casas[5].posicao_x + 4, casas[5].posicao_y + 4)
    p_gasolina = (p_gasolina_img, p_gasolina_pos)
    imagens.append(p_gasolina)
    padaria_img = pygame.image.load("./imagens/padaria.png")
    padaria_img = pygame.transform.scale(padaria_img, (square_size - 8, square_size - 8))
    padaria_pos = (casas[6].posicao_x + 4, casas[6].posicao_y + 4)
    padaria = (padaria_img, padaria_pos)
    imagens.append(padaria)
    livraria_img = pygame.image.load("./imagens/livraria.png")
    livraria_img = pygame.transform.scale(livraria_img, (square_size - 8, square_size - 8))
    livraria_pos = (casas[7].posicao_x + 4, casas[7].posicao_y + 4)
    livraria = (livraria_img, livraria_pos)
    imagens.append(livraria)
    loja_roupas_img = pygame.image.load("./imagens/loja_roupas.png")
    loja_roupas_img = pygame.transform.scale(loja_roupas_img, (square_size - 8, square_size - 8))
    loja_roupas_pos = (casas[8].posicao_x + 4, casas[8].posicao_y + 4)
    loja_roupas = (loja_roupas_img, loja_roupas_pos)
    imagens.append(loja_roupas)
    congelamento_img = pygame.image.load("./imagens/congelamento.png")
    congelamento_img = pygame.transform.scale(congelamento_img, (square_size - 8, square_size - 8))
    congelamento_pos = (casas[9].posicao_x + 4, casas[9].posicao_y + 4)
    congelamento = (congelamento_img, congelamento_pos)
    imagens.append(congelamento)
    barbearia_img = pygame.image.load("./imagens/barbearia.png")
    barbearia_img = pygame.transform.scale(barbearia_img, (square_size - 8, square_size - 8))
    barbearia_pos = (casas[10].posicao_x + 4, casas[10].posicao_y + 4)
    barbearia = (barbearia_img, barbearia_pos)
    imagens.append(barbearia)
    academia_img = pygame.image.load("./imagens/academia.png")
    academia_img = pygame.transform.scale(academia_img, (square_size - 8, square_size - 8))
    academia_pos = (casas[11].posicao_x + 4, casas[11].posicao_y + 4)
    academia = (academia_img, academia_pos)
    imagens.append(academia)
    sorveteria_img = pygame.image.load("./imagens/sorveteria.png")
    sorveteria_img = pygame.transform.scale(sorveteria_img, (square_size - 8, square_size - 8))
    sorveteria_pos = (casas[12].posicao_x + 4, casas[12].posicao_y + 4)
    sorveteria = (sorveteria_img, sorveteria_pos)
    imagens.append(sorveteria)
    e_agora_2_img = pygame.image.load("./imagens/e_agora.png")
    e_agora_2_img = pygame.transform.scale(e_agora_2_img, (square_size - 8, square_size - 8))
    e_agora_2_pos = (casas[13].posicao_x + 4, casas[13].posicao_y + 4)
    e_agora_2 = (e_agora_2_img, e_agora_2_pos)
    imagens.append(e_agora_2)
    cafeteria_img = pygame.image.load("./imagens/cafeteria.png")
    cafeteria_img = pygame.transform.scale(cafeteria_img, (square_size - 8, square_size - 8))
    cafeteria_pos = (casas[14].posicao_x + 4, casas[14].posicao_y + 4)
    cafeteria = (cafeteria_img, cafeteria_pos)
    imagens.append(cafeteria)
    cinema_img = pygame.image.load("./imagens/cinema.png")
    cinema_img = pygame.transform.scale(cinema_img, (square_size - 8, square_size - 8))
    cinema_pos = (casas[15].posicao_x + 4, casas[15].posicao_y + 4)
    cinema = (cinema_img, cinema_pos)
    imagens.append(cinema)
    teatro_img = pygame.image.load("./imagens/teatro.png")
    teatro_img = pygame.transform.scale(teatro_img, (square_size - 8, square_size - 8))
    teatro_pos = (casas[16].posicao_x + 4, casas[16].posicao_y + 4)
    teatro = (teatro_img, teatro_pos)
    imagens.append(teatro)
    floricultura_img = pygame.image.load("./imagens/floricultura.jpeg")
    floricultura_img = pygame.transform.scale(floricultura_img, (square_size - 8, square_size - 8))
    floricultura_pos = (casas[17].posicao_x + 4, casas[17].posicao_y + 4)
    floricultura = (floricultura_img, floricultura_pos)
    imagens.append(floricultura)
    ferias_img = pygame.image.load("./imagens/ferias.jpeg")
    ferias_img = pygame.transform.scale(ferias_img, (square_size - 8, square_size - 8))
    ferias_pos = (casas[18].posicao_x + 4, casas[18].posicao_y + 4)
    ferias = (ferias_img, ferias_pos)
    imagens.append(ferias)
    #ferias
    #banco
    #papelaria
    #clinica mediaca
    #e agora
    #pet shop
    #cosmeticos
    #brinquedos
    #mecanica
    #V p congelamento
    #acougue
    #hamburgueria
    #auto shopping
    #e agora
    #esportes
    #pizzaria
    #hortifrut
    #informatica
    
    
    return imagens