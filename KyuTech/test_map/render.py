import pygame
import pytmx
from pytmx.util_pygame import load_pygame
from setting import *
from camera import CameraGroup

class Generic(pygame.sprite.Sprite):
	def __init__(self, pos, surf, groups, z):
		super().__init__(groups)
		self.image = surf
		self.rect = self.image.get_rect(topleft = pos)
		self.z = z
		self.hitbox = self.rect.copy().inflate(-self.rect.width * 0.2, -self.rect.height * 0.75)

class Tile(Generic):
    def __init__(self, pos, surf, groups):
        super().__init__(
            pos = pos,
            surf = surf,
            groups = groups,
            z = LAYER["ground"],
        )
        self.hitbox = self.rect.copy().inflate(-self.rect.width * 0.2, -self.rect.height * 0.75)

class TopDecoration(Generic):
    def __init__(self, pos, surf, groups):
        super().__init__(
            pos = pos,
            surf = surf,
            groups = groups,
            z = LAYER["top_decoration"]
        )

class Object(Generic):
    def __init__(self, pos, surf, groups):
        super().__init__(
            pos = pos,
            surf = surf,
            groups = groups,
            z = LAYER["objects"]
        )

class FloorDecoration(Generic):
    def __init__(self, pos, surf, groups):
        super().__init__(
            pos = pos,
            surf = surf,
            groups = groups,
            z = LAYER["floor_decoration"]
        )

class CollisionObject(pygame.sprite.Sprite):
    def __init__(self, rect, groups):
        super().__init__(groups)
        self.rect = rect
        self.z = LAYER["objects"]
        self.image = pygame.Surface((rect.width, rect.height), pygame.SRCALPHA)  # Transparent collision box

def map_render(tmx_path):
    """Loads a .tmx file and returns a sprite group with all tiles and collision objects."""
    tmx_data = load_pygame(tmx_path)
    sprite_group = CameraGroup()
    collision_sprites = pygame.sprite.Group()

    for layer in tmx_data.visible_layers:
        for layer in ['Floor1','Floor2','Floor3']:
            for x, y, surf in tmx_data.get_layer_by_name(layer).tiles():
                pos = (x * tmx_data.tilewidth, y * tmx_data.tileheight)
                Generic(pos,surf,sprite_group,LAYER['ground'])

        for layer in ['Wall1','Wall2','Wall3','Wall4']:
            for x, y, surf in tmx_data.get_layer_by_name(layer).tiles():
                pos = (x * tmx_data.tilewidth, y * tmx_data.tileheight)
                rect = pygame.Rect(pos[0], pos[1], surf.get_size()[0]/32, surf.get_size()[0]/32)
                Generic(pos,surf,sprite_group,LAYER['objects'])
                CollisionObject(rect, collision_sprites)
        
        for obj in tmx_data.get_layer_by_name('NPC'):
            pos = (obj.x, obj.y)
            rect = pygame.Rect(obj.x, obj.y, obj.width, obj.height)
            CollisionObject(rect, collision_sprites)  # Add proper collision object
            Object(pos, obj.image, sprite_group)

    return sprite_group, collision_sprites

