import pygame, sys
from setting import *
from render import map_render
from player import Player
from camera import CameraGroup

class Game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((Width, Height))
        self.clock = pygame.time.Clock()

        # Camera & Sprite Groups
        self.camera_group = CameraGroup()

        # Load Map
        self.tiles, self.collision_sprites = map_render('..\Graphic\KYUTECH GAME MAP.tmx')
        self.camera_group.add(self.tiles)  # Add map tiles to camera group

        # Load Player
        self.player = Player((32*30, 32*46), self.camera_group, self.collision_sprites)  
        

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill((0, 0, 0))  # Clear screen
            self.camera_group.custom_draw(self.player)  # Draw everything
            self.camera_group.update()

            pygame.display.update()
            self.clock.tick(60)  # Limit FPS

Game().run()
