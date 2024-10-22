class Players:

    def __init__(self, num, p, file):
        self._order = num
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
        self.set_playa(num, file)
        self._space = 0

    # returns the name of the player
    @property
    def order(self):
        return self._order

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

    @property
    def space(self):
        return self._space

    @space.setter
    def space(self, value):
        if value > 31:
            self._space = value - 32
            self.wood += 200
        else:
            self._space = value

    # sets the name of the player depending on what icon they chose
    def set_playa(self, num, file):
        if num == 1:
            self.name = "Nog Ops"
            self.color = 89, 211, 227
            self.img = file.nog_ops
        if num == 2:
            self.name = "Jonesy"
            self.color = 219, 31, 62
            self.img = file.jonesy

        if num == 3:
            self.name = "Raven"
            self.color = 137, 42, 156
            self.img = file.raven

        if num == 4:
            self.name = "John Wick"
            self.color = 82, 82, 82
            self.img = file.john_wick

    def set_start_val(self):
        if self._num == 1:
            self.loc_x = 605
            self.loc_y = 605
        if self._num == 2:
            self.loc_x = 605
            self.loc_y = 625
        if self._num == 3:
            self.loc_x = 625
            self.loc_y = 605
        if self._num == 4:
            self.loc_x = 625
            self.loc_y = 625

    def render_output(self, text_center, img_pos, mats_x_y, bool, vals, scrn, pygame):
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

    def p1_out(self, vals, scrn, pygame):
        self.render_output((195, 787), (145, 675), (425, 725), False, vals, scrn, pygame)

    def p2_out(self, vals, scrn, pygame):
        self.render_output((75, 130), (25, 145), (175, 375), True, vals, scrn, pygame)

    def p3_out(self, vals, scrn, pygame):
        self.render_output((195, 13), (145, 25), (425, 75), False, vals, scrn, pygame)

    def p4_out(self, vals, scrn, pygame):
        self.render_output((725, 130), (675, 145), (825, 375), True, vals, scrn, pygame)

    def render_circle(self, scrn, pygame):
        pygame.draw.circle(scrn, self.color, [self.loc_x, self.loc_y], 10, 0)
