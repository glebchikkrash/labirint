# Разработай свою игру в этом файле!

from pygame import *
import time
class GameSprite(sprite.Sprite):
    def __init__(self,picture,w,h,x,y):
        super().__init__()
        self.image=transform.scale(image.load(picture),(w,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Gost(GameSprite):
    def __init__(self,picture,w,h,x,y, x_speed, y_speed): 
        super().__init__(picture,w,h,x,y)
        self.x_speed = x_speed
        self.y_speed = y_speed
    def update(self):
        self.rect.x+=self.x_speed
        self.rect.y+=self.y_speed


        
window = display.set_mode((900, 800))
display.set_caption('ЛАБИРИНТ')
wall_1 = GameSprite('labirint.png', 900, 800, 0, 0)
gost = Gost('001.png', 60, 60, 30, 30, 0, 0)

run = True
while run:
    wall_1.reset()
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_UP:
                gost.y_speed = -5
            elif e.key == K_DOWN:
                gost.y_speed = 5    
            elif e.key == K_LEFT:
                gost.x_speed = -5
            elif e.key == K_RIGHT:
                gost.x_speed = 5    
        elif e.type == KEYUP:
            if e.key == K_UP or e.key == K_DOWN:
                gost.y_speed = 0
            elif e.key == K_LEFT or e.key == K_RIGHT:
                gost.x_speed = 0
        
    gost.update()
    
    gost.reset()
    
    display.update()
