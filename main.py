import pygame
from pygame.sprite import Group

# Instanciando a classe Config_Game do arquivo config_game:
from config_game import Config_Game

# Instanciando a classe Nave() do arquivo naves_game para importar a nave:
from naves_game import Nave

# Importando a classe EstatisticaGame() do módulo estatistica_game
from estatistica_game import EstatistsicaGame

# Instanciando o método check_events() que trata dos eventos do jogo:
import invasao_alien_functions_game as func_game


# DAR CONTINUIDADE AO DESENVOLVIMENTO DO JOGO A PARTIR DA PÁGINA 412 DO LIVRO.


def run_game():
    """ Inicializa o jogo criando uma tela pré-definida, nave, balas e alienígenas """
    pygame.init()

    # Instanciando a classe Config_Game para receber as informações de configuração do game.
    ai_config = Config_Game()
    screen = pygame.display.set_mode((
        ai_config.screen_width, ai_config.screen_height))

    # Mostra a mensagem na barra da tela através da classe Config_Game do módulo config_game.py
    ai_config.message

    # Cria uma nave para mostrar na tela através da classe Nave() no módulo naves_game.py:
    nave = Nave(ai_config, screen)

    # Cria um grupo no qual serão armazenados as balas e alienígenas:
    balas = Group()
    aliens = Group()

    # Cria uma instancia para armazenar as estatísticas do game
    estatistica = EstatistsicaGame(ai_config)

    # Cria a frota de alienígenas:
    func_game.cria_frota(ai_config, screen, nave, aliens)

    # Inicializa o laço principal do game:
    while True:
        # if pygame.mixer.get_busy() is not None:
        # Recebe informações do teclado e do mouse através do método check_events.
        if estatistica.ai_config:
            func_game.check_events(ai_config, screen, nave, balas)
            nave.update()
            balas.update()
            func_game.update_balas(ai_config, screen, nave, aliens, balas)
            func_game.update_aliens(ai_config, estatistica, screen, nave, aliens, balas)
            func_game.update_screen(ai_config, screen, nave, aliens, balas)


# Faz o jogo iniciar chamando o método run_game():
run_game()
