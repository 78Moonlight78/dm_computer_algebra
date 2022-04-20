import sys
import pygame as pg
import os
from pygame import MOUSEBUTTONDOWN, QUIT
import time

from translate import *
from rational import *
from natural import *
from integer import *
from polynomials import *
from config import *


def correct_polinom(symb,text):
    flag = False
    if text:
        if text[-1:] in '/' and symb in NUMBER:
            flag = True
        elif text[-1:] == " " and (symb in '+-' or symb in NUMBER):
            flag = True
        elif text[-1:] in "+-" and symb in NUMBER:
            flag = True
        elif text[-1:] in NUMBER and (symb in ' /' or symb in NUMBER):
            flag = True
    else:
        if symb in NUMBER or symb in '+-':
            flag = True
    return flag


def screen_input_nat():
    screen.fill(WHITE)
    cursor = 0
    input_rect1 = pg.Rect(screen_width//17, int(screen_height*0.17), screen_width//9*7, int(1/20 * screen_height))
    input_rect2 = pg.Rect(screen_width//17, int(screen_height*0.25), screen_width//9*7, int(1/20 * screen_height))
    output_rect = pg.Rect(screen_width//17, int(screen_height*0.33), screen_width//9*7, int(1/20 * screen_height))
    input_text1, input_text2, output_text = '', '', 'Вывод'
    active1, active2 = False, False
    click = False
    while True:
        for event in pg.event.get():
            click = False
            # if user types QUIT then the screen will close
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if input_rect1.collidepoint(event.pos):
                    active1 = True
                    active2 = False
                    click = False
                else:
                    active1 = False
                if input_rect2.collidepoint(event.pos):
                    active2 = True
                    active1 = False
                    click = False
                else:
                    active2 = False
                if not (input_rect1.collidepoint(event.pos) and input_rect2.collidepoint(event.pos)):
                    for i in range(8):
                        mouse = pg.mouse.get_pos()
                        button_i = button_layout_level_menu[i]
                        if button_i[0] < mouse[0] < button_i[0] + button_i[2] and button_i[1] < mouse[1] < button_i[1] + \
                                button_i[3]:
                            click = True
            if event.type == pg.KEYDOWN:
                # Check for backspace
                if event.key == pg.K_BACKSPACE:
                    # get text input from 0 to -1 i.e. end.
                    if active1:
                        input_text1 = input_text1[:-1]
                    if active2:
                        input_text2 = input_text2[:-1]
                # Unicode standard is used for string
                # formation
                else:
                    if active1 and event.unicode in NUMBER:
                        input_text1 += event.unicode
                    elif active2 and event.unicode in NUMBER:
                        input_text2 += event.unicode
        # it will set background color of screen
        if button("С Л О Ж Е Н И Е", *button_layout_level_menu[0], click):
           if input_text1 and input_text2:
               output_text = output_nat(ADD_NN_N(*input_nat(input_text1), *input_nat(input_text2)))
           else:
               output_text = "Введите значение"
        elif button("В Ы Ч И Т А Н И Е", *button_layout_level_menu[1], click):
            if (input_text1 and input_text2) and input_text2 < input_text1:
                output_text = output_nat(SUB_NN_N(*input_nat(input_text1), *input_nat(input_text2)))
            else:
                output_text = "Первое меньше, попробуйте другое число"
        elif button("У М Н О Ж Е Н И Е ", *button_layout_level_menu[2], click):
            if (input_text1 and input_text2):
                output_text = output_nat(MUL_NN_N(*input_nat(input_text1), *input_nat(input_text2)))
        elif button("О С Т А Т О К  О Т  Д Е Л Е Н И Я ", *button_layout_level_menu[3], click):
            pass
        elif button("Ч А С Т Н О Е  О Т  Д Е Л Е Н И Я ", *button_layout_level_menu[4], click):
            if (input_text1 and input_text2) and input_text2 < input_text1:
                output_text = output_nat(DIV_NN_N(*input_nat(input_text1), *input_nat(input_text2)))
            else:
                output_text = "Первое меньше, попробуйте другое число"
        elif button("Н О Д", *button_layout_level_menu[5], click):
            if (input_text1 and input_text2):
                output_text = output_nat(GCF_NN_N(*input_nat(input_text1), *input_nat(input_text2)))
        elif button('Н О К', *button_layout_level_menu[6], click):
            if (input_text1 and input_text2):
                output_text = output_nat(LCM_NN_N(*input_nat(input_text1), *input_nat(input_text2)))
        elif button("В Ы Х О Д", *button_layout_level_menu[7], click):
            menu_of_type()

        text_surface1 = menu_text.render(input_text1, True, WHITE)
        text_surface2 = menu_text.render(input_text2, True, WHITE)
        text_surface3 = menu_text.render(output_text, True, WHITE)

        if active1:
            color1 = LIGHT_PINK
            txt_rect = text_surface1.get_rect()
            cursor = pg.Rect(txt_rect.topright, (3, txt_rect.height + 2))
        else:
            color1 = PINK
        if active2:
            color2 = LIGHT_PINK
            txt_rect = text_surface2.get_rect()
            cursor = pg.Rect(txt_rect.topright, (3, txt_rect.height + 2))
        else:
            color2 = PINK
        # draw rectangle and argument passed which should
        # be on screen
        pg.draw.rect(screen, color1, input_rect1)
        pg.draw.rect(screen, color2, input_rect2)
        pg.draw.rect(screen, LIGHT_PINK, output_rect)
        if time.time() % 1 > 0.5 and active1:
            # bounding rectangle of the text
            text_rect = text_surface1.get_rect(topleft=(input_rect1.x + 5, input_rect1.y + 10))
            # set cursor position
            cursor.midleft = text_rect.midright
            pg.draw.rect(screen, WHITE, cursor)
        elif time.time() % 1 > 0.5 and active2:
            # bounding rectangle of the text
            text_rect = text_surface2.get_rect(topleft=(input_rect2.x + 5, input_rect2.y + 5))
            # set cursor position
            cursor.midleft = text_rect.midright
            pg.draw.rect(screen, WHITE, cursor)
        # render at position stated in arguments
        screen.blit(text_surface1, (input_rect1.x + 5, input_rect1.y + 5))
        screen.blit(text_surface2, (input_rect2.x + 5, input_rect2.y + 5))
        screen.blit(text_surface3, (output_rect.x + 5, output_rect.y + 5))

        # display.flip() will update only a portion of the
        # screen to updated, not full area
        pg.display.flip()
        # clock.tick(60) means that for every second at most
        # 60 frames should be passed.
        clock.tick(60)


def screen_input_int():
    screen.fill(WHITE)
    cursor = 0
    input_rect1 = pg.Rect(screen_width // 17, int(screen_height * 0.2), screen_width // 9 * 7,
                          int(1 / 20 * screen_height))
    input_rect2 = pg.Rect(screen_width // 17, int(screen_height * 0.3), screen_width // 9 * 7,
                          int(1 / 20 * screen_height))
    output_rect = pg.Rect(screen_width // 17, int(screen_height * 0.4), screen_width // 9 * 7,
                          int(1 / 20 * screen_height))
    input_text1, input_text2, output_text = '', '', 'Вывод'
    active1, active2 = False, False
    click = False
    while True:
        for event in pg.event.get():
            click = False
            # if user types QUIT then the screen will close
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if input_rect1.collidepoint(event.pos):
                    active1 = True
                    active2 = False
                    click = False
                else:
                    active1 = False
                if input_rect2.collidepoint(event.pos):
                    active2 = True
                    active1 = False
                    click = False
                else:
                    active2 = False
                if not (input_rect1.collidepoint(event.pos) and input_rect2.collidepoint(event.pos)):
                    for i in range(6):
                        if i == 5:
                            i = 7
                        mouse = pg.mouse.get_pos()
                        button_i = button_layout_level_menu[i]
                        if button_i[0] < mouse[0] < button_i[0] + button_i[2] and button_i[1] < mouse[1] < button_i[1] + \
                                button_i[3]:
                            click = True

            if event.type == pg.KEYDOWN:
                # Check for backspace
                if event.key == pg.K_BACKSPACE:
                    # get text input from 0 to -1 i.e. end.
                    if active1:
                        input_text1 = input_text1[:-1]
                    if active2:
                        input_text2 = input_text2[:-1]
                # Unicode standard is used for string
                # formation
                else:
                    if active1 and (event.unicode in NUMBER or (event.unicode == '-' and input_text1 == '')):
                        input_text1 += event.unicode
                    elif active2 and (event.unicode in NUMBER or (event.unicode == '-' and input_text2 == '')):
                        input_text2 += event.unicode
        # it will set background color of screen
        flag = False
        if input_text1 and input_text2 and input_text1[-1:] != '-' and input_text2[-1:] != '-':
            flag = True
        if button("С Л О Ж Е Н И Е", *button_layout_level_menu[0], click):
            if flag:
                output_text = output_int(ADD_ZZ_Z(*input_int(input_text1), *input_int(input_text2)))
            else:
                output_text = "Введите значение"
        elif button("В Ы Ч И Т А Н И Е", *button_layout_level_menu[1], click):
            if flag:
                output_text = output_int(SUB_ZZ_Z(*input_int(input_text1), *input_int(input_text2)))
            else:
                output_text = "Введите значение"
        elif button("У М Н О Ж Е Н И Е ", *button_layout_level_menu[2], click):
            if flag:
                output_text = output_int(MUL_ZZ_Z(*input_int(input_text1), *input_int(input_text2)))
            else:
                output_text = "Введите значение"
        elif button("О С Т А Т О К  О Т  Д Е Л Е Н И Я ", *button_layout_level_menu[3], click):
            if flag:
                output_text = output_int(DIV_ZZ_Z(*input_int(input_text1), *input_int(input_text2)))
            else:
                output_text = "Введите значение"
        elif button("Ч А С Т Н О Е  О Т  Д Е Л Е Н И Я ", *button_layout_level_menu[4], click):
            if flag:
                output_text = output_int(MOD_ZZ_Z(*input_int(input_text1), *input_int(input_text2)))
            else:
                output_text = "Введите значение"
        elif button("В Ы Х О Д", *button_layout_level_menu[7], click):
            menu_of_type()

        text_surface1 = menu_text.render(input_text1, True, WHITE)
        text_surface2 = menu_text.render(input_text2, True, WHITE)
        text_surface3 = menu_text.render(output_text, True, WHITE)

        if active1:
            color1 = LIGHT_PINK
            txt_rect = text_surface1.get_rect()
            cursor = pg.Rect(txt_rect.topright, (3, txt_rect.height + 2))
        else:
            color1 = PINK
        if active2:
            color2 = LIGHT_PINK
            txt_rect = text_surface2.get_rect()
            cursor = pg.Rect(txt_rect.topright, (3, txt_rect.height + 2))
        else:
            color2 = PINK
        # draw rectangle and argument passed which should
        # be on screen
        pg.draw.rect(screen, color1, input_rect1)
        pg.draw.rect(screen, color2, input_rect2)
        pg.draw.rect(screen, LIGHT_PINK, output_rect)
        if time.time() % 1 > 0.5 and active1:
            # bounding rectangle of the text
            text_rect = text_surface1.get_rect(topleft=(input_rect1.x + 5, input_rect1.y + 10))
            # set cursor position
            cursor.midleft = text_rect.midright
            pg.draw.rect(screen, WHITE, cursor)
        elif time.time() % 1 > 0.5 and active2:
            # bounding rectangle of the text
            text_rect = text_surface2.get_rect(topleft=(input_rect2.x + 5, input_rect2.y + 5))
            # set cursor position
            cursor.midleft = text_rect.midright
            pg.draw.rect(screen, WHITE, cursor)
        # render at position stated in arguments
        screen.blit(text_surface1, (input_rect1.x + 5, input_rect1.y + 5))
        screen.blit(text_surface2, (input_rect2.x + 5, input_rect2.y + 5))
        screen.blit(text_surface3, (output_rect.x + 5, output_rect.y + 5))

        # display.flip() will update only a portion of the
        # screen to updated, not full area
        pg.display.flip()
        # clock.tick(60) means that for every second at most
        # 60 frames should be passed.
        clock.tick(60)


def rat_choice():
    screen.fill(WHITE)
    cursor = 0
    input_rect1 = pg.Rect(screen_width // 17, int(screen_height * 0.2), screen_width // 9 * 7,
                          int(1 / 20 * screen_height))
    input_rect2 = pg.Rect(screen_width // 17, int(screen_height * 0.3), screen_width // 9 * 7,
                          int(1 / 20 * screen_height))
    output_rect = pg.Rect(screen_width // 17, int(screen_height * 0.4), screen_width // 9 * 7,
                          int(1 / 20 * screen_height))
    input_text1, input_text2, output_text = '', '', 'Вывод'
    active1, active2 = False, False
    click = False
    while True:
        for event in pg.event.get():
            click = False
            # if user types QUIT then the screen will close
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if input_rect1.collidepoint(event.pos):
                    active1 = True
                    active2 = False
                    click = False
                else:
                    active1 = False
                if input_rect2.collidepoint(event.pos):
                    active2 = True
                    active1 = False
                    click = False
                else:
                    active2 = False
                if not (input_rect1.collidepoint(event.pos) and input_rect2.collidepoint(event.pos)):
                    for i in range(6):
                        if i == 5:
                            i = 7
                        mouse = pg.mouse.get_pos()
                        button_i = button_layout_level_menu[i]
                        if button_i[0] < mouse[0] < button_i[0] + button_i[2] and button_i[1] < mouse[1] < button_i[1] + \
                                button_i[3]:
                            click = True

            if event.type == pg.KEYDOWN:
                # Check for backspace
                if event.key == pg.K_BACKSPACE:
                    # get text input from 0 to -1 i.e. end.
                    if active1:
                        input_text1 = input_text1[:-1]
                    if active2:
                        input_text2 = input_text2[:-1]
                # Unicode standard is used for string
                # formation
                else:
                    if active1 and (event.unicode in NUMBER or (event.unicode == '-' and len(input_text1) == 0)
                                    or (event.unicode == '/' and len(input_text1) != 0 and '/' not in input_text1)):
                        input_text1 += event.unicode
                    elif active2 and (event.unicode in NUMBER or (event.unicode == '-' and len(input_text2) == 0)
                                    or (event.unicode == '/' and len(input_text2) != 0 and '/' not in input_text2)):
                        input_text2 += event.unicode
        # it will set background color of screen
        flag = False
        if ('/' in input_text1 and '/' in input_text2) and input_text1 and input_text2:
            if input_text1[len(input_text1) - 1] != '/' and input_text2[len(input_text2) - 1] != '/':
                flag = True
        if button("С Л О Ж Е Н И Е", *button_layout_level_menu[0], click):
            if flag:
                output_text = output_rational(ADD_QQ_Q(input_rational(input_text1), input_rational(input_text2)))
            else:
                output_text = "Введите значение"
        elif button("В Ы Ч И Т А Н И Е", *button_layout_level_menu[1], click):
            if flag:
                output_text = output_rational(SUB_QQ_Q(input_rational(input_text1), input_rational(input_text2)))
            else:
                output_text = "Введите значение"
        elif button("У М Н О Ж Е Н И Е ", *button_layout_level_menu[2], click):
            if flag:
                output_text = output_rational(MUL_QQ_Q(input_rational(input_text1), input_rational(input_text2)))
            else:
                output_text = "Введите значение"
        elif button(" Д Е Л Е Н И Е ", *button_layout_level_menu[3], click):
            if flag:
                output_text = output_rational(DIV_QQ_Q(input_rational(input_text1), input_rational(input_text2)))
            else:
                output_text = "Введите значение"
        elif button("В Ы Х О Д", *button_layout_level_menu[7], click):
            menu_of_type()

        text_surface1 = menu_text.render(input_text1, True, WHITE)
        text_surface2 = menu_text.render(input_text2, True, WHITE)
        text_surface3 = menu_text.render(output_text, True, WHITE)

        if active1:
            color1 = LIGHT_PINK
            txt_rect = text_surface1.get_rect()
            cursor = pg.Rect(txt_rect.topright, (3, txt_rect.height + 2))
        else:
            color1 = PINK
        if active2:
            color2 = LIGHT_PINK
            txt_rect = text_surface2.get_rect()
            cursor = pg.Rect(txt_rect.topright, (3, txt_rect.height + 2))
        else:
            color2 = PINK
        # draw rectangle and argument passed which should
        # be on screen
        pg.draw.rect(screen, color1, input_rect1)
        pg.draw.rect(screen, color2, input_rect2)
        pg.draw.rect(screen, LIGHT_PINK, output_rect)
        if time.time() % 1 > 0.5 and active1:
            # bounding rectangle of the text
            text_rect = text_surface1.get_rect(topleft=(input_rect1.x + 5, input_rect1.y + 10))
            # set cursor position
            cursor.midleft = text_rect.midright
            pg.draw.rect(screen, WHITE, cursor)
        elif time.time() % 1 > 0.5 and active2:
            # bounding rectangle of the text
            text_rect = text_surface2.get_rect(topleft=(input_rect2.x + 5, input_rect2.y + 5))
            # set cursor position
            cursor.midleft = text_rect.midright
            pg.draw.rect(screen, WHITE, cursor)
        # render at position stated in arguments
        screen.blit(text_surface1, (input_rect1.x + 5, input_rect1.y + 5))
        screen.blit(text_surface2, (input_rect2.x + 5, input_rect2.y + 5))
        screen.blit(text_surface3, (output_rect.x + 5, output_rect.y + 5))

        # display.flip() will update only a portion of the
        # screen to updated, not full area
        pg.display.flip()
        # clock.tick(60) means that for every second at most
        # 60 frames should be passed.
        clock.tick(60)


def polinom_choice():
    screen.fill(WHITE)
    cursor = 0
    input_rect1 = pg.Rect(screen_width // 17, int(screen_height * 0.16), screen_width // 9 * 7,
                          int(1 / 20 * screen_height))
    input_rect2 = pg.Rect(screen_width // 17, int(screen_height * 0.23), screen_width // 9 * 7,
                          int(1 / 20 * screen_height))
    input_rect3 = pg.Rect(screen_width // 17, int(screen_height * 0.3), screen_width // 9 * 7,
                          int(1 / 20 * screen_height))
    input_rect4 = pg.Rect(screen_width // 17, int(screen_height * 0.37), screen_width // 9 * 7,
                          int(1 / 20 * screen_height))
    output_rect = pg.Rect(screen_width // 17, int(screen_height * 0.44), screen_width // 9 * 7,
                          int(1 / 20 * screen_height))
    input_text1, input_text2, input_text3, input_text4, output_text = '', '', '', '', 'Вывод'
    active1, active2, active3, active4 = False, False, False, False
    click = False
    while True:
        for event in pg.event.get():
            click = False
            # if user types QUIT then the screen will close
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if input_rect1.collidepoint(event.pos):
                    click = False
                    active1 = True
                else:
                    active1 = False
                if input_rect2.collidepoint(event.pos):
                    click = False
                    active2 = True
                else:
                    active2 = False

                if input_rect3.collidepoint(event.pos):
                    click = False
                    active3 = True
                else:
                    active3 = False
                if input_rect4.collidepoint(event.pos):
                    click = False
                    active4 = True
                else:
                    active4 = False
                if not (input_rect1.collidepoint(event.pos) and input_rect2.collidepoint(event.pos)):
                    for i in range(6):
                        if i == 5:
                            i = 7
                        mouse = pg.mouse.get_pos()
                        button_i = button_layout_level_menu[i]
                        if button_i[0] < mouse[0] < button_i[0] + button_i[2] and button_i[1] < mouse[1] < button_i[1] + \
                                button_i[3]:
                            click = True

            if event.type == pg.KEYDOWN:
                # Check for backspace
                if event.key == pg.K_BACKSPACE:
                    # get text input from 0 to -1 i.e. end.
                    if active1:
                        input_text1 = input_text1[:-1]
                    if active2:
                        input_text2 = input_text2[:-1]
                    if active3:
                        input_text3 = input_text3[:-1]
                    if active4:
                        input_text4 = input_text4[:-1]
                # Unicode standard is used for string
                # formation
                else:
                    if active1 and (event.unicode in NUMBER or event.unicode == ' '):
                        input_text1 += event.unicode
                    elif active2 and correct_polinom(event.unicode, input_text2):
                        input_text2 += event.unicode
                    elif active3 and (event.unicode in NUMBER or event.unicode == ' '):
                        input_text3 += event.unicode
                    elif active4 and correct_polinom(event.unicode, input_text4):
                        input_text4 += event.unicode
        # it will set background color of screen
        flag = 'Не верные данные'
        if input_text1 and input_text2 and input_text3 and input_text4:
            if input_text2[-1:] not in '+- /' and input_text1[-1] != ' ' and input_text4[-1:] not in '+- /' and input_text3[-1] != ' ':
                flag = False
        if button("С Л О Ж Е Н И Е", *button_layout_level_menu[0], click):
            if not flag and input_polynom(input_text1, input_text2) and input_polynom(input_text3, input_text4):
                output_text = output_pol(ADD_PP_P(*input_polynom(input_text1, input_text2), *input_polynom(input_text3, input_text4)))
            else:
                output_text = flag
        elif button("В Ы Ч И Т А Н И Е", *button_layout_level_menu[1], click):
            if not flag and input_polynom(input_text1, input_text2) and input_polynom(input_text3, input_text4):
                output_text = output_pol(SUB_PP_P(*input_polynom(input_text1, input_text2), *input_polynom(input_text3, input_text4)))
            else:
                output_text = flag
        elif button("У М Н О Ж Е Н И Е ", *button_layout_level_menu[2], click):
            if not flag and input_polynom(input_text1, input_text2) and input_polynom(input_text3, input_text4):
                output_text = output_pol(MUL_PP_P(*input_polynom(input_text1, input_text2), *input_polynom(input_text3, input_text4)))
            else:
                output_text = flag
        elif button("О С Т А Т О К  О Т  Д Е Л Е Н И Я ", *button_layout_level_menu[3], click):
            pass
        elif button("Ч А С Т Н О Е  О Т  Д Е Л Е Н И Я ", *button_layout_level_menu[4], click):
            pass
        elif button("П Р О И З В О Д Н А Я ", *button_layout_level_menu[5], click):
            pass
        elif button("В Ы Х О Д", *button_layout_level_menu[7], click):
            menu_of_type()

        text_surface1 = menu_text.render(input_text1, True, WHITE)
        text_surface2 = menu_text.render(input_text2, True, WHITE)
        text_surface3 = menu_text.render(input_text3, True, WHITE)
        text_surface4 = menu_text.render(input_text4, True, WHITE)
        text_surface5 = menu_text.render(output_text, True, WHITE)

        if active1:
            color1 = LIGHT_PINK
            txt_rect = text_surface1.get_rect()
            cursor = pg.Rect(txt_rect.topright, (3, txt_rect.height + 2))
        else:
            color1 = PINK
        if active2:
            color2 = LIGHT_PINK
            txt_rect = text_surface2.get_rect()
            cursor = pg.Rect(txt_rect.topright, (3, txt_rect.height + 2))
        else:
            color2 = PINK
        if active3:
            color3 = LIGHT_PINK
            txt_rect = text_surface3.get_rect()
            cursor = pg.Rect(txt_rect.topright, (3, txt_rect.height + 2))
        else:
            color3 = PINK
        if active4:
            color4 = LIGHT_PINK
            txt_rect = text_surface4.get_rect()
            cursor = pg.Rect(txt_rect.topright, (3, txt_rect.height + 2))
        else:
            color4 = PINK
        # draw rectangle and argument passed which should
        # be on screen
        pg.draw.rect(screen, color1, input_rect1)
        pg.draw.rect(screen, color2, input_rect2)
        pg.draw.rect(screen, color3, input_rect3)
        pg.draw.rect(screen, color4, input_rect4)
        pg.draw.rect(screen, LIGHT_PINK, output_rect)
        if time.time() % 1 > 0.5 and active1:
            # bounding rectangle of the text
            text_rect = text_surface1.get_rect(topleft=(input_rect1.x + 5, input_rect1.y + 10))
            # set cursor position
            cursor.midleft = text_rect.midright
            pg.draw.rect(screen, WHITE, cursor)
        elif time.time() % 1 > 0.5 and active2:
            # bounding rectangle of the text
            text_rect = text_surface2.get_rect(topleft=(input_rect2.x + 5, input_rect2.y + 5))
            # set cursor position
            cursor.midleft = text_rect.midright
            pg.draw.rect(screen, WHITE, cursor)
        elif time.time() % 1 > 0.5 and active3:
            # bounding rectangle of the text
            text_rect = text_surface3.get_rect(topleft=(input_rect3.x + 5, input_rect3.y + 5))
            # set cursor position
            cursor.midleft = text_rect.midright
            pg.draw.rect(screen, WHITE, cursor)
        elif time.time() % 1 > 0.5 and active4:
            # bounding rectangle of the text
            text_rect = text_surface4.get_rect(topleft=(input_rect4.x + 5, input_rect4.y + 5))
            # set cursor position
            cursor.midleft = text_rect.midright
            pg.draw.rect(screen, WHITE, cursor)

        # render at position stated in arguments
        screen.blit(text_surface1, (input_rect1.x + 5, input_rect1.y + 5))
        screen.blit(text_surface2, (input_rect2.x + 5, input_rect2.y + 5))
        screen.blit(text_surface3, (input_rect3.x + 5, input_rect3.y + 5))
        screen.blit(text_surface4, (input_rect4.x + 5, input_rect4.y + 5))
        screen.blit(text_surface5, (output_rect.x + 5, output_rect.y + 5))

        # display.flip() will update only a portion of the
        # screen to updated, not full area
        pg.display.flip()
        # clock.tick(60) means that for every second at most
        # 60 frames should be passed.
        clock.tick(60)


def window_init():
    # получаем размеры монитора
    # в pg неудобно получать размер монитора, поэтому воспользуемся
    # другой библиотекой
    from tkinter import Tk
    temp = Tk()
    MONITOR_SIZE = temp.winfo_screenwidth(), temp.winfo_screenheight()
    temp.destroy()
    del temp
    # помещаем окно в центр экрана
    screen_coords = ((MONITOR_SIZE[0] - WIN_SIZE.w) // 3 * 2, (MONITOR_SIZE[1] - WIN_SIZE.h) // 2)
    os.environ['SDL_VIDEO_WINDOW_POS'] = f"{screen_coords[0]}, {screen_coords[1]}"

    screen = pg.display.set_mode(WIN_SIZE.size)

    return screen


def load_image(name, color_key=None, w=WIN_SIZE.width, h=WIN_SIZE.height):
    # Получаем путь до файла
    fullname = os.path.join('data', name)
    # При неудачной попытке загрузить картинку вызываем исключение
    try:
        image = pg.image.load(fullname).convert()
    except pg.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)
    # Если указан color_key == -1, то устанавливаем значение colorkey для плосоксти image
    if color_key is not None:
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    # Оптимизируем плоскость для переноса на текущий экран
    # ("the new surface will be optimized for blitting to the current display")
    else:
        image = image.convert_alpha()
    image = pg.transform.scale(image, (w, h))
    return image


# создание кнопки, функция получает текст, координаты x, y, ширина, высота, а также значение типа bool(нажата ли кнопка или нет)
def button(text, x, y, w, h, click, inactive_colour=PINK, active_colour=LIGHT_PINK, text_colour=WHITE):
    mouse = pg.mouse.get_pos()
    return_value = False
    if x < mouse[0] < x + w and y < mouse[1] < y + h:  # отрисовка "светлой" кнопки
        pg.draw.rect(screen, active_colour, (x, y, w, h))
        if click and pg.time.get_ticks() > 100: return_value = True  # возвращение значение True, если кнопка была нажата
    else:
        pg.draw.rect(screen, inactive_colour, (x, y, w, h))  # отрисовка "темной" кнопки

    text_surf, text_rect = text_objects(text, small_text, colour=text_colour)
    text_rect.center = (int(x + w / 2), int(y + h / 2))
    screen.blit(text_surf, text_rect)  # отрисовка текста
    return return_value

# создание поверхности текста
def text_objects(text, font, colour=BLACK):
    text_surface = font.render(text, True, colour)
    return text_surface, text_surface.get_rect()


def text_objects(text, font, colour=BLACK):
    text_surface = font.render(text, True, colour)
    return text_surface, text_surface.get_rect()

def menu_of_type():
    screen.fill(WHITE)
    pg.display.flip()
    text_surf, text_rect = text_objects('Я система компьютерной алгебры, выберите, с чем хотите работать ', menu_text)
    text_rect.center = ((screen_width // 2), (screen_height // 7))
    screen.blit(text_surf, text_rect)
    image = load_image('girl_1.png', -1, screen_width//8*7, screen_height//7*6)
    screen.blit(image, (50, 100))
    pg.display.update()
    click = False
    while True:
        pressed_keys = pg.key.get_pressed()
        for event in pg.event.get():
            if event.type == QUIT:
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                for i in range(4):

                    mouse = pg.mouse.get_pos()
                    button_i = button_main_menu[i]
                    if button_i[0] < mouse[0] < button_i[0] + button_i[2] and button_i[1] < mouse[1] < button_i[1] + \
                            button_i[3]:
                        click = True
        if button('Н А Т У Р А Л Ь Н Ы Е', *button_main_menu[0], click):
            screen_input_nat()
        elif button('Ц Е Л Ы Е', *button_main_menu[1], click):
            screen_input_int()
        elif button('Д Р О Б Н Ы Е', *button_main_menu[2], click):
            rat_choice()
        elif button('М Н О Г О Ч Л Е Н Ы', *button_main_menu[3], click):
            polinom_choice()

        pg.display.update(button_main_menu)
        clock.tick(60)

if __name__ == '__main__':
    pg.init()
    screen = window_init()
    pg.display.set_caption('computer algebra')
    """programIcon = pg.image.load('data/girl_2.png')
    pg.display.set_icon(programIcon)"""
    screen_width, screen_height = screen.get_size()
    small_text = pg.font.SysFont('arial', int(29 / 1440 * screen_height))
    menu_text = pg.font.SysFont('arial', int(50 / 1440 * screen_height))
    clock = pg.time.Clock()
    BUTTON_WIDTH_LEVEL = int(screen_width * 0.3)
    BUTTON_HEIGHT_LEVEL = int(screen_height * 5 // 81)
    button_main_menu = [(0, 0, screen_width // 4,  screen_height // 10),
                        (screen_width // 4, 0,screen_width // 4,  screen_height // 10),
                        (screen_width // 2, 0, screen_width // 4,  screen_height // 10),
                        (screen_width // 4 * 3, 0, screen_width // 4,  screen_height // 10)]
    button_layout_level_menu = [(screen_width//17, int(screen_height * 63 // 81), BUTTON_WIDTH_LEVEL, BUTTON_HEIGHT_LEVEL),
                                (screen_width//17 + BUTTON_WIDTH_LEVEL, int(screen_height * 63 // 81), BUTTON_WIDTH_LEVEL, BUTTON_HEIGHT_LEVEL),
                                (screen_width//17 + BUTTON_WIDTH_LEVEL*2, int(screen_height * 63 // 81), BUTTON_WIDTH_LEVEL, BUTTON_HEIGHT_LEVEL),
                                (screen_width//17, int(screen_height * 69 // 81), BUTTON_WIDTH_LEVEL, BUTTON_HEIGHT_LEVEL),
                                (screen_width//17 + BUTTON_WIDTH_LEVEL,int(screen_height * 69 // 81), BUTTON_WIDTH_LEVEL, BUTTON_HEIGHT_LEVEL),
                                (screen_width//17 + BUTTON_WIDTH_LEVEL*2, int(screen_height * 69 // 81), BUTTON_WIDTH_LEVEL, BUTTON_HEIGHT_LEVEL),
                                (screen_width//17 + BUTTON_WIDTH_LEVEL, int(screen_height * 75 // 81), BUTTON_WIDTH_LEVEL, BUTTON_HEIGHT_LEVEL),
                                (screen_width//25, int(screen_height // 40), BUTTON_WIDTH_LEVEL, BUTTON_HEIGHT_LEVEL)]
    menu_of_type()
