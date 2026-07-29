import pygame

pygame.init()

screen = pygame.display.set_mode((365,547))
y_f = -100

background = pygame.image.load("images/card.jpeg")
flower = pygame.image.load("images/flower.png")
flower = pygame.transform.scale(flower, (100,100))
cake = pygame.image.load("images/cake.png")
cake = pygame.transform.scale(cake, (190,205.83))

font = pygame.font.SysFont("Helvetica",  25)
font1 = pygame.font.SysFont("Helvetica",  20)

Text = font.render("HAPPY BIRTHDAY", True, "gold")
Text2 = font1.render("I WISH YOU A", True, "gold")
Text1 = font1.render("HAPPY BIRTHDAY", True, "gold")

while True:
    screen.blit(background, (0, 0))
    screen.blit(cake, (80, 140))
    screen.blit(Text, (70, 75))
    screen.blit(Text2, (105, 380))
    screen.blit(Text1, (90, 410))
    screen.blit(flower, (130, y_f))
    y_f += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    pygame.display.update()


