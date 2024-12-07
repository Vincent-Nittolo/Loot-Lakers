# import the necessary libraries
import pygame
from pygame import mixer, MOUSEBUTTONUP, MOUSEBUTTONDOWN
import random
from Code.buttons import *
from pygame.examples.aliens import Player
from Code.values import Values
from Code.files import File
from Code.spaces import make_board
from Code.print_screens import *
from Code.players import *

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
        vals.jx, vals.jy = pygame.mouse.get_pos()
        vals.mx, vals.my = pygame.mouse.get_pos()

        if i.type == MOUSEBUTTONDOWN and i.button == 1:
            vals.clicking = True

            if vals.START:
                start_button(vals)

            if vals._CHOOSE:
                choose_players(vals, Players, file)
                continue_button_1(vals)
                print_num_players(scrn, pygame, file, vals)

            if vals.SELEC:
                icons(vals, Players, file)
                print_selec(Players, scrn, pygame, file, vals)
                print_selec(Players, scrn, pygame, file, vals)
                continue_button_2(vals)

            if vals.GAME:
                pay(vals, board)

                settings_button(vals)

                info_button(vals)

                # Next Turn
                roll_dice(vals, mixer, file, pygame, board, random)

                # Checks if the player rolls doubles
                check_doubles(vals)

                # Player presses next turn
                next_turn(vals, random)

                # Player presses roll again
                roll_again(vals, random)

                purchase(vals, board)

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

            if vals.full_screen and not vals.SETTINGS:
                sound_board(pygame, vals, file, mixer)


            print(f'{vals.mx} {vals.my}')

        elif i.type == MOUSEBUTTONUP and i.button == 1:
            vals.clicking = False

        if vals.full_screen and not vals.SETTINGS:
            print_easter_egg(file, scrn, pygame, vals)

        if vals.GAME:
            if vals.plays[vals.player-1].CPU is True:

                vals.mx = 880
                vals.my = 60
                roll_dice(vals, mixer, file, pygame, board, random)

                vals.mx = 880
                vals.my = 60
                check_doubles(vals)

                vals.mx = 680
                vals.my = 720
                pay(vals, board)

                vals.mx = 680
                vals.my = 720
                purchase(vals, board)

                vals.mx = 930
                vals.my = 10
                next_turn(vals, random)
                roll_again(vals, random)

                print_board(scrn, pygame, file, vals, board)

        if vals.nums_of_turns >100:
            temp = []
            for k in range(1, 3):
                if vals.plays[i].health > 0:
                    temp.append(vals.plays[i])
            vals.winner = random.choice(temp)
            mixer.music.load(file.win_sound)
            pygame.mixer.music.queue(file.music)
            mixer.music.play()
            vals.WIN = True

        if vals.WIN:
            print_win(scrn, vals, pygame, file, mixer)

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