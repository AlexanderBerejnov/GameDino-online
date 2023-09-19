


import pygame 
pygame.init()

class Game():
    def __init__(self, window_height=500, window_width=500, size_player=40):
        self.window = pygame.display.set_mode((window_height, window_width))
        self.size_player = size_player
        self.up = False
        self.clock = pygame.time.Clock()
        self.x_player = 10
        self.y_player = 300
    def monster(self):
        self.window.fill((0, 0, 0))
        x_monster = 500
        pygame.draw.rect(self.window, (255, 255, 255), [x_monster, 400, 25, 25])
        pygame.display.update()
        if x_monster <= 5:
            x_monster = 500
        else:
            x_monster -= 1
        
        
        
    def player(self):
        self.window.fill((0, 0, 0))
        if self.up == False and self.y_player <= 300:
            self.y_player += 10
        if self.y_player <= 200:
            self.up = False
            
        if self.up == True:
            self.y_player -= 11
        pygame.draw.rect(self.window, (255, 255, 255), [self.x_player, 
                                                        self.y_player, 
                                                        self.size_player,
                                                        self.size_player])
    def main(self):
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and self.up == False and self.y_player >= 300:
                        self.up = True
                        
            self.monster()
            self.player()
            self.clock.tick(30)
            pygame.display.update()
            
            
Game().main()
                        