import pygame

class Button(object):
    def __init__(self, x, y, width, height) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.is_hovered = False
        self.is_down = False

    def get_image(self, image_path):
        image = pygame.image.load(image_path)
        image = pygame.transform.scale(image, (self.width, self.height))
        rect = image.get_rect(topleft=(self.x, self.y))

        return image, rect

    def draw(self, screen, image_path):
        self.image, self.rect = self.get_image(image_path)
        screen.blit(self.image, self.rect)

    def check_hover(self, mouse_pos):
        self.is_hovered = self.rect.collidepoint(mouse_pos)

    def check_down(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and self.is_hovered:
                self.is_down = True

class Button_start(Button):
    def __init__(self, screen, x, y, width, height) -> None:
        super().__init__(x, y, width, height)

        self.draw(screen, "button_start.png")