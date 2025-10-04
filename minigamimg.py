import pygame, sys, random
# pip install pygame

#inicializacao do jogo
pygame.init()

#criando tela do jogo (x,y)
screen = pygame.display.set_mode((800, 600))

#carregar imagem
player_img = pygame.image.load('dog.jpg')

food_img = pygame.image.load("dogfood.jpg")
food_img = pygame.transform.scale(food_img, (50,20))

#posicao inicial da bolinha
x = 200
y = 150
tamanho = 40
velocidade = 10

#posicao aleatoria da comida
food_x = random.randint(20, 380) # meu limite é 400
food_y = random.randint(20, 280) # meu limite é 300

while True:
    # verificar todos os eventos
    for event in pygame.event.get():
        ## o jogador clicou no x da guia e saiu do jogo
        if event.type == pygame.QUIT:
            sys.exit()

    # pegar teclas do jogador
    keys = pygame.key.get_pressed()

    # andar para a esquerda
    if keys[pygame.K_LEFT]:
        x -= 0.2

    # andar para a direita
    if keys[pygame.K_RIGHT]:
        x += 0.2

    # andar para a cima
    if keys[pygame.K_UP]:
        y -= 0.2

    # andar para a cima
    if keys[pygame.K_DOWN]:
        y += 0.2
    
    # se x for menor que zero, colocamos do tamanho da bolinha
    if x < 0: 
        x = 0

      # se x for maior que 400, colocamos do tamanho da bolinha
    if x > 400 - tamanho:
        x = 400 - tamanho

    # se y for menor que zero, colocamos do tamanho da bolinha
    if y < 0:
        y = 0
    
    # se y for menor que 300, colocamos do tamanho da bolinha
    if y > 300 - tamanho:
        y = 300 - tamanho

    centro_player_x = x + tamanho / 2
    centro_player_y = y + tamanho / 2

    centro_food_x = food_x + 10
    centro_food_y = food_y + 10

    diferenca_x = centro_player_x - centro_food_x
    diferenca_y = centro_player_y - centro_food_y

    quadrado_x = diferenca_x ** 2
    quadrado_y = diferenca_y ** 2

    #soma dos quadrados
    soma_quadrados = quadrado_x + quadrado_y
    #raiz da soma dos quadrados
    distancia = soma_quadrados ** 0.5


    if distancia < (tamanho / 2 + 10): # se encostar (o raio 10 é o tamanho da bolinha amarela)
        tamanho += 3 #aumenta a bolinha vermelha

        #reposiciona a comida
        food_x = random.randint(20, 380)
        food_y = random.randint(20, 280)

    # redimensionar a imagem do jogador 
    player_scalled = pygame.transform.scale(player_img, (tamanho, tamanho))

    #pintar o fundo do jogo, RGB (0, 0, 0)
    screen.fill((0, 0, 0))
    screen.blit(food_img, (food_x, food_y))
    screen.blit(player_scalled,(x, y))

    #desenhar um circulo vermelho, RGB(255, 0, 0)
    # Cor RGB, Posicao X e Y, com raio 20
    # pygame.draw.circle(screen, (255, 0, 0), (x, y), tamanho)

    # Bolinha amarela (comida)
    # pygame.draw.circle(screen, (255,255,0), (food_x, food_y), 10)

    # para trocar o frame do jogo
    pygame.display.flip()

