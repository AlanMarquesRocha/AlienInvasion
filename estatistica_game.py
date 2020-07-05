
class EstatistsicaGame():
    """ Classe que irá armazenar as estatísticas do game """
    def __init__(self, ai_config):
        """ Inicializa os dados estatísticos """
        self.ai_config = ai_config
        self.reset_estatistica()
        self.game_ativo = True

    def reset_estatistica(self):
        """ Armazena os dados estatísticos que podem mudar durante o game """
        self.nave_left = self.ai_config.nave_limit