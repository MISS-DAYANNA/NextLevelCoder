
import pygame
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager

from dino_runner.utils.constants import BG, CLOUD, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.power_ups.power_up_manager import PowerUpManager

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.points = 0
        self.power_up_manager = PowerUpManager()
        #self.puntuacion = 0


    def run(self):
        # Game loop: events - update - draw
        self.create_components()
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
        pygame.quit()
    
    def create_components(self):
        self.power_up_manager.reset_power_up(self.points)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
            
                
                
        #for muerto in 
    #def reiniciarPartida(self):
        #if self.playing == False:
            # self.game_speed = 20,
            # self.x_pos_bg = 0,
            # self.y_pos_bg = 380,
             #self.player = Dinosaur(),
            # self.obstacle_manager = ObstacleManager(),
            # self.points = 0,
            # self.power_up_manager = PowerUpManager()

          
        

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.power_up_manager.update(self.points, self.game_speed, self.player)

    def draw(self):
        self.score()
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        #self.puntuacion.draw("score: "+ int(self.points))
        #print("SCORE: ", self.points)
        #text = ('score: ', self.points,80, 300, (0,0,0))
        pygame.display.update()
        pygame.display.flip()


    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

        image_width = CLOUD.get_width()
        self.screen.blit(CLOUD, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(CLOUD, (image_width + 500-self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= image_width:
            self.screen.blit(CLOUD, (image_width + self.x_pos_bg, self.y_pos_bg))
            
    
    def score(self):
        self.points += 1
        if self.points % 100 == 0:
            self.game_speed += 1 #cada 100 puntos el dino va mas rapido 
        self.player.check_invicibility(self.screen)
        print("SCORE: ", self.points)
        
            
    


