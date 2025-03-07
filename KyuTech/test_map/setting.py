import pygame
pygame.init()
Info = pygame.display.Info()
Height = Info.current_h
Width = Info.current_w

LAYER = {
    "ground": 0,
    "floor_decoration": 1,
    "objects": 2,
    "top_decoration": 3,
    "player": 4,
}


