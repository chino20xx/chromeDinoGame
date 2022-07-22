import os
import pygame

pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Chrome Dino Game by chino20xx")
background = pygame.image.load('background.png')
cactus = pygame.image.load('cactus.png')
dinosaur = pygame.image.load('dinosaur.png')
WHITE = (255,255,255)
RED = (255,0,0)
font = pygame.font.SysFont('roboto', 20)
font1 = pygame.font.SysFont('roboto', 40)
background_x,background_y = 0, 0
dinosaur_x, dinosaur_y = 0, 230
cactus_x, cactus_y = 550, 230
x_velocity, y_velocity = 5, 7
score = 0
jump = False
pausing = False
running = True
clock = pygame.time.Clock()

while running:
    clock.tick(60)
    SCREEN.fill(WHITE)
    background1_rect = SCREEN.blit(background, (background_x, background_y))
    background2_rect = SCREEN.blit(background, (background_x+600, background_y))
    dinosaur_rect = SCREEN.blit(dinosaur, (dinosaur_x, dinosaur_y))
    score_txt = font.render('Score: '+ str(score), True, RED)
    SCREEN.blit(score_txt,(5,5))
    background_x -= x_velocity
    if background_x+600 < 0:
        background_x = 0
    cactus_x -= x_velocity
    if cactus_x <= -20:
        cactus_x = 550
        score += 1
    if 80 <= dinosaur_y <= 230:
        if jump == True:
            dinosaur_y -= y_velocity
    else:
        jump = False
    if dinosaur_y < 230:
        if jump == False:
            dinosaur_y += y_velocity
    dinosaur_rect = SCREEN.blit(dinosaur, (dinosaur_x, dinosaur_y))
    cactus_rect = SCREEN.blit(cactus, (cactus_x, cactus_y))
    if dinosaur_rect.colliderect(cactus_rect):
        pausing = True
        gameover_txt = font1.render("Game Over", True, RED)
        SCREEN.blit(gameover_txt,(200,150))
        x_velocity, y_velocity = 0, 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                if dinosaur_y == 230:
                    jump = True
                if pausing:
                    background_x, background_y = 0, 0
                    dinosaur_x, dinosaur_y = 0, 230
                    cactus_x, cactus_y = 550, 230
                    x_velocity, y_velocity = 5, 7
                    score = 0
                    pausing = False
    pygame.display.flip()
pygame.quit()