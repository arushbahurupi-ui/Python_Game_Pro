import pygame

pygame.init()

screen = pygame.display.set_mode((1600,800))

class Ball():
    def __init__(self, color, pos_x, pos_y, rad, width):
        self.color = color
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.rad = rad
        self.width = width


    def draw(self):
        pygame.draw.circle(screen, self.color, (self.pos_x, self.pos_y), self.rad, self.width)

    def move(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_w] and self.pos_y - self.rad >= 0:
            self.pos_y -= 3
        if key[pygame.K_s] and self.pos_y + self.rad <= 800:
            self.pos_y += 3
        if key[pygame.K_a] and self.pos_x - self.rad >= 0:
            self.pos_x -= 3
        if key[pygame.K_d] and self.pos_x + self.rad <= 1600:
            self.pos_x += 3

class Square():
    def __init__(self, color, pos_x, pos_y, height, width):
        self.color = color
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.height = height
        self.width = width


    def draw(self):
        pygame.draw.rect(screen, self.color, (self.pos_x, self.pos_y, self.height, self.width))

    def move(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_UP] and self.pos_y - self.height >= 0:
            self.pos_y -= 3
        if key[pygame.K_DOWN] and self.pos_y + self.height <= 800:
            self.pos_y += 3
        if key[pygame.K_LEFT] and self.pos_x - self.height >= 0:
            self.pos_x -= 3
        if key[pygame.K_RIGHT] and self.pos_x + self.height <= 1600:
            self.pos_x += 3


ball1 = Ball("white", 800, 400, 50, 0)
square1 = Square("white", 800, 400, 50, 50)

while True:
    screen.fill("gray")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    ball1.draw()
    ball1.move()
    square1.draw()
    square1.move()
    pygame.display.update()

