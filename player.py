import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 255))  # Magenta color
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velocity_y = 0
        self.jumping = False
        self.gravity = 0.8
        self.jump_power = -15
        self.speed = 5

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_SPACE] and not self.jumping:
            self.velocity_y = self.jump_power
            self.jumping = True

    def update(self):
        # Apply gravity
        self.velocity_y += self.gravity
        self.rect.y += self.velocity_y

        # Basic ground collision
        if self.rect.bottom > 600:  # Screen height
            self.rect.bottom = 600
            self.velocity_y = 0
            self.jumping = False

        # Keep player in bounds
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > 800:  # Screen width
            self.rect.right = 800 