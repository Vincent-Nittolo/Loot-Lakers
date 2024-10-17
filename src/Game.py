#import the necessary libraries
import pygame
from pygame import mixer, MOUSEBUTTONUP, MOUSEBUTTONDOWN
import random
from values import Values

#initializes the game and declares values of X and Y
pygame.init()
X = 1200
Y = 800

#creates the screen, and sets the width to X and the height to Y
scrn = pygame.display.set_mode((X, Y))

#values that determine the current stage of the game
vals = Values()
vals._font1 = pygame.font.Font('freesansbold.ttf', 40)
vals._font2 = pygame.font.Font('freesansbold.ttf', 20)
vals._font3 = pygame.font.Font('freesansbold.ttf', 30)


class Players:

    def __init__(self, num, p):
        self._num = num
        self._wood = 300
        self._brick = 200
        self._metal = 100
        self._loc_x = 0
        self._loc_y = 0
        self._num = p
        self._icon_x = 0
        self._icon_y = 0
        self._name_text_x = 0
        self._name_text_y = 0
        self._name = "Placeholder"
        self._color = 0, 0, 0
        self._img = "Placeholder"
        self.set_playa(num)

    # returns the name of the player
    @property
    def wood(self):
        return self._wood

    @wood.setter
    def wood(self, value):
        self._wood = value

    @property
    def brick(self):
        return self._brick

    @brick.setter
    def brick(self, value):
        self._brick = value

    @property
    def metal(self):
        return self._metal

    @metal.setter
    def metal(self, value):
        self._metal = value

    @property
    def name(self):
        return self._name

    @property
    def loc_x(self):
        return self._loc_x

    @loc_x.setter
    def loc_x(self, value):
        self._loc_x = value

    @property
    def loc_y(self):
        return self._loc_y

    @loc_y.setter
    def loc_y(self, value):
        self._loc_y = value

    @property
    def num(self):
        return self._num

    @property
    def name_text_x(self):
        return self._name_text_x

    @name_text_x.setter
    def name_text_x(self, value):
        self._name_text_x = value

    @property
    def name_text_y(self):
        return self._name_text_y

    @name_text_y.setter
    def name_text_y(self, value):
        self._name_text_y = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value

    @property
    def img(self):
        return self._img

    @img.setter
    def img(self, value):
        self._img = value

    # sets the name of the player depending on what icon they chose
    def set_playa(self, num):
        if num == 1:
            self.name = "Nog Ops"
            self.color = 89, 211, 227
            self.img = "C:\\Users\\vinny\\Downloads\\nog_ops.jpg"
        if num == 2:
            self.name = "Jonesy"
            self.color = 219, 31, 62
            self.img = "C:\\Users\\vinny\\Downloads\\jonesy.jpg"

        if num == 3:
            self.name = "Raven"
            self.color = 137, 42, 156
            self.img = "C:\\Users\\vinny\\Downloads\\Raven.jpg"

        if num == 4:
            self.name = "John Wick"
            self.color = 82, 82, 82
            self.img = "C:\\Users\\vinny\\Downloads\\John_wick.jpg"

    def render_output(self, text_center, img_pos, mats_x_y, bool):
        text = vals.font2.render(f'{self.name} {self.num}', True, (245, 245, 245))
        textRect = text.get_rect()
        textRect.center = text_center
        scrn.blit(text, textRect)
        img = pygame.image.load(self.img)
        img = pygame.transform.scale(img, (100, 100))
        scrn.blit(img, img_pos)
        text = vals.font1.render(f'{self.wood} {self.brick} {self._metal}!', True, (245, 245, 245))
        textRect = text.get_rect()
        textRect.center = (mats_x_y)
        if bool:
            text = pygame.transform.rotate(text, 90)
        scrn.blit(text, textRect)

    def p1_out(self):
        self.render_output((195, 787), (145, 675), (425, 725), False)

    def p2_out(self):
        self.render_output((75, 130), (25, 145), (175, 375), True)

    def p3_out(self):
        self.render_output((195, 13), (145, 25), (425, 75), False)

    def p4_out(self):
        self.render_output((725, 130), (675, 145), (825, 375), True)

    def render_circle(self):
        pygame.draw.circle(scrn, self.color, [self.loc_x, self.loc_y], 10, 0)

class Spaces:

    def __init__(self, name, x, y):
        self.name = name
        self.loc_1_x = x
        self.loc_2_x = self.loc_1_x + 20
        self.loc_3_x = self.loc_1_x
        self.loc_4_x = self.loc_1_x + 20
        self.loc_1_y = y
        self.loc_2_y = self.loc_1_y + 20
        self.loc_3_y = self.loc_1_y
        self.loc_4_y = self.loc_1_y + 20

    def get_loc1_x(self):
        return self.loc_1_x
    def get_loc2_x(self):
        return self.loc_2_x
    def get_loc3_x(self):
        return self.loc_3_x
    def get_loc4_x(self):
        return self.loc_4_x
    def get_loc1_y(self):
        return self.loc_1_y
    def get_loc2_y(self):
        return self.loc_2_y
    def get_loc3_y(self):
        return self.loc_3_y
    def get_loc4_y(self):
        return self.loc_4_y

board = [Spaces]
go = Spaces('Go', 605, 605)
next_space = Spaces('Next Space', 535, 605)
board.append(go)
board.append(next_space)

#declares Player Class, that contains info of each of the 4 players


#prints the images that make the starting screen
def print_start():

    #fills the screen to blue
    scrn.fill((27, 144, 221))

    # sets imp to the image of the board, and declares its size
    start_but = pygame.image.load("C:\\Users\\vinny\\Downloads\\start_button.jpg")
    start_but = pygame.transform.scale(start_but, (300, 120))
    scrn.blit(start_but, (450, 450))

    #sets imp to the image of the board, and declares its size and location
    title = pygame.image.load("C:\\Users\\vinny\\Downloads\\Title_text.png")
    title = pygame.transform.scale(title, (900, 200))
    scrn.blit(title, (150, 150))

def print_selec():

    #fills the screen to blue
    scrn.fill((27, 144, 221))

    #creates the selection screen text
    title = pygame.image.load("C:\\Users\\vinny\\Downloads\\Title_text.png")
    title = pygame.transform.scale(title, (400, 100))
    scrn.blit(title, (750, 5))

    #tells the user whose turn it is to choose a player
    if vals.player <5:
        text = vals.font1.render(f'Player {vals.player} Choose:', True, (245, 245, 245))
        textRect = text.get_rect()
        textRect.center = (200, 50)
        scrn.blit(text, textRect)

    #the user is told to continue when all players are selected
    else:
        text = vals.font1.render(f'Please Continue!', True, (245, 245, 245))
        textRect = text.get_rect()
        textRect.center = (200, 50)
        scrn.blit(text, textRect)

        text = vals.font1.render(f'Continue', True, (245, 245, 245))
        textRect = text.get_rect()
        textRect.center = (600, 500)
        scrn.blit(text, textRect)

    #only shows the icons when they have not been selected yet
    def display_selec_icons():
        if vals.P1:
            nog_ops = pygame.image.load("C:\\Users\\vinny\\Downloads\\nog_ops.jpg")
            nog_ops = pygame.transform.scale(nog_ops, (300, 300))
            scrn.blit(nog_ops, (100, 100))

        if vals.P2:
            jonesy = pygame.image.load("C:\\Users\\vinny\\Downloads\\jonesy.jpg")
            jonesy = pygame.transform.scale(jonesy, (300, 300))
            scrn.blit(jonesy, (800, 100))

        if vals.P3:
            raven = pygame.image.load("C:\\Users\\vinny\\Downloads\\Raven.jpg")
            raven = pygame.transform.scale(raven, (300, 300))
            scrn.blit(raven, (100, 450))

        if vals.P4:
            j_wick = pygame.image.load("C:\\Users\\vinny\\Downloads\\John_wick.jpg")
            j_wick = pygame.transform.scale(j_wick, (300, 300))
            scrn.blit(j_wick, (800, 450))
    display_selec_icons()

#declares the function print_board, that will print all images for board
def print_board():

    #fills the screen to blue
    scrn.fill((27, 144, 221))

    #draws the rectangles
    def recs():
        pygame.draw.rect(scrn, (0,0,0), pygame.Rect(145, 145, 510, 510))
        pygame.draw.rect(scrn, (0,0,0), pygame.Rect(875, 50, 300, 700))
        pygame.draw.rect(scrn, (0,0,0), pygame.Rect(145, 675, 510, 100))
        pygame.draw.rect(scrn, (0,0,0), pygame.Rect(25, 145, 100, 510))
        pygame.draw.rect(scrn, (0,0,0), pygame.Rect(675, 145, 100, 510))
        pygame.draw.rect(scrn, (0,0,0), pygame.Rect(145, 25, 510, 100))
    recs()

    #sets imp to the image of the board, and declares its size and location
    def map():
        imp = pygame.image.load("C:\\Users\\vinny\\Downloads\\Mappy .jpg").convert()
        imp = pygame.transform.scale(imp, (500, 500))
        scrn.blit(imp, (150, 150))
    map()

    #displays player 1's information
    def process(p):
        for i in range(4):
            num = p.num
            if num == 1:
                p.p1_out()
            elif num == 2:
                p.p2_out()
            elif num == 3:
                p.p3_out()
            elif num == 4:
                p.p4_out()

    process(p_1)
    process(p_2)
    process(p_3)
    process(p_4)

    text = vals.font3.render(f'{vals.plays[vals.player-1].name}\'s turn', True, (245, 245, 245), vals.plays[vals.player-1].color)
    textRect = text.get_rect()
    textRect.center = (775, 25)
    scrn.blit(text, textRect)
    vals.plays[0].render_circle()
    vals.plays[1].render_circle()
    vals.plays[2].render_circle()
    vals.plays[3].render_circle()

#sets the window name
pygame.display.set_caption('Fortnite Monopoly')

#starts the mixer, loads the Fortnite theme song, sets the volume, and plays the theme

mixer.init()
mixer.music.load("C:\\Users\\vinny\\Downloads\\01. Battle Royal (Guitar Theme).mp3")
mixer.music.set_volume(0.7)
mixer.music.play()

#paint screen one time
pygame.display.flip()

#loop for running the game until the window is closed
status = True
while (status):

    #iterate over the list of Event objects that was returned by pygame.event.get() method.
    for i in pygame.event.get():
        #stores the x and y values of the mouse
        mx, my = pygame.mouse.get_pos()
        dice1 = pygame.image.load("C:\\Users\\vinny\\Downloads\\dice.png")
        dice1 = pygame.transform.scale(dice1, (50, 50))

        # sets dice2 to the image of the dice, and declares its size and location
        dice2 = pygame.image.load("C:\\Users\\vinny\\Downloads\\dice.png")
        dice2 = pygame.transform.scale(dice2, (50, 50))
        #displays start screen if START is true

        if i.type == MOUSEBUTTONDOWN and i.button == 1:
            vals.clicking = True
            if vals.START:
                if (450 < mx < 750) and (450 < my < 570):
                    # TEST FOR WHEN THE START BUTTON HAS BEEN PRESSED
                    print("You clicked start")
                    vals.START = False
                    vals.SELEC = True


            if vals.SELEC:
                # if P1 icon is clicked while it is still available
                if (100 < mx < 400) and (100 < my < 400) and vals.P1:
                    # declares that P1 can no longer be used and increases whose turn it is to choose by 1
                    vals.P1 = False
                    print(vals.player)
                    p_1 = Players(1, vals.player)
                    p_1.loc_x = 605
                    p_1.loc_y = 605
                    vals.player += 1
                    vals.plays.append(p_1)

                # if P2 icon is clicked while it is still available
                if (800 < mx < 1100) and (100 < my < 400) and vals.P2:
                    # declares that P2 can no longer be used and increases whose turn it is to choose by 1
                    vals.P2 = False
                    print(vals.player)
                    p_2 = Players(2, vals.player)
                    p_2.loc_x = 625
                    p_2.loc_y = 605
                    vals.player += 1
                    vals.plays.append(p_2)

                # if P3 icon is clicked while it is still available
                if (100 < mx < 400) and (450 < my < 750) and vals.P3:
                    # declares that P3 can no longer be used and increases whose turn it is to choose by 1
                    vals.P3 = False
                    print(vals.player)
                    p_3 = Players(3, vals.player)
                    p_3.loc_x = 605
                    p_3.loc_y = 625
                    vals.player += 1
                    vals.plays.append(p_3)

                # if P4 icon is clicked while it is still available
                if (800 < mx < 1100) and (450 < my < 750) and vals.P4:
                    # declares that P4 can no longer be used and increases whose turn it is to choose by 1
                    vals.P4 = False
                    print(vals.player)
                    p_4 = Players(4, vals.player)
                    p_4.loc_x = 625
                    p_4.loc_y = 625
                    vals.player += 1
                    vals.plays.append(p_4)

        # if the continue button is clicked, enters the game screen
                if (510 < mx < 690) and (480 < my < 510) and vals.player == 5:
                    # TEST FOR WHEN THE CONTINUE BUTTON HAS BEEN CLICKED
                    print("You clicked start Again")
                    vals.SELEC = False
                    vals.GAME = True
                    vals.player = 1


            if vals.GAME:

                #Next Turn
                if (875 < mx < 1175) and (50 < my < 750) and vals.DICE:
                    # declares that the player just rolled
                    vals.DICE = False
                    vals.DOUBLES = False
                    vals.ROLLING = True
                    mixer.music.load("C:\\Users\\vinny\\Downloads\\dice-142528.mp3")
                    pygame.mixer.music.queue("C:\\Users\\vinny\\Downloads\\01. Battle Royal (Guitar Theme).mp3")
                    mixer.music.play()
                    x1 = vals.plays[vals.player-1].loc_x
                    y1 = vals.plays[vals.player-1].loc_y
                    for k in range(vals.num1 + vals.num2):
                        if ((vals.plays[vals.player-1].loc_x) - (52)) > 150 and vals.plays[vals.player-1].loc_y > 600:
                            vals.plays[vals.player-1].loc_x -= (52)

                        elif ((vals.plays[vals.player-1].loc_y) - (52)) > 150 and vals.plays[vals.player-1].loc_x < 200:
                            vals.plays[vals.player-1].loc_y -= (52)

                        elif ((vals.plays[vals.player-1].loc_x) + (52)) < 650 and vals.plays[vals.player-1].loc_y < 200:
                            vals.plays[vals.player-1].loc_x += (52)

                        elif ((vals.plays[vals.player-1].loc_y) + (52)) < 650 and vals.plays[vals.player-1].loc_x > 600:
                            vals.plays[vals.player-1].loc_y += (52)
                    x2 = vals.plays[vals.player-1].loc_x
                    y2 = vals.plays[vals.player-1].loc_y
                    if x1 > x2 and y1 < y2 or 575< y2 < 650 and 575 < x2 < 650:
                        vals.plays[vals.player - 1].wood += 200


                #Checks if the player rolls doubles
                if (875 < mx < 1175) and (50 < my < 750) and vals.num1 == vals.num2:
                    # declares that the player has doubles
                    vals.DOUBLES = True
                    vals.DICE = False
                    vals.ROLLING = False

                #player rolls again after double
                elif (875 < mx < 1175) and (50 < my < 750) and vals.DOUBLES:
                    vals.DOUBLES = False
                    vals.DICE = True
                    vals.ROLLING = False

                #Player presses next turn
                if (920 < mx < 1130) and (5 < my < 45) and not vals.DICE and not vals.DOUBLES:
                    vals.DICE = True
                    vals.DOUBLES = False
                    vals.num1 = random.randint(1, 6)
                    vals.num2 = random.randint(1, 6)
                    vals.player +=1
                    if vals.player == 5:
                        vals.player = 1

                #Player presses roll again
                if (920 < mx < 1130) and (5 < my < 45):
                    # resets the rolling values to allow the next turn
                    vals.DICE = True
                    vals.DOUBLES = False
                    vals.num1 = random.randint(1, 6)
                    vals.num2 = random.randint(1, 6)
            print(f'{mx} {my}')
            #print(f'DICE: {vals.DICE} DOUBLES: {vals.DOUBLES}')
        elif i.type == MOUSEBUTTONUP and i.button == 1:
            vals.clicking = False
            
        if vals.START:
            print_start()
        if vals.SELEC:
            print_selec()
        if vals.GAME:
            print_board()
            if vals.DICE:
                # moves the dice to follow the mouse if the mouse is within the roll box
                if (875 < mx < 1175) and (50 < my < 750):
                    scrn.blit(dice1, (mx - 25, my - 25))
                    scrn.blit(dice2, (mx + 25, my + 25))

                # moves dice to default spot if the mouse is not within the roll box
                else:
                    scrn.blit(dice1, (1060, 675))
                    scrn.blit(dice2, (1110, 675))

                    # sets the text size and location, and prints the Dice label
                    text = vals.font1.render('Dice:', True, (245, 245, 245), (0, 0, 0))
                    textRect = text.get_rect()
                    textRect.center = (960, 700)
                    scrn.blit(text, textRect)

            # if the previous dice were doubles
            elif vals.DOUBLES:
                # moves the dice to follow the mouse if the mouse is within the roll box
                if (875 < mx < 1175) and (50 < my < 750):
                    scrn.blit(dice1, (mx - 25, my - 25))
                    scrn.blit(dice2, (mx + 25, my + 25))

                else:
                    # moves dice to default spot if the mouse is not within the roll box
                    scrn.blit(dice1, (1060, 675))
                    scrn.blit(dice2, (1110, 675))

                # Displays the sum of the numbers rolled as well as that they were doubles
                text = vals.font1.render(f'Doubles {vals.num1 + vals.num2}!', True, (245, 245, 245))
                textRect = text.get_rect()
                textRect.center = (1000, 630)
                scrn.blit(text, textRect)

                # sets the text size and location, and prints the Dice label
                text = vals.font1.render('Dice:', True, (245, 245, 245))
                textRect = text.get_rect()
                textRect.center = (960, 700)
                scrn.blit(text, textRect)

                # displays the Roll Again button if the player can roll after had rolling doubles
                text = vals.font1.render('Roll Again:', True, (245, 245, 245))
                textRect = text.get_rect()
                textRect.center = (1025, 25)
                scrn.blit(text, textRect)

            else:
                # Displays the sum of the numbers rolled
                text = vals.font1.render(f'You Rolled {vals.num1 + vals.num2}!', True, (245, 245, 245))
                textRect = text.get_rect()
                textRect.center = (1025, 700)
                scrn.blit(text, textRect)

                # displays the Next Turn button if the player can roll
                text = vals.font1.render('Next Turn:', True, (245, 245, 245))
                textRect = text.get_rect()
                textRect.center = (1025, 25)
                scrn.blit(text, textRect)

        pygame.display.update()

        #if window is closed, the program ends
        if i.type == pygame.QUIT:
            status = False

#deactivates pygame library
pygame.quit()
