import pygame
import os
from setting import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group, collision_sprites):
        super().__init__(group)
        self.animation = []
        self.animation_index = 0
        self.animation_speed = 0.3
        for path in os.listdir('Graphic/Player/KUP'):
            print(path)
            image = pygame.image.load('Graphic/Player/KUP/' + path).convert_alpha()
            self.animation.append(image)
        # self.image = pygame.image.load('Graphic/Player/BINH/BINH IDLE.png').convert_alpha()
        self.image = self.animation[0]
        self.sup_animation = []

        self.rect = self.image.get_rect(center=pos)
        self.direction = pygame.math.Vector2()
        self.speed = 5
        self.collision_sprites = collision_sprites
        self.z = LAYER['player']
        self.facing_up = True
        self.facing_right = False

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.direction.y = -1
            self.facing_up = True
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
            self.facing_up = False
        else:
            self.direction.y = 0

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.facing_right = True

        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.facing_right = False

        else:
            self.direction.x = 0


    def interact(self):
        pass

    def move(self):
        new_rect = self.rect.copy()
        new_rect.center += self.direction * self.speed

        for sprite in self.collision_sprites:
            if new_rect.colliderect(sprite.rect):
                return  # Cancel movement if colliding

        self.rect.center += self.direction * self.speed

    def animate(self):
        """Updates the player's animation."""
        if not self.facing_up:
            self.sup_animation = self.animation[:2]
        else:
            self.sup_animation = self.animation[3:]
        if self.direction.x != 0 or self.direction.y != 0:  # ✅ Only animate when moving
            self.animation_index += self.animation_speed

            if self.animation_index >= len(self.sup_animation):  # ✅ Loop animation
                self.animation_index = 0

        else:
            self.animation_index = 0  # ✅ Reset to idle frame when stopping


        # Update image
        self.image = self.sup_animation[int(self.animation_index)]
        # Flip image if facing left
        if self.facing_right:
            self.image = pygame.transform.flip(self.image, True, False)
    
    def update(self):
        self.input()
        self.move()
        self.animate()
