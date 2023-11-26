import pygame

# Updated to conform to flake8 and black standards <-- what standards?
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill((0, 0, 255))
        self.rect = self.surf.get_rect()

    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

pygame.init()

# ----- SETUP ----- #

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player = Player()

# ----- GAME LOOP ----- #

running = True

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

        elif event.type == QUIT:
            running = False

    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)

    screen.fill((255, 255, 255))

    surf = pygame.Surface((50, 50))
    surf.fill((0, 0, 0))
    rect = surf.get_rect()

    surf_center = (
        (SCREEN_WIDTH-surf.get_width())/2,
        (SCREEN_HEIGHT-surf.get_height())/2
    )

    screen.blit(surf, surf_center)
    screen.blit(player.surf, player.rect)
    # screen.blit(player.surf, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
    pygame.display.flip()