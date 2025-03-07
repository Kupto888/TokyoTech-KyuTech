import pygame, sys
from setting import *
from render import map_render
from player import Player
from camera import CameraGroup
from Main_menu.menu import main_menu
from Main_menu.button import Button
import cv2
class Game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((Width, Height))
        self.clock = pygame.time.Clock()

        # Camera & Sprite Groups
        self.camera_group = CameraGroup()

        # Load Map
        self.tiles, self.collision_sprites = map_render('Graphic/Map/map.tmx')
        self.camera_group.add(self.tiles)  # Add map tiles to camera group

        # Load Player
        self.player = Player((400, 400), self.camera_group, self.collision_sprites)
        

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.K_ESCAPE:

                    pass

            self.screen.fill((0, 0, 0))  # Clear screen
            self.camera_group.update()
            self.camera_group.custom_draw(self.player)  # Draw everything

                
                





            pygame.display.update()
            self.clock.tick(60)  # Limit FPS


GO = Game() 

# vid = cv2.VideoCapture('Game Intro.mp4')
# video_play = True
# while video_play:
#     ret, frame = vid.read()
#     if not ret:
#         break

#     frame_scaled = cv2.resize(frame, (Width, Height))

#     # Convert the BGR frame to RGB (OpenCV uses BGR, Pygame uses RGB)
#     frame_rgb = cv2.cvtColor(frame_scaled, cv2.COLOR_BGR2RGB)

#     # Convert the frame to a Pygame surface
#     frame_surface = pygame.image.fromstring(frame_rgb.tobytes(), frame_rgb.shape[1::-1], "RGB")

#     # Display the frame
#     GO.screen.blit(frame_surface, (0, 0))
#     pygame.display.update()

#     # Control the frame rate (e.g., 30 frames per second)
#     GO.clock.tick(30)

# vid.release()


main_menu(button_bg = pygame.image.load("Main_menu/resource/button.png"),frame_index = 0)
GO.run()
