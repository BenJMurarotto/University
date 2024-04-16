import pygame
import time
import random
import sys
WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("HECS DEBT")

BG = pygame.transform.scale(pygame.image.load("bg.jpeg"), (WIDTH, HEIGHT))
PLAYER_WIDTH = 40
PLAYER_HEIGHT = 80
PLAYER_VEL = 20
ENEMY1_WIDTH = 15
ENEMY1_HEIGHT = 15
ENEMY1_VEL = 25


ENEMY_WIDTH_SPAWN = random.randint(ENEMY1_WIDTH, WIDTH - ENEMY1_WIDTH)

def draw(player):
    WIN.blit(BG, (0, 0))


    pygame.draw.rect(WIN, (255, 0, 255), player)

    pygame.display.update()

    
def main():
    pygame.init()
    run = True
    clock = pygame.time.Clock()
    counter, text = 0, "0".rjust(3)
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    font = pygame.font.SysFont("Consolas   ", 30)

    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)
    enemy1 = pygame.Rect(ENEMY_WIDTH_SPAWN, HEIGHT + ENEMY1_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)


    while run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.USEREVENT:
                counter += 1
                text = str(counter).rjust(3)

            if event.type == pygame.QUIT:
                run = False
                break

    
            


        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x > 0:
            player.x -= PLAYER_VEL
        if keys[pygame.K_RIGHT] and player.x < 1000 - PLAYER_WIDTH:
            player.x += PLAYER_VEL
        if keys[pygame.K_DOWN] and player.y < 800 - PLAYER_HEIGHT:
            player.y += PLAYER_VEL
        if keys[pygame.K_UP] and player.y > 0:
            player.y -= PLAYER_VEL

        hit_edge = pygame.mixer.Sound("hit_edge.wav")
        if player.x == 1000 - PLAYER_WIDTH or player.x == 0 or player.y == 800 - PLAYER_HEIGHT or player.y == 0:
            hit_edge.play()
            hit_edge.stop()



    
    

        



        draw(player)


    pygame.quit()

if __name__ == "__main__":
    main()
    