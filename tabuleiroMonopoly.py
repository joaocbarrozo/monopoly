import pygame
import sys
import classesMonopoly

# Inicializar o Pygame
pygame.init()

# Obter informações sobre a tela
screen_info = pygame.display.Info()

# Definir as dimensões da tela com base na resolução do sistema
screen_width = int(screen_info.current_w * 0.95)
screen_height = min(int(screen_info.current_h * 0.9),int(screen_width / 1.8))
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
    classesMonopoly.Propriedade(yellow, black, "Posto de Gasolina", "5", 1, None, 350, [150, 200, 250, 300, 350]),
    classesMonopoly.Propriedade(yellow, black, "Padaria", "6", 1, None, 250, [150, 200, 250, 300, 350]),
    classesMonopoly.Propriedade(yellow, black, "Livraria", "7", 1, None, 100, [150, 200, 250, 300, 350]),
    classesMonopoly.Propriedade(yellow, black, "Loja de Roupas", "8", 1, None, 150, [150, 200, 250, 300, 350]),
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
    classesMonopoly.Propriedade(yellow, black, "Vá para o Congelamento", "27", 1, "Banco", 0, [150, 200, 250, 300, 350], "Vá para a prisão!"),
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
    #inicio_img = pygame.transform.scale(inicio_img, (square_size - 8, square_size - 8))
    inicio_pos = (casas[0].posicao_x + 4, casas[0].posicao_y + 4)
    inicio = (inicio_img, inicio_pos)
    imagens.append(inicio)
    farmacia_img = pygame.image.load("./imagens/farmacia.png")
    #farmacia_img = pygame.transform.scale(farmacia_img, (square_size - 8, square_size - 8))
    farmacia_pos = (casas[1].posicao_x + 4, casas[1].posicao_y + 4)
    farmacia = (farmacia_img, farmacia_pos)
    imagens.append(farmacia)
    restaurante_img = pygame.image.load("./imagens/restaurante.png")
    #restaurante_img = pygame.transform.scale(restaurante_img, (square_size - 8, square_size - 8))
    restaurante_pos = (casas[2].posicao_x + 4, casas[2].posicao_y + 4)
    restaurante = (restaurante_img, restaurante_pos)
    imagens.append(restaurante)
    supermercado_img = pygame.image.load("./imagens/supermercado.png")
    #supermercado_img = pygame.transform.scale(supermercado_img, (square_size - 8, square_size - 8))
    supermercado_pos = (casas[3].posicao_x + 4, casas[3].posicao_y + 4)
    supermercado = (supermercado_img, supermercado_pos)
    imagens.append(supermercado)
    e_agora_img = pygame.image.load("./imagens/e_agora.png")
    #e_agora_img = pygame.transform.scale(e_agora_img, (square_size - 8, square_size - 8))
    e_agora_pos = (casas[4].posicao_x + 4, casas[4].posicao_y + 4)
    e_agora = (e_agora_img, e_agora_pos)
    imagens.append(e_agora)
    p_gasolina_img = pygame.image.load("./imagens/p_gasolina.png")
    #p_gasolina_img = pygame.transform.scale(p_gasolina_img, (square_size - 8, square_size - 8))
    p_gasolina_pos = (casas[5].posicao_x + 4, casas[5].posicao_y + 4)
    p_gasolina = (p_gasolina_img, p_gasolina_pos)
    imagens.append(p_gasolina)
    padaria_img = pygame.image.load("./imagens/padaria.png")
    #padaria_img = pygame.transform.scale(padaria_img, (square_size - 8, square_size - 8))
    padaria_pos = (casas[6].posicao_x + 4, casas[6].posicao_y + 4)
    padaria = (padaria_img, padaria_pos)
    imagens.append(padaria)
    livraria_img = pygame.image.load("./imagens/livraria.png")
    #livraria_img = pygame.transform.scale(livraria_img, (square_size - 8, square_size - 8))
    livraria_pos = (casas[7].posicao_x + 4, casas[7].posicao_y + 4)
    livraria = (livraria_img, livraria_pos)
    imagens.append(livraria)
    loja_roupas_img = pygame.image.load("./imagens/loja_roupas.png")
    #loja_roupas_img = pygame.transform.scale(loja_roupas_img, (square_size - 8, square_size - 8))
    loja_roupas_pos = (casas[8].posicao_x + 4, casas[8].posicao_y + 4)
    loja_roupas = (loja_roupas_img, loja_roupas_pos)
    imagens.append(loja_roupas)
    congelamento_img = pygame.image.load("./imagens/congelamento.png")
    #congelamento_img = pygame.transform.scale(congelamento_img, (square_size - 8, square_size - 8))
    congelamento_pos = (casas[9].posicao_x + 4, casas[9].posicao_y + 4)
    congelamento = (congelamento_img, congelamento_pos)
    imagens.append(congelamento)
    barbearia_img = pygame.image.load("./imagens/barbearia.png")
    #barbearia_img = pygame.transform.scale(barbearia_img, (square_size - 8, square_size - 8))
    barbearia_pos = (casas[10].posicao_x + 4, casas[10].posicao_y + 4)
    barbearia = (barbearia_img, barbearia_pos)
    imagens.append(barbearia)
    academia_img = pygame.image.load("./imagens/academia.png")
    #academia_img = pygame.transform.scale(academia_img, (square_size - 8, square_size - 8))
    academia_pos = (casas[11].posicao_x + 4, casas[11].posicao_y + 4)
    academia = (academia_img, academia_pos)
    imagens.append(academia)
    sorveteria_img = pygame.image.load("./imagens/sorveteria.png")
    #sorveteria_img = pygame.transform.scale(sorveteria_img, (square_size - 8, square_size - 8))
    sorveteria_pos = (casas[12].posicao_x + 4, casas[12].posicao_y + 4)
    sorveteria = (sorveteria_img, sorveteria_pos)
    imagens.append(sorveteria)
    e_agora_2_img = pygame.image.load("./imagens/e_agora.png")
    #e_agora_2_img = pygame.transform.scale(e_agora_2_img, (square_size - 8, square_size - 8))
    e_agora_2_pos = (casas[13].posicao_x + 4, casas[13].posicao_y + 4)
    e_agora_2 = (e_agora_2_img, e_agora_2_pos)
    imagens.append(e_agora_2)
    cafeteria_img = pygame.image.load("./imagens/cafeteria.png")
    #cafeteria_img = pygame.transform.scale(cafeteria_img, (square_size - 8, square_size - 8))
    cafeteria_pos = (casas[14].posicao_x + 4, casas[14].posicao_y + 4)
    cafeteria = (cafeteria_img, cafeteria_pos)
    imagens.append(cafeteria)
    cinema_img = pygame.image.load("./imagens/cinema.png")
    #cinema_img = pygame.transform.scale(cinema_img, (square_size - 8, square_size - 8))
    cinema_pos = (casas[15].posicao_x + 4, casas[15].posicao_y + 4)
    cinema = (cinema_img, cinema_pos)
    imagens.append(cinema)
    teatro_img = pygame.image.load("./imagens/teatro.png")
    #teatro_img = pygame.transform.scale(teatro_img, (square_size - 8, square_size - 8))
    teatro_pos = (casas[16].posicao_x + 4, casas[16].posicao_y + 4)
    teatro = (teatro_img, teatro_pos)
    imagens.append(teatro)
    floricultura_img = pygame.image.load("./imagens/floricultura.jpeg")
    #floricultura_img = pygame.transform.scale(floricultura_img, (square_size - 8, square_size - 8))
    floricultura_pos = (casas[17].posicao_x + 4, casas[17].posicao_y + 4)
    floricultura = (floricultura_img, floricultura_pos)
    imagens.append(floricultura)
    ferias_img = pygame.image.load("./imagens/ferias.jpeg")
    #ferias_img = pygame.transform.scale(ferias_img, (square_size - 8, square_size - 8))
    ferias_pos = (casas[18].posicao_x + 4, casas[18].posicao_y + 4)
    ferias = (ferias_img, ferias_pos)
    imagens.append(ferias)
    banco_img = pygame.image.load("./imagens/banco.png")
    #banco_img = pygame.transform.scale(banco_img, (square_size - 8, square_size - 8))
    banco_pos = (casas[19].posicao_x + 4, casas[19].posicao_y + 4)
    banco = (banco_img, banco_pos)
    imagens.append(banco)
    papelaria_img = pygame.image.load("./imagens/papelaria.png")
    #papelaria_img = pygame.transform.scale(papelaria_img, (square_size - 8, square_size - 8))
    papelaria_pos = (casas[20].posicao_x + 4, casas[20].posicao_y + 4)
    papelaria = (papelaria_img, papelaria_pos)
    imagens.append(papelaria)
    clinica_medica_img = pygame.image.load("./imagens/clinica_medica.png")
    #clinica_medica_img = pygame.transform.scale(clinica_medica_img, (square_size - 8, square_size - 8))
    clinica_medica_pos = (casas[21].posicao_x + 4, casas[21].posicao_y + 4)
    clinica_medica = (clinica_medica_img, clinica_medica_pos)
    imagens.append(clinica_medica)
    e_agora_3_img = pygame.image.load("./imagens/e_agora.png")
    #e_agora_3_img = pygame.transform.scale(e_agora_3_img, (square_size - 8, square_size - 8))
    e_agora_3_pos = (casas[22].posicao_x + 4, casas[22].posicao_y + 4)
    e_agora_3 = (e_agora_3_img, e_agora_3_pos)
    imagens.append(e_agora_3)
    pet_shop_img = pygame.image.load("./imagens/pet_shop.png")
    #pet_shop_img = pygame.transform.scale(pet_shop_img, (square_size - 8, square_size - 8))
    pet_shop_pos = (casas[23].posicao_x + 4, casas[23].posicao_y + 4)
    pet_shop = (pet_shop_img, pet_shop_pos)
    imagens.append(pet_shop)
    loja_cosmeticos_img = pygame.image.load("./imagens/loja_cosmeticos.png")
    #loja_cosmeticos_img = pygame.transform.scale(loja_cosmeticos_img, (square_size - 8, square_size - 8))
    loja_cosmeticos_pos = (casas[24].posicao_x + 4, casas[24].posicao_y + 4)
    loja_cosmeticos = (loja_cosmeticos_img, loja_cosmeticos_pos)
    imagens.append(loja_cosmeticos)
    loja_brinquedos_img = pygame.image.load("./imagens/loja_brinquedos.png")
    #loja_brinquedos_img = pygame.transform.scale(loja_brinquedos_img, (square_size - 8, square_size - 8))
    loja_brinquedos_pos = (casas[25].posicao_x + 4, casas[25].posicao_y + 4)
    loja_brinquedos = (loja_brinquedos_img, loja_brinquedos_pos)
    imagens.append(loja_brinquedos)
    oficina_mecanica_img = pygame.image.load("./imagens/oficina_mecanica.png")
    #oficina_mecanica_img = pygame.transform.scale(oficina_mecanica_img, (square_size - 8, square_size - 8))
    oficina_mecanica_pos = (casas[26].posicao_x + 4, casas[26].posicao_y + 4)
    oficina_mecanica = (oficina_mecanica_img, oficina_mecanica_pos)
    imagens.append(oficina_mecanica)
    va_congelameto_img = pygame.image.load("./imagens/va_congelamento.png")
    #va_congelameto_img = pygame.transform.scale(va_congelameto_img, (square_size - 8, square_size - 8))
    va_congelameto_pos = (casas[27].posicao_x + 4, casas[27].posicao_y + 4)
    va_congelameto = (va_congelameto_img, va_congelameto_pos)
    imagens.append(va_congelameto)
    açougue_img = pygame.image.load("./imagens/açougue.png")
    #açougue_img = pygame.transform.scale(açougue_img, (square_size - 8, square_size - 8))
    açougue_pos = (casas[28].posicao_x + 4, casas[28].posicao_y + 4)
    açougue = (açougue_img, açougue_pos)
    imagens.append(açougue)
    hamburgueria_img = pygame.image.load("./imagens/hamburgueria.jpeg")
    #hamburgueria_img = pygame.transform.scale(hamburgueria_img, (square_size - 8, square_size - 8))
    hamburgueria_pos = (casas[29].posicao_x + 4, casas[29].posicao_y + 4)
    hamburgueria = (hamburgueria_img, hamburgueria_pos)
    imagens.append(hamburgueria)
    loja_carros_img = pygame.image.load("./imagens/loja_carros.png")
    #loja_carros_img = pygame.transform.scale(loja_carros_img, (square_size - 8, square_size - 8))
    loja_carros_pos = (casas[30].posicao_x + 4, casas[30].posicao_y + 4)
    loja_carros = (loja_carros_img, loja_carros_pos)
    imagens.append(loja_carros)
    e_agora_4_img = pygame.image.load("./imagens/e_agora.png")
    #e_agora_4_img = pygame.transform.scale(e_agora_4_img, (square_size - 8, square_size - 8))
    e_agora_4_pos = (casas[31].posicao_x + 4, casas[31].posicao_y + 4)
    e_agora_4 = (e_agora_4_img, e_agora_4_pos)
    imagens.append(e_agora_4)
    loja_esportes_img = pygame.image.load("./imagens/loja_esportes.jpeg")
    #loja_esportes_img = pygame.transform.scale(loja_esportes_img, (square_size - 8, square_size - 8))
    loja_esportes_pos = (casas[32].posicao_x + 4, casas[32].posicao_y + 4)
    loja_esportes = (loja_esportes_img, loja_esportes_pos)
    imagens.append(loja_esportes)
    pizzaria_img = pygame.image.load("./imagens/pizzaria.png")
    #pizzaria_img = pygame.transform.scale(pizzaria_img, (square_size - 8, square_size - 8))
    pizzaria_pos = (casas[33].posicao_x + 4, casas[33].posicao_y + 4)
    pizzaria = (pizzaria_img, pizzaria_pos)
    imagens.append(pizzaria)
    hortifruti_img = pygame.image.load("./imagens/hortifruti.jpeg")
    #hortifruti_img = pygame.transform.scale(hortifruti_img, (square_size - 8, square_size - 8))
    hortifruti_pos = (casas[34].posicao_x + 4, casas[34].posicao_y + 4)
    hortifruti = (hortifruti_img, hortifruti_pos)
    imagens.append(hortifruti)
    loja_informatica_img = pygame.image.load("./imagens/loja_informatica.jpeg")
    #loja_informatica_img = pygame.transform.scale(loja_informatica_img, (square_size - 8, square_size - 8))
    loja_informatica_pos = (casas[35].posicao_x + 4, casas[35].posicao_y + 4)
    loja_informatica = (loja_informatica_img, loja_informatica_pos)
    imagens.append(loja_informatica)

    return imagens