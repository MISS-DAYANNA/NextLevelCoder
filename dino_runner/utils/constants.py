import pygame
import os

# Global Constants
TITLE = "Chrome Kirby Runner <3"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "DinoWallpaper.png"))

RUNNING = [
    #pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1.png")),
    #pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/kirby1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/kirby3.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/kirby2.png")),
]

RUNNING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/kirby1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/kirby3Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/kirby2Shield.png")),
]

RUNNING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

JUMPING = pygame.image.load(os.path.join(IMG_DIR, "Dino/kirbyJump.png"))
JUMPING_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Dino/kirbyJumpShield.png"))
JUMPING_HAMMER = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpHammer.png"))

DUCKING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/kirbyDuck1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/kirbyDuck2.png")),
]

DUCKING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/kirbyDuck1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/kirbyDuck2Shield.png")),
]

DUCKING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

SMALL_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/obstaculo1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/obstaculo2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/obstaculo3.png")),
]
LARGE_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus3.png")),
]

BIRD = [
    pygame.image.load(os.path.join(IMG_DIR, "Bird/bird1P.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/bird2P.png")),
]

CLOUD = pygame.image.load(os.path.join(IMG_DIR, 'Other/cloud1.png'))
SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shieldEstrella.png'))
HAMMER = pygame.image.load(os.path.join(IMG_DIR, 'Other/hammer.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

DEFAULT_TYPE = "default"
SHIELD_TYPE = "shield"

