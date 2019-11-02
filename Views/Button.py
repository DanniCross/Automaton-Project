import pygame


class Button(pygame.sprite.Sprite):

    def __init__(self, up, down, x, y):
        super(Button, Button).__init__(self)
        self.normal = up
        self.selection = down
        self.current = self.normal
        self.rect = self.current.get_rect()
        self.rect.left, self.rect.top = (x, y)
        self.x = x
        self.y = y

    def update(self, screen, cursor, add):
        if cursor.colliderect(self.rect):
            self.current = self.selection
        else:
            self.current = self.normal
        screen.blit(self.current, self.rect)
        screen.blit(add, (self.x + 20, self.y + 22))
