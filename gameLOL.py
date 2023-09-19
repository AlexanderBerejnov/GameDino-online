import pygame 
import random

window_height = 500
window_width = 500
dis = pygame.display.set_mode((window_height, window_width))
player = pygame.draw.rect(dis, (0,0,0), [10, 20, 10, 10])
run = True
up = True
pygame.RESIZABLE
x = 100
y = 450
pygame.font.init()
clock = pygame.time.Clock()
botX = 400
bot = pygame.draw.rect(dis, (25, 211,0), [botX, 450, 25, 25])
v = 0
while run:
    def game_over():
        dis.fill((0,0,255))  
        font = pygame.font.SysFont('Aria', 100)
        img = font.render(':)', True, (0, 0, 0))
        dis.blit(img, (40, 250))
        
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            run = False
        if ev.type == pygame.KEYDOWN:
            if up == True:
                if ev.key == pygame.K_SPACE:
                    y -= random.randint(0, 400)
                    up = False
    if y >= 450:
        up = True
    if up == False and y<450:
        y += 12
    botX-=10
    if botX <=0:
        botX=450
    bot = pygame.draw.rect(dis, (0,0, 0), [botX, 450, 25, 25])
    p = pygame.draw.rect(dis, (255,255,255), [x, y, 25, 25])
    pygame.draw.rect(dis, (255,0,0), [0, 475, 500, 25])
    c = bot.colliderect(p)
    if c:
        game_over()
        

    
    
    pygame.display.update()
    
    lol = [(0,0,0), (255, 255, 255)]
    dis.fill(lol[random.randint(0,1)])
    clock.tick(25)
                    
                    
                