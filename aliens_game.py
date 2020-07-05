import pygame
from pygame.sprite import Sprite


class Alienigenas(Sprite):
    """ Classe que representa os alienígenas do game """
    def __init__(self, ai_config, screen):
        super(Alienigenas, self).__init__()
        self.screen = screen
        self.ai_config = ai_config

        # Carrega a imagem da nave alienígena:
        self.image = pygame.image.load('Images/alien_nave_min.bmp')
        self.rect = self.image.get_rect()

        # Informa a posição inicial da nave no canto superior esquerdo da screen:
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Armazenando a posição atual da nave alienígena:
        self.x = float(self.rect.x)

    def check_bordas(self):
        """ Verifica se a nave está na borda da tela e retorna True (se for verdade)"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """ Faz com que a frota de alienígenas se mova para a direta
        ou esquerda na screen """
        self.x += float(self.ai_config.alienigena_speed_factor *
                   self.ai_config.direcao_tropa)
        self.rect.x = self.x

    def blitme(self):
        """ Função que desenha a nave alienígena na posição inicial """
        self.screen.blit(self.image, self.rect)