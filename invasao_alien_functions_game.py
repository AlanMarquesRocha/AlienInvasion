import pygame, sys
from config_balas import Bala
from aliens_game import Alienigenas
from time import sleep


def nave_hit(ai_config, estatistica, screen, nave, aliens, balas):
    """ Rpresenta as ações que ocorrem quando a nave colide com a frota """

    if estatistica.nave_left > 0:
        # Diminui a quantidade de vidas da nave após a colisão:
        estatistica.nave_left -= 1

        # Esvazia a lista de balas e naves alienigenas:
        aliens.empty()
        balas.empty()

        # Recria a frota de alienígenas e centraliza a nave no centro inferior da screen:
        cria_frota(ai_config, screen, nave, aliens)
        nave.center_nave()

        # Faz uma pequena pausa de 1.0 s
        sleep(1.0)

    else:
        estatistica.game_ativo = False
        sys.exit()


def check_events_keydown(event, ai_config, screen, nave, balas):
    """ Trata os eventos no jogo quando as teclas são pressionadas """
    # Move a nave para a direita enquanto a tecla 'D' estiver pressinada:
    if event.key == pygame.K_d:
        nave.moving_right = True

        # Atira um projétil quando a tecla 'F' é pressionada:
    elif event.key == pygame.K_f:

        # Verifica se a qtd. de balas é menor do que a permitida:
        if len(balas) < ai_config.qtd_balas:
            # Cria um novo projétil e adiciona no Grupo de balas:
            new_bala = Bala(ai_config, screen, nave)
            balas.add(new_bala)

    # Move a nave para a esqueda enquanto a tecla 'A' estiver pressionada:
    elif event.key == pygame.K_a:
        nave.moving_left = True

    # Move a nave para cima enquanto a tecla 'W' estiver pressionada:
    elif event.key == pygame.K_w:
        nave.moving_up = False

    # Move a nave para baixo enquanto a tecla 'S' estiver pressionada:
    elif event.key == pygame.K_s:
        nave.moving_down = False

    # Finaliza o jogo se o usuário apertar a tecla 'Q':
    elif event.key == pygame.K_q:
        sys.exit()


def check_events_keyup(event, nave):
    """ Trata os eventos do jogo quando os botões param de ser pressionados """

    # Faz a nave parar de se mover para a direita quando a tecla 'D' deixa de ser pressionada:
    if event.key == pygame.K_d:
        nave.moving_right = False

    # Faz a nave parar de se mover para a esquerda quando a tecla 'A' deixa de ser pressionada:
    elif event.key == pygame.K_a:
        nave.moving_left = False

    # Faz a nave parar de se mover para cima quando a tecla 'W' deixa de ser pressionada:
    elif event.key == pygame.K_w:
        nave.moving_up = True

    # Faz a nave parar de se mover para baixo quando a tecla 'S' deixa de ser pressionada:
    elif event.key == pygame.K_s:
        nave.moving_down = True


def check_events(ai_config, screen, nave, balas):
    """ Responde a eventos da tela, teclado e mouse """
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()
        # Programando as ações de movimento para direita (D) e para a esqueda (A)
        # elif event.type == pygame.KEYDOWN:
        #     check_events_keydown(event, ai_config, screen, nave, balas)

        # Trata os eventos quando as teclas são pressionadas:
        elif event.type == pygame.KEYDOWN:
            check_events_keydown(event, ai_config, screen, nave, balas)

        # Trata os eventos quando as teclas são soltas:
        elif event.type == pygame.KEYUP:
            check_events_keyup(event, nave)

        # Programando as ações de movimento para cima (W) e para baixo (S):
        elif event.type == pygame.KEYDOWN:
            # Chama o método check_events_keydown
            check_events_keydown(event, ai_config, screen, nave, balas)

        elif event.type == pygame.KEYUP:
            # Chama o método check_events_keyup:
            check_events_keyup(event, nave)


def update_screen(ai_config, screen, nave, aliens, balas):
    """ Atualiza as imagens da tela e atualiza para uma nova tela """
    # Redesenha todos os projéteis atrás das naves e dos alienígenas:
    for bala in balas.sprites():
        bala.draw_bala()

    # Deixa a tela mais recente visível:
    pygame.display.flip()

    # Recebe os valores das cores para gerar a cor da screen:
    screen.fill(ai_config.bgcolor)
    nave.blitme()
    aliens.draw(screen)


def update_balas(ai_config, screen, nave, aliens, balas):
    # Atualiza a posição das balas:
    balas.update()

    """Livrando-se das balas que passaram da tela para não consumir memória: """
    for bala in balas.copy():
        if bala.rect.bottom <= 0:
            balas.remove(bala)

    # Faz a verificação de colisão entre uma bala e uma nave alienígena:
    colisao = pygame.sprite.groupcollide(balas, aliens, True, True)

    # Verifica se todas as naves alienígenas foram eliminadas e então
    # gera uma nova frota de naves.
    if len(aliens) == 0:
        balas.empty()
        cria_frota(ai_config, screen, nave, aliens)


def get_num_aliens_x(ai_config, alienigena_width):
    """ Determinar o número de alienígenas que cabem na horizontal da screen """
    espaco_disponivel_x = ai_config.screen_width - 1 * alienigena_width
    num_alienigenas_x = int(1 * espaco_disponivel_x / (1.5 * alienigena_width))
    return num_alienigenas_x


def get_num_rows(ai_config, nave_height, alienigena_height):
    """ Determinar o número de alienígenas que cabem no eixo vertical da screen """
    espaco_disponivel_y = (ai_config.screen_height -
                           (3 * alienigena_height) - nave_height)
    num_rows = int(2 * espaco_disponivel_y / (3 * alienigena_height))
    return num_rows


def cria_alien(ai_config, screen, aliens, alienigenas_num, num_rows):
    """ Cria uma nave alienígena e posiciona de forma ordenada horizontalmente na screen"""
    alienigena = Alienigenas(ai_config, screen)
    alienigena_width = alienigena.rect.width
    alienigena.x = alienigena_width + 1.5 * alienigena_width * alienigenas_num
    alienigena.rect.x = alienigena.x
    alienigena.rect.y = alienigena.rect.height + 1.5 * alienigena.rect.height * num_rows
    aliens.add(alienigena)


def cria_frota(ai_config, screen, nave, aliens):
    """ Cria o exercito de alienígenas do game """
    alienigena = Alienigenas(ai_config, screen)
    num_alienigenas_x = get_num_aliens_x(ai_config, alienigena.rect.width)
    num_rows = get_num_rows(ai_config, nave.rect.height, alienigena.rect.height)

    for row_number in range(num_rows):
        # Criando a primeira linha de alienígenas:
        for alienigenas_num in range(num_alienigenas_x):
            cria_alien(ai_config, screen, aliens, alienigenas_num, row_number)


def check_borda_frota(ai_config, aliens):
    """ Verifica se alguma nave alienígena alcançou a borda da screen """
    for alienigenas in aliens.sprites():
        if alienigenas.check_bordas():
            muda_direcao_frota(ai_config, aliens)
            break


def muda_direcao_frota(ai_config, aliens):
    """ Faz a tropa de alienígenas descer e mudar de direção """
    for alienigenas in aliens.sprites():
        alienigenas.rect.y += ai_config.frota_dobra_velocidade
    ai_config.direcao_tropa *= -1


def check_aliens_bottom(ai_config, estatistica, screen, nave, aliens, balas):
    """ Verifica se alguma nave alienígena da frota alcançou a bottom da screen """
    screen_rect = screen.get_rect()
    for alienigenas in aliens.sprites():
        if alienigenas.rect.bottom >= screen_rect.bottom:
            # Chama o método nave_hit se alguma nave atingir a borda inferior da tela:
            nave_hit(ai_config, estatistica, screen, nave, aliens, balas)
            break


def update_aliens(ai_config, estatistica, screen, nave, aliens, balas):
    """ Verifica se as tropas estão nas bordas da screen
     e atualiza a posição de toda a frota alienígena na screen """
    check_borda_frota(ai_config, aliens)
    check_aliens_bottom(ai_config, estatistica, screen, nave, aliens, balas)
    aliens.update()

    # Faz a verificação de colisão entre as naves alienígenas e aww nave terrestre:
    if pygame.sprite.spritecollideany(nave, aliens):
        nave_hit(ai_config, estatistica, screen, nave, aliens, balas)