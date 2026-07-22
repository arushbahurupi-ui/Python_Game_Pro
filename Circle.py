import pygame

pygame.init()

screen = pygame.display.set_mode((1600,800))

list_circle = []



class circle():
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
        if key[pygame.K_d] and self.pos_x + self.rad <= 1600:
            self.pos_x += 3
        if key[pygame.K_a] and self.pos_x - self.rad >= 0:
            self.pos_x -= 3





pointer = circle("white", 800, 400, 20, 0)



while True:
    screen.fill("gray")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                circle_d = circle("white", pointer.pos_x, pointer.pos_y, 65, 0)
                list_circle.append(circle_d)
    for circles in list_circle:
        circles.draw()
    pointer.draw()
    pointer.move()
    pygame.display.update()
