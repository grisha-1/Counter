# -*- coding: utf-8 -*-
# Импортировать в текстовый документ в виде таблицы
import webbrowser
from settings import *

pygame.init()


sc = pygame.display.set_mode((700, 500), pygame.RESIZABLE)

pygame.display.set_caption('Счётчик баллов')
pygame.display.set_icon(pygame.image.load('img/icon.png'))
clock = pygame.time.Clock()
FPS = 20
page = 0

clubinfo = False
pointsinfo = False
points = ''
club = ''
cooldown = 0
CursorCooldown = 0
XMOUTION, YMOUTION = 0, 0

# fonts
font = pygame.font.SysFont('font.ttf', 25, bold=True)
logo_font = pygame.font.SysFont('logo_font.ttf', 50, bold=True)

# labels
# BUTTONS
render_chart = font.render('Топы в списке', 1, pygame.Color('black'))
render_in = font.render('Вбить клубы', 1, pygame.Color('black'))
render_people = font.render('Связаться', 1, pygame.Color('black'))
render_import = font.render('импорт в docx', 1, pygame.Color('black'))
render_delete = font.render('Очистить список', 1, pygame.Color('black'))
# INFO
render_club_info = font.render('Клуб:', 1, pygame.Color('black'))
render_points_info = font.render('Баллы: ', 1, pygame.Color('black'))
render_add_club = font.render('ДОБАВИТЬ КЛУБ', 1, pygame.Color('black'))
render_successfully = font.render('Операция прошла успешно!', 1, pygame.Color('black'))
# LOGO
render_logo = logo_font.render('Счётчик', 1, pygame.Color('White'))
# Цикл
while True:
    cursor_img = pygame.image.load('img/cursor.png').convert_alpha()
    cursor_img.set_colorkey((255, 255, 255))
    cursor_img_rect = cursor_img.get_rect()
    cursor_img_rect = pygame.mouse.get_pos()
    if cooldown > 0:
        cooldown -= 0.3
    key = pygame.key.get_pressed()
    pointschars = {key[pygame.K_0]: '0', key[pygame.K_1]: '1', key[pygame.K_2]: '2', key[pygame.K_3]: '3',
                   key[pygame.K_4]: '4', key[pygame.K_5]: '5', key[pygame.K_6]: '6', key[pygame.K_7]: '7',
                   key[pygame.K_8]: '8', key[pygame.K_9]: '9'}

    clubschars = {key[pygame.K_0]: '0', key[pygame.K_1]: '1', key[pygame.K_2]: '2', key[pygame.K_3]: '3',
                  key[pygame.K_4]: '4', key[pygame.K_5]: '5', key[pygame.K_6]: '6', key[pygame.K_7]: '7',
                  key[pygame.K_8]: '8', key[pygame.K_9]: '9', key[pygame.K_a]: 'a', key[pygame.K_b]: 'b',
                  key[pygame.K_c]: 'c', key[pygame.K_d]: 'd', key[pygame.K_e]: 'e', key[pygame.K_f]: 'f',
                  key[pygame.K_g]: 'g', key[pygame.K_h]: 'h', key[pygame.K_j]: 'j', key[pygame.K_k]: 'k',
                  key[pygame.K_l]: 'l', key[pygame.K_m]: 'm', key[pygame.K_n]: 'n', key[pygame.K_o]: 'o',
                  key[pygame.K_p]: 'p', key[pygame.K_q]: 'q', key[pygame.K_r]: 'r', key[pygame.K_s]: 's',
                  key[pygame.K_t]: 't', key[pygame.K_u]: 'u', key[pygame.K_v]: 'v', key[pygame.K_w]: 'w',
                  key[pygame.K_x]: 'x', key[pygame.K_y]: 'y', key[pygame.K_z]: 'z', key[pygame.K_i]: 'i',
                  key[pygame.K_MINUS]: '-'}
    # Курсор
    pygame.mouse.set_cursor(*pygame.cursors.arrow)
    # Определение параметров экрана
    width, height = pygame.display.get_surface().get_size()

    # Заполнение
    sc.fill(DARKGRAY)
    pygame.draw.rect(sc, 'gray', (0, 0, width // 4, height))
    # --------
    if 10 <= XMOUTION <= width // 4 - 5 and 10 <= YMOUTION <= height // 8:
        pygame.draw.rect(sc, SUPERLIGHTGRAY, (10, 10, width // 4 - 5, height // 8 - 5))
    else:
        pygame.draw.rect(sc, LIGHTGRAY, (10, 10, width // 4 - 5, height // 8 - 5))

    if 10 <= XMOUTION <= width // 4 - 5 and height // 8 * 2 <= YMOUTION <= height // 8 * 3:
        pygame.draw.rect(sc, SUPERLIGHTGRAY, (10, height // 4 + 10, width // 4 - 5, height // 8 - 5))
    else:
        pygame.draw.rect(sc, LIGHTGRAY, (10, height // 4 + 10, width // 4 - 5, height // 8 - 5))

    if 10 <= XMOUTION <= width // 4 - 5 and height // 8 * 4 <= YMOUTION <= height // 8 * 5:
        pygame.draw.rect(sc, SUPERLIGHTGRAY, (10, height // 4 * 2 + 10, width // 4 - 5, height // 8 - 5))
    else:
        pygame.draw.rect(sc, LIGHTGRAY, (10, height // 4 * 2 + 10, width // 4 - 5, height // 8 - 5))

    if 10 <= XMOUTION <= width // 4 - 5 and height // 8 * 6 <= YMOUTION <= height // 8 * 7:
        pygame.draw.rect(sc, SUPERLIGHTGRAY, (10, height // 4 * 3 + 10, width // 4 - 5, height // 8 - 5))
    else:
        pygame.draw.rect(sc, LIGHTGRAY, (10, height // 4 * 3 + 10, width // 4 - 5, height // 8 - 5))
    # --------
    if 10 <= XMOUTION <= width // 4 - 5 and height // 8 <= YMOUTION <= height // 8 * 2:
        pygame.draw.rect(sc, 'white', (10, height // 8 + 10, width // 4 - 5, height // 8 - 5))
    else:
        pygame.draw.rect(sc, SUPERLIGHTGRAY, (10, height // 8 + 10, width // 4 - 5, height // 8 - 5))

    if 10 <= XMOUTION <= width // 4 - 5 and height // 8 * 3 <= YMOUTION <= height // 8 * 4:
        pygame.draw.rect(sc, 'white', (10, height // 8 * 3 + 10, width // 4 - 5, height // 8 - 5))
    else:
        pygame.draw.rect(sc, SUPERLIGHTGRAY, (10, height // 8 * 3 + 10, width // 4 - 5, height // 8 - 5))

    if 10 <= XMOUTION <= width // 4 - 5 and height // 8 * 5 <= YMOUTION <= height // 8 * 6:
        pygame.draw.rect(sc, 'white', (10, height // 8 * 5 + 10, width // 4 - 5, height // 8 - 5))
    else:
        pygame.draw.rect(sc, SUPERLIGHTGRAY, (10, height // 8 * 5 + 10, width // 4 - 5, height // 8 - 5))

    if 10 <= XMOUTION <= width // 4 - 5 and height // 8 * 7 <= YMOUTION <= height // 8 * 8:
        pygame.draw.rect(sc, 'white', (10, height // 8 * 7 + 10, width // 4 - 5, height // 8 - 5))
    else:
        pygame.draw.rect(sc, SUPERLIGHTGRAY, (10, height // 8 * 7 + 10, width // 4 - 5, height // 8 - 5))
    # Определение страницы
    if page == 1:
        chart(top())
        page = 3
    if page == 3:
        pygame.draw.rect(sc, 'White', (width // 3, height // 3, width // 1.7, height // 6))
        sc.blit(render_successfully, (width // 3 + 10, height // 3 + 10))
    if page == 2:
        render_points = font.render(points, 1, pygame.Color('black'))
        render_club = font.render(club, 1, pygame.Color('black'))

        pygame.draw.rect(sc, LIGHTBLUE, (width // 2.5, 210, width // 2, 100))
        pygame.draw.rect(sc, 'white', (width // 2.5, 75, width // 2, 25))
        pygame.draw.rect(sc, 'white', (width // 2.5, 175, width // 2, 25))
        sc.blit(render_club_info, (width // 2.5 - 55, 75))
        sc.blit(render_points_info, (width // 2.5 - 70, 175))
        sc.blit(render_add_club, (width // 2.5, 250))
        if clubinfo:

            if CursorCooldown < 1:
                CursorCooldown += 0.15
            elif CursorCooldown < 2:
                render_club = font.render(club + '|', 1, pygame.Color('black'))
                CursorCooldown += 0.15
            else:
                CursorCooldown = 0

            if cooldown <= 0:
                if len(club) != 25:
                    for i in clubschars:
                        if i:
                            club += clubschars[i]
                            cooldown = 1
                if key[pygame.K_BACKSPACE] and len(club) != 0:
                    club = club[0:len(club) - 1]
                    cooldown = 1

        elif pointsinfo:
            if CursorCooldown < 1:
                CursorCooldown += 0.15
            elif CursorCooldown < 2:
                render_points = font.render(points + '|', 1, pygame.Color('black'))
                CursorCooldown += 0.15
            else:
                CursorCooldown = 0

            if cooldown <= 0:
                if len(points) != 20:
                    for i in pointschars:
                        if i:
                            points += pointschars[i]
                            cooldown = 1
                if key[pygame.K_BACKSPACE] and len(points) != 0:
                    points = points[0:len(points) - 1]
                    cooldown = 1
        sc.blit(render_club, (width // 2.5, 75))
        sc.blit(render_points, (width // 2.5, 175))

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEMOTION:
            XMOUTION, YMOUTION = event.pos
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if 10 <= event.pos[0] <= width // 4 + 10 and height // 8 * 7 + 10 <= event.pos[1] <= height:
                    webbrowser.open('https://t.me/Kochetcov_Grigoriy')
                if 10 <= event.pos[0] <= width // 4 + 10 and 5 <= event.pos[1] <= height // 8 + 10:
                    page = 1
                if 10 <= event.pos[0] <= width // 4 + 10 and height // 8 + 10 <= event.pos[1] <= height // 8 * 2 + 10:
                    page = 2
                if 10 <= event.pos[0] <= width // 4 + 10 and height // 8 * 2 + 10 <= event.pos[1] <= height // 8 * 3 + 5:
                    clear()
                    page = 3
                if page == 2 and width // 2.5 <= event.pos[0] <= width // 2.5 + width // 2 and 75 <= event.pos[
                    1] <= 100:
                    clubinfo = True
                    pointsinfo = False
                if page == 2 and width // 2.5 <= event.pos[0] <= width // 2.5 + width // 2 and 175 <= event.pos[
                    1] <= 200:
                    clubinfo = False
                    pointsinfo = True
                if page == 2 and width // 2.5 <= event.pos[0] <= width // 2.5 + width // 2 and 210 <= event.pos[
                    1] <= 310:
                    if points != '' and club != '':
                        points = int(points)
                        write(finder(club), club, points)
                        club = ''
                        points = ''
                if 10 <= event.pos[0] <= width // 4 + 10 and height // 8 * 3 + 10 <= event.pos[1] <= height // 2 + 5:
                    out_docx(top())
                    page = 3
    # отрисовка надписей
    # BUTTONS
    sc.blit(render_chart, (20, 25))
    sc.blit(render_in, (20, height // 8 + 25))
    sc.blit(render_delete, (20, height // 4 + 25))
    sc.blit(render_import, (20, height // 8 * 3 + 25))
    #
    #
    #
    sc.blit(render_people, (20, height // 8 * 7 + 25))
    # LOGO
    sc.blit(render_logo, (width // 2.5, 25))
    if page == 2 and width // 2.5 <= cursor_img_rect[0] <= width // 2.5 + width // 2 and 75 <= cursor_img_rect[
            1] <= 100 or page == 2 and width // 2.5 <= cursor_img_rect[0] <= width // 2.5 + width // 2 and 175 <= cursor_img_rect[
            1] <= 200:
        sc.blit(cursor_img, cursor_img_rect)
        pygame.mouse.set_visible(False)
    else:
        pygame.mouse.set_visible(True)
    # Обновление и задержка
    pygame.display.update()
    clock.tick(FPS)

