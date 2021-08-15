import pygame
import time

pygame.init()
screen=pygame.display.set_mode((640,480))


x=30
y=30
c=[0]*20
def draw() :
    global y,x
    x=y=30
    for i in range(count) :
        c[i]=pygame.draw.circle(screen,(0,255,0),(x,y),15)
        y+=40
        x+
        print(c[i][1])
    pygame.display.update()


run=True
img=False
count=0
while run :
    screen.fill((150,246,255))

    for event in pygame.event.get() :
        if event.type==pygame.QUIT :
            run=False
        
        if event.type==pygame.KEYDOWN :
            if event.key==pygame.K_LEFT :
                count+=1
                img=True
            
        if img :
            draw()
    #pygame.display.update()