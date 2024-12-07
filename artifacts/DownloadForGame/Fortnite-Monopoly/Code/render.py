def render_images(pygame, file, scrn, dimensions, location):
    start_but = pygame.image.load(file)
    start_but = pygame.transform.scale(start_but, dimensions)
    scrn.blit(start_but, location)

def render_text(font, scrn, text, color, location):
    text = font.render(text, True, color)
    textRect = text.get_rect()
    textRect.center = location
    scrn.blit(text, textRect)

def render_text_with_bg(font, scrn, text, color, bg_color, location):
    text = font.render(text, True, color, bg_color)
    textRect = text.get_rect()
    textRect.center = location
    scrn.blit(text, textRect)

def render_circle(player, scrn, pygame):
    if player.space == 8 and player.jail:
        player.loc_x = 170 + 10*player.num
        player.loc_y = 585 + 10*player.num
        pygame.draw.circle(scrn, player.color, [player.loc_x, player.loc_y], 10, 0)
    else:
        pygame.draw.circle(scrn, player.color, [player.loc_x, player.loc_y], 10, 0)