import pygame
from pygame.sprite import Sprite


class Bala(Sprite):
    """ Uma classe que configura os projeteis disparados pelas naves """

    def __init__(self, ai_config, screen, nave):
        """ Cria um objeto para o projétil na posição inicial da espaçonave """
        super(Bala, self).__init__()
        self.screen = screen

        # Criando um projétil na posição (0,0)
        self.rect = pygame.Rect(0, 0, ai_config.bala_width,
                                ai_config.bala_height)
        self.rect.centerx = nave.rect.centerx
        self.rect.top = nave.rect.top

        # Armazena a posição do projétil em posição decimal:
        self.y = float(self.rect.y)

        self.color = ai_config.bala_bgcolor
        self.speed_factor = ai_config.bala_speed_factor

    def update(self):
        """ Move o projétil para cima na tela """
        # Atualiza a posição inicial do projétil:
        self.y -= self.speed_factor

        # Atualiza a posição do rect:
        self.rect.y = self.y

    def draw_bala(self):
        """ Desenha o projétil na tela """
        pygame.draw.rect(self.screen, self.color, self.rect)