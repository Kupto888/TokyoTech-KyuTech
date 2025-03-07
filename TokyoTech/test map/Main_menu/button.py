import pygame

class Button():
    def __init__(self, image, pos, text_input, font, base_color, hovering_color):
        self.image = image
        self.original_image = image.copy() if image is not None else None  # Store the original image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.base_color, self.hovering_color = base_color, hovering_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)
        
        if self.image is None:
            self.image = self.text
        
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def update(self, screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def checkForInput(self, position):
        if self.rect.collidepoint(position):  # Simplified hitbox check
            return True
        return False

    def changeColor(self, position):
        is_hovered = self.rect.collidepoint(position)
        
        if is_hovered:
            self.text = self.font.render(self.text_input, True, self.hovering_color)
            if self.original_image is not None:
                self.image = self.original_image.copy()
                self.image.fill((30, 30, 30), special_flags=pygame.BLEND_RGB_ADD)  # Brighten
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)
            self.image = self.original_image  # Restore original image
        
        return self.text_input, is_hovered  # Return button name and hover state



