import pygame
import player
import bullet
import hunter
from random import uniform
from sys import exit
from main import background_img_name, player_img_name, GameOver

def handle(position, background, screen, screen_title, player_img_name):
    directions = [0, 0, 0, 0]
    b_directions = [0, 0, 0, 0]
    p1 = player.player(background.get_width(), background.get_height(), player_img_name)
    hunters = []
    bullets = []
    for i in range(int(uniform(1,6))):
        hunters.append(hunter.hunter(background.get_width(), background.get_height()))
    while True:
        screen.blit(background, (0,0))
        screen.blit(p1.img,(p1.x_index,p1.y_index))
        for h in hunters: screen.blit(h.img,(h.x_index,h.y_index))
        for b in bullets: screen.blit(b.img,(b.x_index,b.y_index))
        pygame.draw.rect(screen, (227,23,13), (7.5, 10, 207.5, 20), 5)
        pygame.draw.line(screen, (227,23,13), (10,20), (10+p1.health*2,20), 20)
        for event in pygame.event.get():
            #player move
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    directions[0] = 1
                if event.key == pygame.K_s:
                    directions[1] = 1
                if event.key == pygame.K_a:
                    directions[2] = 1
                if event.key == pygame.K_d:
                    directions[3] = 1
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    directions[0] = 0
                if event.key == pygame.K_s:
                    directions[1] = 0
                if event.key == pygame.K_a:
                    directions[2] = 0
                if event.key == pygame.K_d:
                    directions[3] = 0
            #bullet
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    b_directions[0] = 1
                if event.key == pygame.K_DOWN:
                    b_directions[1] = 1
                if event.key == pygame.K_LEFT:
                    b_directions[2] = 1
                if event.key == pygame.K_RIGHT:
                    b_directions[3] = 1
                #create bullet
                if b_directions != [0, 0, 0, 0] and \
                (b_directions[1]-b_directions[0], b_directions[3]-b_directions[2]) != (0, 0):
                    # if not using temp, the directions of all bullets will change
                    temp = [0, 0, 0, 0]
                    for i in range(4):
                        temp[i] = b_directions[i]
                    bullets.append(bullet.bullet(p1, temp))
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    b_directions[0] = 0
                if event.key == pygame.K_DOWN:
                    b_directions[1] = 0
                if event.key == pygame.K_LEFT:
                    b_directions[2] = 0
                if event.key == pygame.K_RIGHT:
                    b_directions[3] = 0
            if event.type == pygame.QUIT:
                exit()
        # move player
        p1.move(background.get_width(), background.get_height(), directions)
        
        # move bullet
        bullets_remove_list = []
        for b in bullets:
            b.move()
            if b.finish(background.get_width(), background.get_height(), hunters):
                bullets_remove_list.append(b)
        for rb in bullets_remove_list: bullets.remove(rb)
        
        # hunter check
        hunters_remove_list = []
        for h in hunters:
            if h.health <= 0:
                hunters_remove_list.append(h)
        for rh in hunters_remove_list: hunters.remove(rh)
        
        # move hunter
        if hunters != []:
            distances = []
            for h in hunters:
                h.move(p1)
                distances.append(h.get_distance(p1))
            if min(distances) < p1.width and p1.in_protect == False:
                p1.health -= 20
                p1.in_protect = True
            if min(distances) > p1.width: p1.in_protect = False
        
        # game-over condition
        if p1.health <= 0:
            while True:
                default_font = pygame.font.SysFont(None, 60)
                gameover_text = default_font.render("Game Over! Press 'R' to restart.", True, (227,23,13))
                screen.blit(gameover_text, (90, 210))
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT: exit()
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_r: raise GameOver
        pygame.display.update()