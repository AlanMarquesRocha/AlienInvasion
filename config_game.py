import pygame, random


class Config_Game():
    """ Define as configurações básicas do jogo """

    def __init__(self):
        # Cria a cor do background de forma aleatória utilizando o sistema RGB de cores:
        self.c_1 = random.choice(range(0, 256))
        self.c_2 = random.choice(range(0, 256))
        self.c_3 = random.choice(range(0, 256))

        # Cria as cores das balas de forma aleatória utilizando o sistema RGB de cores:
        self.b_1 = random.choice(range(0, 256))
        self.b_2 = random.choice(range(0, 256))
        self.b_3 = random.choice(range(0, 256))

        # Recebe as variáveis geradas de forma aleatória para formar a cor de fundo em RGB
        self.bgcolor = (self.c_1, self.c_2, self.c_3)

        # Configurando o tamanho da tela em pixels
        self.screen_width = 700
        self.screen_height = 500

        # Configurando a velocidade da nave:
        self.nave_speed_factor = 1

        # Configura o número de vidas da nave humana:
        self.nave_limit = 3

        # Configuração de direção dos alienígenas:
        self.frota_dobra_velocidade = 30

        # Configura a velocidade do alienígena:
        self.alienigena_speed_factor = 0.3

        # direcao_tropa = 1 (tropa para a direita) / -1 (tropa para a esquerda):
        self.direcao_tropa = 1

        # Confugaração inicial das balas que serão disparadas pela nave
        self.bala_speed_factor = 0.75
        self.bala_width = 9
        self.bala_height = 25
        self.bala_bgcolor = (self.b_1, self.b_2, self.b_3)

        # Configura a quantidade de balas permitida por vez no jogo:
        self.qtd_balas = 3

        # Colocando um nome na barra inicial do jogo
        self.message = pygame.display.set_caption('Invasão Alienígena - Por: Alan M. Rocha')
