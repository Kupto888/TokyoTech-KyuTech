import pygame
pygame.init()
Info = pygame.display.Info()
Height = Info.current_h
Width = Info.current_w

LAYER = {
    "ground": 0,
    "floor_decoration": 1,
    "wall" : 2,
    "player": 5,
    "objects": 10,
    "border" : 20,
    "top_decoration": 200
}


