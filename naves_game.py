import pygame


# Criando a classe de configurações das naves
class Nave:
    """ Mostra a posição inicial da espaçonave """

    def __init__(self, ai_config, screen):
        self.screen = screen

        self.ai_config = ai_config

        # Carrega a imagem da nave tripulada pelos humanos
        self.image = pygame.image.load('Images/human_nave_.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Configura a posição inicial da espaço nave (Centro inferior da screen):
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Armazena um valor decimal para o centro da nave:
        self.center = float(self.rect.centerx)

        # Flag do movimento contínuo para a direita
        self.moving_right = False

        # Flag do movimento contínuo para a esquerda
        self.moving_left = False

        # Flag do movimento contínuo para cima
        self.moving_up = True

        # Flag do movimento contínuo para baixo
        self.moving_down = True

    def update(self):
        """ Faz a atualização da posição da espaçonave de acordo
        com a flag de movimento """

        # Atualiza o valor do centro da nave para não ultrapassar a tela pelo lado direito:
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_config.nave_speed_factor

        # Atualiza o valor do centro da nave para não ultrapassar a tela pelo lado esquerdo:
        if self.moving_left and self.rect.left > 0:
             self.center -= self.ai_config.nave_speed_factor

        # Atualiza o objeto rect de acordo com self.centerx:
        self.rect.centerx = self.center

        # Atualiza o valor do centro da nave para não ultrapassar a tela por baixo:
        if self.rect.centery < 455:
            if self.moving_up:
                self.rect.centery += 1

        # Atualiza o valor do centro da nave para não ultrapassar a tela por cima:
        if self.moving_down and self.rect.centery > 0:
            if self.moving_down:
                self.rect.centery -= 1

    def blitme(self):
        """ Desenha a espaçonave na posição atual """
        self.screen.blit(self.image, self.rect)

    def center_nave(self):
        """ Centraliza a nave na tela """
        self.center = self.screen_rect.centerx