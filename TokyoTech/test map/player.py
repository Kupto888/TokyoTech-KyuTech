import pygame
import os

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group, collision_sprites):
        super().__init__(group)
        
        # Load animations
        self.animation = []
        self.animation_index = 0
        self.animation_speed = 0.15  
        for path in sorted(os.listdir('Graphic/Player/kup')):  
            image = pygame.image.load(f'Graphic/Player/kup/{path}').convert_alpha()
            self.animation.append(image)
        self.sup_animation = []
        
        self.image = self.animation[0]  # Default frame
        self.rect = self.image.get_rect(center=pos)
        
        # Movement variables
        self.direction = pygame.math.Vector2()
        self.speed = 3.0
        self.collision_sprites = collision_sprites
        self.z_index = 'player'

        # Facing direction
        self.facing_right = True  
        self.facing_up = False

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
            self.facing_right = True  # ✅ Face right

        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.facing_right = False  # ✅ Face left

        else:
            self.direction.x = 0

    def animate(self):
        """Updates the player's animation."""
        if not self.facing_up:
            self.sup_animation = self.animation[:2]
        else:
            self.sup_animation = self.animation[3:]
        if self.direction.x != 0 or self.direction.y != 0:  
            self.animation_index += self.animation_speed

            if self.animation_index >= len(self.sup_animation): 
                self.animation_index = 0

        else:
            self.animation_index = 0  
            # self.sup_animation = self.animation[:2]


        # Update image
        self.image = self.sup_animation[int(self.animation_index)]
        # Flip image if facing left
        if self.facing_right:
            self.image = pygame.transform.flip(self.image, True, False)

    def move(self):
        """Handles movement and collision."""
        new_rect = self.rect.copy()
        new_rect.center += self.direction * self.speed

        for sprite in self.collision_sprites:
            if new_rect.colliderect(sprite.rect):
                return  # Stop moving if colliding

        self.rect.center += self.direction * self.speed

    def update(self):
        """Updates player movement and animation."""
        self.input()
        self.move()
        self.animate()  
