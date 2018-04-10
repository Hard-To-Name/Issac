import pygame
import room
import handle

background_img_name = "img/Background.JPG"
player_img_name = "img/huaji.png"

class GameOver(Exception):
    pass

def main():
    pygame.init()
    screen = pygame.display.set_mode([800,500])
    screen_title = pygame.display.set_caption("Issac")
    background = pygame.image.load(background_img_name).convert()
    level_info = room.generate_environment()
    for item in level_info:
        print(item)
        print()
    handle.handle(0, background, screen, screen_title, player_img_name)
    

if __name__ == "__main__":
    while True:
        try:
            main()
        except GameOver: pass
            
