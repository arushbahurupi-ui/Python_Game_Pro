import pygame
import random

pygame.init()
screen = pygame.display.set_mode((1600, 800))
background = pygame.image.load("images/images-2.jpeg")
background = pygame.transform.scale(background, (1600, 800))
original_flower = pygame.image.load("images/flower.png")
original_flower = pygame.transform.scale(original_flower, (100, 100))
flower = original_flower

y_f = -100
y_f2 = 800
x_f = -100
x_f2 = 1600

particles = []

for i in range(150):

    particles.append([
        random.randint(0, 1600),
        random.randint(0, 800),
        random.uniform(-1, 1),
        random.uniform(-1, 1),
        random.randint(1, 4)
    ])

def draw_particles():

    for p in particles:
        p[0] += p[2]
        p[1] += p[3]
        if p[0] < 0:
            p[0] = 1600
        if p[0] > 1600:
            p[0] = 0
        if p[1] < 0:
            p[1] = 800
        if p[1] > 800:

            p[1] = 0

        pygame.draw.circle(screen, (255, 255, 255),
                           (int(p[0]), int(p[1])), p[4])

def animation():

    global y_f, y_f2, x_f, x_f2
    for i in range(16):
        screen.blit(flower, (i * 100, y_f))
    y_f += 2
    for i in range(16):
        screen.blit(flower, (i * 100, y_f2))
    y_f2 -= 2
    for i in range(8):
        screen.blit(flower, (x_f, i * 100))
    x_f += 4
    for i in range(8):
        screen.blit(flower, (x_f2, i * 100))
    x_f2 -= 4

angle = 0
clock = pygame.time.Clock()

running = True
while running:

    screen.blit(background, (0, 0))
    angle += 2
    flower = pygame.transform.rotate(original_flower, angle)
    animation()

    if x_f >= 1600:
        y_f = -100
        y_f2 = 800
        x_f = -100
        x_f2 = 1600
    draw_particles()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
    clock.tick(60)

pygame.quit()
