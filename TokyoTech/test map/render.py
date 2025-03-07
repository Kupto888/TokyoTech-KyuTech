import pygame
from pytmx.util_pygame import load_pygame
import pytmx
class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups, z_index="ground"):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft=pos)
        self.z_index = z_index

class TopDecoration(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft=pos)
        self.z_index = "top_decoration"

class Object(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft=pos)
        self.z_index = "objects"

class FloorDecoration(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft=pos)
        self.z_index = "floor_decoration"

class CollisionObject(pygame.sprite.Sprite):
    def __init__(self, rect, groups):
        super().__init__(groups)
        self.rect = rect
        self.image = pygame.Surface((rect.width, rect.height), pygame.SRCALPHA)  # Transparent collision box

class NPC(pygame.sprite.Sprite): #NPC
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft=pos)
        self.z_index = "NPC"        

def map_render(tmx_path):
    """Loads a .tmx file and returns sprite groups for tiles, objects, and collisions."""
    tmx_data = load_pygame(tmx_path)
    sprite_group = pygame.sprite.Group()
    collision_sprites = pygame.sprite.Group()

    # Load Tile Layers
    for layer in tmx_data.visible_layers:
        if isinstance(layer, pytmx.TiledTileLayer):  
            for x, y, surf in layer.tiles():
                pos = (x * tmx_data.tilewidth, y * tmx_data.tileheight)

                if layer.name == "Floor":
                    Tile(pos, surf, sprite_group, z_index="ground")
                elif layer.name == "Wall":
                    Tile(pos, surf, sprite_group, z_index="wall")
                elif layer.name == "Border":  
                    Tile(pos, surf, sprite_group, z_index="border")
                    CollisionObject(pygame.Rect(pos[0], pos[1], tmx_data.tilewidth, tmx_data.tileheight), collision_sprites)



    # Load Object Layers
    for layer in tmx_data.objectgroups:
        for obj in layer:
            if hasattr(obj, "gid"):  
                surf = tmx_data.get_tile_image_by_gid(obj.gid)  

                if surf:  # Only create if there's a valid image
                    pos = (obj.x, obj.y)

                    if layer.name == "FloorDecoration":
                        FloorDecoration(pos, surf, sprite_group)

                    elif layer.name == "Object":
                        Object(pos, surf, sprite_group)

                    elif layer.name == "TopDecoration":
                        TopDecoration(pos, surf, sprite_group)

            elif layer.name == "Player":  
                rect = pygame.Rect(obj.x, obj.y, obj.width, obj.height)
                CollisionObject(rect, collision_sprites)

    return sprite_group, collision_sprites
