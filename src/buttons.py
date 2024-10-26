from print_screens import print_board


def start_button(vals):
    if (450 < vals.mx < 750) and (450 < vals.my < 570):
        # TEST FOR WHEN THE START BUTTON HAS BEEN PRESSED
        print("You clicked start")
        vals.START = False
        vals.SELEC = True

def icon_nog_ops(vals, Players, file):
    if (100 < vals.mx < 400) and (100 < vals.my < 400) and vals.P1:
        # declares that P1 can no longer be used and increases whose turn it is to choose by 1
        vals.P1 = False
        p_1 = Players(1, vals.player, file)
        p_1.set_start_val()
        vals.p_1 = p_1
        vals.player += 1
        vals.plays.append(p_1)

def icon_jonesy(vals, Players, file):
    if (800 < vals.mx < 1100) and (100 < vals.my < 400) and vals.P2:
        # declares that P2 can no longer be used and increases whose turn it is to choose by 1
        vals.P2 = False
        p_2 = Players(2, vals.player, file)
        p_2.set_start_val()
        vals.p_2 = p_2
        vals.player += 1
        vals.plays.append(p_2)

def icon_raven(vals, Players, file):
    if (100 < vals.mx < 400) and (450 < vals.my < 750) and vals.P3:
        # declares that P3 can no longer be used and increases whose turn it is to choose by 1
        vals.P3 = False
        p_3 = Players(3, vals.player, file)
        p_3.set_start_val()
        vals.p_3 = p_3
        vals.player += 1
        vals.plays.append(p_3)

def icon_john_wick(vals, Players, file):
    if (800 < vals.mx < 1100) and (450 < vals.my < 750) and vals.P4:
        # declares that P4 can no longer be used and increases whose turn it is to choose by 1
        vals.P4 = False
        p_4 = Players(4, vals.player, file)
        p_4.set_start_val()
        vals.p_4 = p_4
        vals.player += 1
        vals.plays.append(p_4)

def icons(vals, Players, file):
    icon_nog_ops(vals, Players, file)
    # if P2 icon is clicked while it is still available
    icon_jonesy(vals, Players, file)
    # if P3 icon is clicked while it is still available
    icon_raven(vals, Players, file)
    # if P4 icon is clicked while it is still available
    icon_john_wick(vals, Players, file)

def continue_button(vals):
    if (510 < vals.mx < 690) and (480 < vals.my < 510) and vals.player == 5:
        # TEST FOR WHEN THE CONTINUE BUTTON HAS BEEN CLICKED
        print("You clicked start Again")
        vals.SELEC = False
        vals.GAME = True
        vals.player = 1
        vals.P1 = True
        vals.P2 = True
        vals.P3 = True
        vals.P4 = True

def return_to_game(scrn, pygame, file, vals, board):
    if (50 < vals.mx < 352) and (715 < vals.my < 750):
        vals.INFO = False
        vals.GAME = True
        print_board(scrn, pygame, file, vals, board)

def info_button(vals):
    if (20 < vals.mx < 80) and (15 < vals.my < 40):
        vals.GAME = False
        vals.INFO = True

def roll_dice(vals, mixer, file, pygame, board, random):
    if (875 < vals.mx < 1175) and (50 < vals.my < 750) and vals.DICE:
        # declares that the player just rolled
        vals.DICE = False
        vals.DOUBLES = False
        vals.ROLLING = True

        mixer.music.load(file.roll_effect)
        pygame.mixer.music.queue(file.music)
        mixer.music.play()

        current_player = vals.plays[vals.player - 1]
        current_player.space += vals.num1 + vals.num2

        print(f'{current_player.name} on space: {board[current_player.space].name}')
        if board[current_player.space].name == "Launchpad":
            current_player.space += random.randint(1, 6)
            print(f'You jumped! to {board[current_player.space].name}')

        if board[current_player.space].name == "Go To Jail":
            current_player.space = 8
            print("You go to jail now!")

        if board[current_player.space].name == "Chest":
            current_player.money -= board[current_player.space].price
            print(f'You gained {-board[current_player.space].price} materials!')

        for p in range(0,3):
            owner = vals.plays[p]
            if board[current_player.space] in owner.inventory and owner != current_player:
                if current_player.money - board[current_player.space].price >= 0:
                    #owner.money += board[current_player.space].price
                    current_player.money -= board[current_player.space].price
                    print(f'{current_player.name} paid {owner.name} {board[current_player.space].price}')
                else:
                    current_player.health -= 50
                    if current_player.health <= 0:
                        if current_player == vals.plays[0]:
                            vals.P1 = False
                        elif current_player == vals.plays[1]:
                            vals.P2 = False
                        elif current_player == vals.plays[2]:
                            vals.P3 = False
                        elif current_player == vals.plays[3]:
                            vals.P4 = False
                        for stuff in current_player.inventory:
                            owner.add_to_inventory(stuff)
                        current_player.inventory = []
                        mixer.music.load(file.death)
                        pygame.mixer.music.queue(file.music)
                        mixer.music.play()
                        print(f'{current_player.name} died :(')
                    print(f'{current_player.name} took 50 damage')
        def check_for_win():
            if vals.P1 and not vals.P2 and not vals.P3 and not vals.P4:
                print()
                print(f'{vals.plays[0].name} WON!')
                print()
                vals.winner = vals.plays[0]
                vals.WIN = True
                mixer.music.load(file.death)
                pygame.mixer.music.queue(file.music)
                mixer.music.play()
            elif not vals.P1 and vals.P2 and not vals.P3 and not vals.P4:
                print()
                print(f'{vals.plays[1].name} WON!')
                print()
                vals.winner = vals.plays[1]
                vals.WIN = True
            elif not vals.P1 and not vals.P2 and vals.P3 and not vals.P4:
                print()
                print(f'{vals.plays[2].name} WON!')
                print()
                vals.winner = vals.plays[2]
                vals.WIN = True
            elif not vals.P1 and not vals.P2 and not vals.P3 and vals.P4:
                print()
                print(f'{vals.plays[3].name} WON!')
                print()
                vals.winner = vals.plays[3]
                vals.WIN = True
        check_for_win()

        if current_player.num == 1:
            current_player.loc_x = board[current_player.space].loc1_x
            current_player.loc_y = board[current_player.space].loc1_y

        elif current_player.num == 2:
            current_player.loc_x = board[current_player.space].loc2_x
            current_player.loc_y = board[current_player.space].loc2_y

        elif current_player.num == 3:
            current_player.loc_x = board[current_player.space].loc3_x
            current_player.loc_y = board[current_player.space].loc3_y

        elif current_player.num == 4:
            current_player.loc_x = board[current_player.space].loc4_x
            current_player.loc_y = board[current_player.space].loc4_y

def check_doubles(vals):
    if (875 < vals.mx < 1175) and (50 < vals.my < 750) and vals.num1 == vals.num2:
        # declares that the player has doubles
        vals.DOUBLES = True
        vals.DICE = False
        vals.ROLLING = False

    elif (875 < vals.mx < 1175) and (50 < vals.my < 750) and vals.DOUBLES:
        vals.DOUBLES = False
        vals.DICE = True
        vals.ROLLING = False

def next_turn(vals, random):
    if (920 < vals.mx < 1130) and (5 < vals.my < 45) and not vals.DICE and not vals.DOUBLES:
        vals.DICE = True
        vals.DOUBLES = False
        vals.num1 = random.randint(1, 6)
        vals.num2 = random.randint(1, 6)
        vals.player += 1
        if vals.player > 4:
            vals.player -= 4
        if not vals.P1 and vals.player == 1:
            vals.player = 2
        if not vals.P2 and vals.player == 2:
            vals.player = 3
        if not vals.P3 and vals.player == 3:
            vals.player = 4
        if not vals.P4 and vals.player == 4:
            vals.player = 1
        if not vals.P1 and vals.player == 1:
            vals.player = 2


def roll_again(vals, random):
    if (920 < vals.mx < 1130) and (5 < vals.my < 45):
        # resets the rolling values to allow the next turn
        vals.DICE = True
        vals.DOUBLES = False
        vals.num1 = random.randint(1, 6)
        vals.num2 = random.randint(1, 6)

def purchase(vals, board):
    if board[vals.plays[vals.player - 1].space].buyable and board[vals.plays[vals.player - 1].space] not in vals.plays[vals.player - 1].inventory:
        if (669 < vals.mx < 852) and (700 < vals.my < 740):
            vals.plays[vals.player - 1].add_to_inventory(board[vals.plays[vals.player - 1].space])
            board[vals.plays[vals.player - 1].space].buyable = False
            vals.plays[vals.player - 1].money -= board[vals.plays[vals.player - 1].space].price
            print(f'{vals.plays[vals.player - 1].name} bought {board[vals.plays[vals.player - 1].space].name} for {board[vals.plays[vals.player - 1].space].price}')
