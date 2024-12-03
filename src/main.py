# import the necessary libraries
import pygame
from pygame import mixer, MOUSEBUTTONUP, MOUSEBUTTONDOWN
import random
from buttons import *
from values import Values
from files import File
from spaces import make_board
from print_screens import *
from players import *

# initializes the game and declares values of X and Y
pygame.init()
X = 1200
Y = 800
scrn = pygame.display.set_mode((X, Y))

# values that determine the current stage of the game
file = File()
vals = Values(pygame, file)
board = []
make_board(board, random)

# load images and define their rectangles
dance_image = pygame.image.load(file.dance)
dance_image = pygame.transform.scale(dance_image, (150, 150))
dance_rect = pygame.Rect(1600, 000, 150, 150)

goofy_laugh_image = pygame.image.load(file.goofy_laugh)
goofy_laugh_image = pygame.transform.scale(goofy_laugh_image, (150, 150))
goofy_laugh_rect = pygame.Rect(1600, 150, 150, 150)

hitmarker_image = pygame.image.load(file.hitmarker)
hitmarker_image = pygame.transform.scale(hitmarker_image, (150, 150))
hitmarker_rect = pygame.Rect(1600, 300, 150, 150)

fall_image = pygame.image.load(file.fall)
fall_image = pygame.transform.scale(fall_image, (150, 150))
fall_rect = pygame.Rect(1600, 450, 150, 150)

cat_image = pygame.image.load(file.cat)
cat_image = pygame.transform.scale(cat_image, (150, 150))
cat_rect = pygame.Rect(1600, 600, 150, 150)

cricket_image = pygame.image.load(file.cricket)
cricket_image = pygame.transform.scale(cricket_image, (150, 150))
cricket_rect = pygame.Rect(1600, 750, 150, 150)

# sets the window name
pygame.display.set_caption('Fortnite Monopoly')

# starts the mixer, loads the Fortnite theme song, sets the volume, and plays the theme
mixer.init()
mixer.music.load(file.music)
mixer.music.set_volume(0.2)
mixer.music.play()

# paint screen one time
pygame.display.flip()

# loop for running the game until the window is closed
status = True
while status:

    # iterate over the list of Event objects that was returned by pygame.event.get() method.
    for i in pygame.event.get():
        # stores the x and y values of the mouse
        vals.mx, vals.my = pygame.mouse.get_pos()
        # displays start screen if START is true

        if i.type == MOUSEBUTTONDOWN and i.button == 1:
            vals.clicking = True
            if vals.START:
                start_button(vals)

            if vals.CHOOSE:
                choose_players(vals)
                print_num_players(scrn, pygame, file, vals)

            if vals.SELEC:
                icons(vals, Players, file)
                print_selec(scrn, pygame, file, vals)
                continue_button(vals)

            if vals.GAME:
                if (vals.p_4.CPU and vals.player == 4):  # or (vals.p_2.CPU and vals.player == 2) or (vals.p_3.CPU and vals.player == 3) or vals.p_4.CPU and vals.player == 4):
                    roll_dice(vals, mixer, file, pygame, board, random)

                    check_doubles(vals)
                    if vals.DOUBLES:
                        roll_again(vals, random)
                        check_doubles(vals)

                    purchase(vals, board)

                    pay(vals, board)

                    next_turn(vals, random)
                    """
                    purchase(vals, board)
                    pygame.time.delay(500)




                    pay(vals, board)
                    pygame.time.delay(500)




                    next_turn(vals, random)
                    pygame.time.delay(500)
                    """

                settings_button(vals)

                info_button(vals)

                # Check for image click when full screen is active and settings are closed
                if vals.full_screen and not vals.SETTINGS and dance_rect.collidepoint(vals.mx, vals.my):
                    mixer.music.load(file.dance_sound)
                    pygame.mixer.music.queue(file.music)
                    mixer.music.play()
                    mixer.music.set_volume(1)
                if vals.full_screen and not vals.SETTINGS and goofy_laugh_rect.collidepoint(vals.mx, vals.my):
                    mixer.music.load(file.goofy_laugh_sound)
                    pygame.mixer.music.queue(file.music)
                    mixer.music.play()
                    mixer.music.set_volume(1)
                if vals.full_screen and not vals.SETTINGS and hitmarker_rect.collidepoint(vals.mx, vals.my):
                    mixer.music.load(file.hitmarker_sound)
                    pygame.mixer.music.queue(file.music)
                    mixer.music.play()
                    mixer.music.set_volume(1)
                if vals.full_screen and not vals.SETTINGS and fall_rect.collidepoint(vals.mx, vals.my):
                    mixer.music.load(file.fall_sound)
                    pygame.mixer.music.queue(file.music)
                    mixer.music.play()
                    mixer.music.set_volume(0.15)
                if vals.full_screen and not vals.SETTINGS and cat_rect.collidepoint(vals.mx, vals.my):
                    mixer.music.load(file.slang_sound)
                    pygame.mixer.music.queue(file.music)
                    mixer.music.play()
                    mixer.music.set_volume(1)
                if vals.full_screen and not vals.SETTINGS and cricket_rect.collidepoint(vals.mx, vals.my):
                    mixer.music.load(file.cricket_sound)
                    pygame.mixer.music.queue(file.music)
                    mixer.music.play()
                    mixer.music.set_volume(1)

                # Next Turn
                roll_dice(vals, mixer, file, pygame, board, random)

                # Checks if the player rolls doubles
                check_doubles(vals)

                # Player presses next turn
                next_turn(vals, random)

                # Player presses roll again
                roll_again(vals, random)

                purchase(vals, board)

                pay(vals, board)

                print_board(scrn, pygame, file, vals, board)

            if vals.INFO:
                print_info(scrn, pygame, file, vals)
                return_to_game(scrn, pygame, file, vals, board)

            if vals.SETTINGS:
                volume_button(vals, mixer)
                resize_screen(vals, pygame)
                screen_mode(vals)
                print_settings(scrn, pygame, file, vals)
                return_to_game(scrn, pygame, file, vals, board)
            if vals.WIN:
                print_win(scrn, vals, pygame, file, mixer)
            print(f'{vals.mx} {vals.my}')

        elif i.type == MOUSEBUTTONUP and i.button == 1:
            vals.clicking = False
        # display the dance image in full-screen mode only if settings is closed
        if vals.full_screen and not vals.SETTINGS:
            scrn.blit(dance_image, dance_rect.topleft)
            scrn.blit(hitmarker_image, hitmarker_rect.topleft)
            scrn.blit(goofy_laugh_image, goofy_laugh_rect.topleft)
            scrn.blit(fall_image, fall_rect.topleft)
            scrn.blit(cat_image, cat_rect.topleft)
            scrn.blit(cricket_image, cricket_rect.topleft)
            print_easter_egg(scrn, pygame, vals)
        print_start(scrn, pygame, file, vals)
        print_dice(pygame, scrn, vals)
        pygame.display.update()
        # if window is closed, the program ends
        if i.type == pygame.QUIT:
            status = False

# deactivates pygame library
pygame.quit()


def main():
    pass


if __name__ == "__main__":
    main()
