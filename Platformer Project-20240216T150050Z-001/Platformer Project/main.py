import pygame
from pygame import mixer
mixer.init()

#მუსიკების შემოტანა
mixer.music.load("images/jungles.ogg")
mixer.music.play(-1)

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode

width = 1400 / 1.4
height = 999 / 1.4((width, height))
pygame.display.set_caption("MazeGame")

icon = pygame.image.load("images/cyborg.png")
pygame.display.set_icon(icon)

background = pygame.image.load("images/background.jpg").convert_alpha()
background = pygame.transform.scale(background, (width, height))

class BaseClass:
    def __init__(self, image, x, y):
        self.right_image = image
        self.image = image
        self.rect = image.get_rect(centerx=x, centery=y)
        self.dx = 0
        self.dy = 0

    def draw(self):
        screen.blit(self.image, self.rect)

        if self.dx > 0:
            self.image = self.right_image
        if self.dx < 0:
            self.image = pygame.transform.flip(self.right_image, True, False)

        #ეკრანს არ გაცდეს
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= width:
            self.rect.right = width
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= height:
            self.rect.bottom = height

class Player(BaseClass):
    def __init__(self, image, x, y):
        super().__init__(image, x, y)

    def movement(self):
        self.dx = 0
        self.dy = 0

        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT]:
            self.dx = 5
        if key[pygame.K_LEFT]:
            self.dx = -5
        if key[pygame.K_UP]:
            self.dy = -5
        if key[pygame.K_DOWN]:
            self.dy = 5

        self.rect.x += self.dx
        self.rect.y += self.dy

    def update(self):
        self.movement()
        self.draw()


class Enemy(BaseClass):
    def __init__(self, image, x, y):
        super().__init__(image, x, y)


player_image = pygame.image.load("images/hero.png")
player_image = pygame.transform.scale(player_image, (70, 70))
player = Player(player_image, 300, 300)

run = True
while run:
    clock.tick(60)
    screen.blit(background, (0, 0))
    player.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
