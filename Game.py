import pygame
import random

pygame.init()

screen = pygame.display.set_mode((500,500))

x_random = random.randint(50,450)
y_random = random.randint(50,450)

class Pointer():
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
        if key[pygame.K_s] and self.pos_y + self.rad <= 500:
            self.pos_y += 3
        if key[pygame.K_a] and self.pos_x - self.rad >= 0:
            self.pos_x -= 3
        if key[pygame.K_d] and self.pos_x + self.rad <= 500:
            self.pos_x += 3

pointer = Pointer("white", 400, 400, 20, 0)

print(x_random)
print(y_random)

while True:
    screen.fill("gray")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    distance = ((pointer.pos_x - x_random) ** 2 + (pointer.pos_y - y_random) ** 2) ** 0.5
    if distance < pointer.rad:
        print("You found the point")
        pygame.quit()
        exit()
    pointer.draw()
    pointer.move()
    pygame.display.update()
