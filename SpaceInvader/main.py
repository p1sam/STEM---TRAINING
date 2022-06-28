import pygame


pygame.init()
screen = pygame.display.set_mode((800, 600))

icon = pygame.image.load("icon.png")

background = pygame.image.load("background.png")
pygame.display.set_caption("Space Invader")
pygame.display.set_icon(icon)


while True:
    screen.blit(background, (120, 100))
    pygame.display.update()
    




if __name__=='__main__':
    pass