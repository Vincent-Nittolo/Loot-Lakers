from Code.render import *


def print_start(scrn, pygame, file, vals):
    if vals.START:
        scrn.fill(vals.current)
        render_images(pygame, file.start, scrn, (300, 120), (450, 450))
        render_images(pygame, file.title, scrn, (900, 200), (150, 150))

def print_num_players(scrn, pygame, file, vals):
    scrn.fill(vals.current)

    #diplays icons for each mode
    if not vals.solos and not vals.duos and not vals.trios and not vals.squads:
        # tells the user to pick the amount of players
        render_text(vals.font1, scrn, f'Please choose the amount of players!', (245, 245, 245), (600, 50))
        render_images(pygame, file.solo, scrn, (300, 300), (100, 100))

        render_images(pygame, file.duos, scrn, (300, 300), (800, 100))
        render_images(pygame, file.trios, scrn, (300, 300), (100, 450))
        render_images(pygame, file.squads, scrn, (300, 300), (800, 450))

    if (vals.solos or vals.duos or vals.trios or vals.squads):
        render_text(vals.font1, scrn, f'Please Continue!', (245, 245, 245), (200, 50))
        render_text(vals.font1, scrn, f'Continue', (245, 245, 245), (600, 500))


def print_selec(Players, scrn, pygame, file, vals):

    scrn.fill(vals.current)
    render_images(pygame, file.title, scrn, (500, 100), (650, 5))

    #tells the user whose turn it is to choose a player
    if vals.player <5:
        render_text(vals.font1, scrn, f'Player {vals.player} Choose:', (245, 245, 245), (200, 50))

    #the user is told to continue when all players are selected
    else:
        render_text(vals.font1, scrn, f'Please Continue!', (245, 245, 245), (200, 50))
        render_text(vals.font1, scrn, f'Continue', (245, 245, 245), (600, 500))

    #only shows the icons when they have not been selected yet
    if vals.num_players != 0:
        if vals.P1:
            render_images(pygame, file.nog_ops, scrn, (300, 300), (100, 100))

        if vals.P2:
            render_images(pygame, file.jonesy, scrn, (300, 300), (800, 100))

        if vals.P3:
            render_images(pygame, file.raven, scrn, (300, 300), (100, 450))

        if vals.P4:
            render_images(pygame, file.john_wick, scrn, (300, 300), (800, 450))

    else:
        if vals.P1 is True:
            vals.P1 = False
            if vals.player == 2:
                p_2 = Players(1, vals.player, file)
                p_2.set_start_val()
                vals.p_2 = p_2
                vals.p_2.CPU = True
                vals.plays.append(vals.p_2)
            elif vals.player == 3:
                p_3 = Players(1, vals.player, file)
                p_3.set_start_val()
                vals.p_3 = p_3
                vals.p_3.CPU = True
                vals.plays.append(vals.p_3)
            elif vals.player == 4:
                p_4 = Players(1, vals.player, file)
                p_4.set_start_val()
                vals.p_4 = p_4
                vals.p_4.CPU = True
                vals.plays.append(vals.p_4)
            vals.player += 1

        if vals.P2 is True:
            vals.P2 = False
            if vals.player == 2:
                p_2 = Players(2, vals.player, file)
                p_2.set_start_val()
                vals.p_2 = p_2
                vals.p_2.CPU = True
                vals.plays.append(vals.p_2)
            elif vals.player == 3:
                p_3 = Players(2, vals.player, file)
                p_3.set_start_val()
                vals.p_3 = p_3
                vals.p_3.CPU = True
                vals.plays.append(vals.p_3)
            elif vals.player == 4:
                p_4 = Players(2, vals.player, file)
                p_4.set_start_val()
                vals.p_4 = p_4
                vals.p_4.CPU = True
                vals.plays.append(vals.p_4)
            vals.player += 1

        if vals.P3 is True:
            vals.P3 = False
            if vals.player == 2:
                p_2 = Players(3, vals.player, file)
                p_2.set_start_val()
                vals.p_2 = p_2
                vals.p_2.CPU = True
                vals.plays.append(vals.p_2)
            elif vals.player == 3:
                p_3 = Players(3, vals.player, file)
                p_3.set_start_val()
                vals.p_3 = p_3
                vals.p_3.CPU = True
                vals.plays.append(vals.p_3)
            elif vals.player == 4:
                p_4 = Players(3, vals.player, file)
                p_4.set_start_val()
                vals.p_4 = p_4
                vals.p_4.CPU = True
                vals.plays.append(vals.p_4)
            vals.player += 1

        if vals.P4 is True:
            vals.P4 = False
            if vals.player == 2:
                p_2 = Players(4, vals.player, file)
                p_2.set_start_val()
                vals.p_2 = p_2
                vals.p_2.CPU = True
                vals.plays.append(vals.p_2)
            elif vals.player == 3:
                p_3 = Players(4, vals.player, file)
                p_3.set_start_val()
                vals.p_3 = p_3
                vals.p_3.CPU = True
                vals.plays.append(vals.p_3)
            elif vals.player == 4:
                p_4 = Players(4, vals.player, file)
                p_4.set_start_val()
                vals.p_4 = p_4
                vals.p_4.CPU = True
                vals.plays.append(vals.p_4)
            vals.player += 1


def print_info(scrn, pygame, file, vals):
    scrn.fill(vals.current)
    render_images(pygame, file.title, scrn, (500, 100), (650, 5))
    pygame.draw.rect(scrn, (0, 0, 0), pygame.Rect(97, 97, 86, 121))
    pygame.draw.rect(scrn, (0, 0, 0), pygame.Rect(97, 247, 86, 121))
    pygame.draw.rect(scrn, (0, 0, 0), pygame.Rect(97, 397, 86, 121))
    pygame.draw.rect(scrn, (0, 0, 0), pygame.Rect(97, 447, 86, 121))

    imp = pygame.image.load(file.map)
    imp = pygame.transform.scale(imp, (800, 800))
    subsurface = imp.subsurface((525, 685, 80, 115))
    scrn.blit(subsurface, (100, 100))
    subsurface2 = imp.subsurface((198, 685, 80, 115))
    scrn.blit(subsurface2, (100, 250))

    render_text(vals.font2, scrn, f'When you land on a launchpad tile, you will move 1-6 additional spaces!', (245, 245, 245), (575, 157))
    render_text(vals.font2, scrn, f'When you land on a chest tile,  you will gain materials!',(245, 245, 245), (495, 307))
    render_text(vals.font2, scrn, f'The game will end when one person is left standing!', (245, 245, 245),(481, 457))
    render_text(vals.font2, scrn, f'If the game reaches over 100 turns, there will be a final heal off!', (245, 245, 245), (535, 607))
    render_text(vals.font1, scrn, f'Rules: ', (245, 245, 245),(163, 50))
    render_text(vals.font1, scrn, f'Return to Game', (245, 245, 245), (200, 735))

def print_settings(scrn, pygame, file, vals):
    scrn.fill(vals.current)
    render_images(pygame, file.title, scrn, (500, 100), (650, 5))
    pygame.draw.rect(scrn, (220, 220, 90), pygame.Rect(125, 125, 950, 550))
    pygame.draw.rect(scrn, (220, 220, 20), pygame.Rect(150, 150, 900, 500))

    render_text(vals.font1, scrn, 'Screen size:', (245, 245, 245), (300, 200))

    render_text(vals.font3, scrn, '1200x800', (245, 245, 245), (600, 200))
    render_text(vals.font3, scrn, '1800x900', (245, 245, 245), (800, 200))

    render_text(vals.font1, scrn, 'Volume:', (245, 245, 245), (258, 300))

    i = 0
    while i <= 100:
        render_text(vals.font1, scrn, f'{i}', (245, 245, 245), (370 + 5*i, 300))
        i+=20

    render_text(vals.font1, scrn, 'Screen Mode:', (245, 245, 245), (315, 400))
    render_text(vals.font1, scrn, 'Light Mode', (245, 245, 245), (600, 400))
    render_text(vals.font1, scrn, 'Dark Mode', (245, 245, 245), (900, 400))

    render_text(vals.font1, scrn, f'Return to Game', (245, 245, 245), (200, 735))

def print_dice(pygame, scrn, vals):
    if vals.GAME:
        if vals.DICE:
            pygame.draw.rect(scrn, vals.current, pygame.Rect(865, 50, 335, 800))
            pygame.draw.rect(scrn, (0, 0, 0), pygame.Rect(875, 50, 300, 700))
            if (890 < vals.mx < 1175) and (73 < vals.my < 750):
                scrn.blit(vals.dice1, (vals.mx - 25, vals.my - 25))
                scrn.blit(vals.dice2, (vals.mx + 25, vals.my + 25))

            # moves dice to default spot if the mouse is not within the roll box
            else:
                scrn.blit(vals.dice1, (1060, 675))
                scrn.blit(vals.dice2, (1110, 675))

                # sets the text size and location, and prints the Dice label
                render_text(vals.font1, scrn, f'Dice:', (245, 245, 245), (960, 700))

        elif vals.DOUBLES:
            pygame.draw.rect(scrn, vals.current, pygame.Rect(865, 50, 335, 800))
            pygame.draw.rect(scrn, (0, 0, 0), pygame.Rect(875, 50, 300, 700))
            if (890 < vals.mx < 1175) and (73 < vals.my < 750):
                scrn.blit(vals.dice1, (vals.mx - 25, vals.my - 25))
                scrn.blit(vals.dice2, (vals.mx + 25, vals.my + 25))

            else:
                # moves dice to default spot if the mouse is not within the roll box
                render_text(vals.font1, scrn, f'You Rolled {vals.num1 + vals.num2}!', (245, 245, 245), (1025, 700))

def print_board(scrn, pygame, file, vals, board):
    #fills the screen to blue
    scrn.fill(vals.current)

    #draws the rectangles
    pygame.draw.rect(scrn, (0,0,0), pygame.Rect(130, 130, 540, 540))
    pygame.draw.rect(scrn, (0,0,0), pygame.Rect(875, 50, 300, 700))
    pygame.draw.rect(scrn, (0,0,0), pygame.Rect(265, 675, 390, 100))
    pygame.draw.rect(scrn, (0,0,0), pygame.Rect(25, 265, 100, 390))
    pygame.draw.rect(scrn, (0,0,0), pygame.Rect(675, 265, 100, 390))
    pygame.draw.rect(scrn, (0,0,0), pygame.Rect(265, 25, 390, 100))

    render_text(vals.font2, scrn, f'Settings', (245, 245, 245), (50, 30))
    render_text(vals.font2, scrn, f'Info', (245, 245, 245), (50, 60))

    render_images(pygame, file.map, scrn, (500, 500), (150, 150))

    #displays player 1's information
    def process(p):
        for i in range(4):
            num = p.num
            if num == 1:
                p.p1_out(vals, scrn, pygame)
            elif num == 2:
                p.p2_out(vals, scrn, pygame)
            elif num == 3:
                p.p3_out(vals, scrn, pygame)
            elif num == 4:
                p.p4_out(vals, scrn, pygame)

    process(vals.plays[0])
    process(vals.plays[1])
    process(vals.plays[2])
    process(vals.plays[3])

    render_text_with_bg(vals.font3, scrn, f'{vals.plays[vals.player-1].name}\'s turn', (245, 245, 245),vals.plays[vals.player-1].color, (775, 25))

    if vals.plays[vals.player-1].jail:
        render_text(vals.font1, scrn, 'Next Turn:', (245, 245, 245), (1025, 25))

    if vals.DICE:
        pass

    # if the previous dice were doubles
    elif vals.DOUBLES:

        # Displays the sum of the numbers rolled as well as that they were doubles
        render_text(vals.font1, scrn, f'Doubles {vals.num1 + vals.num2}!', (245, 245, 245), (1000, 630))

        # sets the text size and location, and prints the Dice label
        render_text(vals.font1, scrn, f'Dice:', (245, 245, 245), (960, 700))

        # displays the Roll Again button if the player can roll after had rolling doubles
        render_text(vals.font1, scrn, 'Roll Again:', (245, 245, 245), (1025, 25))

    else:
        # Displays the sum of the numbers rolled
        render_text(vals.font1, scrn, f'You Rolled {vals.num1 + vals.num2}!', (245, 245, 245), (1025, 700))

        # displays the Next Turn button if the player can roll

        render_text(vals.font1, scrn, 'Next Turn:', (245, 245, 245), (1025, 25))

    if board[vals.plays[vals.player-1].space].buyable and board[vals.plays[vals.player-1].space] not in vals.plays[vals.player-1].inventory:
        if vals.plays[vals.player-1].money > board[vals.plays[vals.player-1].space].price:
            render_text_with_bg(vals.font1, scrn, f'Purchase', (245, 245, 245), (0, 0, 0), (760, 720))

    if board[vals.plays[vals.player - 1].space].name == 'Jail' and vals.plays[vals.player - 1].jail:
        if vals.plays[vals.player - 1].money >= 50:
            render_text_with_bg(vals.font1, scrn, f'Pay 50', (245, 245, 245), (0, 0, 0), (760, 720))

    render_images(pygame, file.materials, scrn, (50, 30), (260, 695))
    render_images(pygame, file.materials, scrn, (50, 30), (20, 265))
    render_images(pygame, file.materials, scrn, (50, 30), (260, 45))
    render_images(pygame, file.materials, scrn, (50, 30), (670, 265))

    for spaces in board:
        spaces.print_owner(pygame, scrn)

    if vals.P1:
        render_circle(vals.plays[0], scrn, pygame)
    else:
        pygame.draw.rect(scrn, (0,0,0), pygame.Rect(265, 675, 390, 100))
    if vals.P2:
        render_circle(vals.plays[1], scrn, pygame)
    else:
        pygame.draw.rect(scrn, (0,0,0), pygame.Rect(25, 265, 100, 390))
    if vals.P3:
        render_circle(vals.plays[2], scrn, pygame)
    else:
        pygame.draw.rect(scrn, (0,0,0), pygame.Rect(265, 25, 390, 100))
    if vals.P4:
        render_circle(vals.plays[3], scrn, pygame)
    else:
        pygame.draw.rect(scrn, (0,0,0), pygame.Rect(675, 265, 100, 390))

    render_text(vals.font2, scrn, f'Turn {vals.nums_of_turns}', (245, 245, 245), (75, 725))

def print_win(scrn, vals, pygame, file, mixer):
        scrn.fill(vals.current)

        render_images(pygame, file.win, scrn, (400, 100), (750, 5))
        render_images(pygame, vals.winner.img, scrn, (300, 300), (100, 100))

def print_easter_egg(file, scrn, pygame, vals):
    pygame.draw.rect(scrn, vals.current, pygame.Rect(1175, 100, 400, 800))

    render_images(pygame, file.dance, scrn, (150, 150), (1600, 0))

    render_images(pygame, file.goofy_laugh, scrn, (150, 150), (1600, 150))

    render_images(pygame, file.hitmarker, scrn, (150, 150), (1600, 300))

    render_images(pygame, file.fall, scrn, (150, 150), (1600, 450))

    render_images(pygame, file.cat, scrn, (150, 150),(1600, 600))

    render_images(pygame, file.cricket, scrn, (150, 150), (1600, 750))