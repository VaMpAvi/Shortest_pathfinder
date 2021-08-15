import pygame
import time
from pygame import mixer
from algo import Graph,BFS

pygame.init()
screen=pygame.display.set_mode((965,800))
pygame.display.set_caption('path')
rect=pygame.Rect(0,0,15,15)
color=[pygame.Color(255,255,255)]*2400
r=[0]*2400
pos=[0]*2400
cir1=(10,197)
cir2=(24,242)
list=[]
box=""
da=pygame.draw.rect(screen,(0,0,0),(20,52,150,20))
pos_1=0
pos_2=101
active=False
move=False
move1=False
call=False
call1=False
menu=False
text1='ALGORITHMS'
font=pygame.font.Font('freesansbold.ttf', 20)
text=font.render(text1,True,(0,240,0))
g=Graph()
graph=[[0 if j!=i+1 and j!=i-1 and j!=i-60 and j!=i+60  else(0 if (i==j-1 and j%60==0)or(i==j+1 and i%60==0)  else 2)  for j in range(2400)]for i in range(2400) ]
def draw() :
    global r,pos,cir1,cir2,color,text1,box,menu
    rect.y=140
    for i in range(2400) :
            if i%60==0 :
                rect.x=1
                rect.y+=16
            r[i]=pygame.draw.rect(screen,color[i],rect,0)
            pos[i]=rect[0:2]
            rect.x+=16
    pygame.draw.circle(screen, (0,0,255), cir1, 5)
    pygame.draw.circle(screen, (255,0,255), cir2, 5)
    box=pygame.draw.rect(screen,(0,0,0),(20,20,150,30))
    if menu :
        da=pygame.draw.rect(screen,(0,0,0),(20,52,150,20))
    #font=text.render('ALGORITHMS',True,(0,240,0))
    text=font.render(text1,True,(0,240,0))
    screen.blit(text,(22,24))
    pygame.display.update()
run=True

while run :
    screen.fill((150,246,255))
    draw()
    for event in pygame.event.get() :
        if event.type==pygame.QUIT :
            run =False 
        #algo call
        if event.type==pygame.KEYDOWN :
            if event.key==pygame.K_RIGHT :
                call=True
            
            if event.key==pygame.K_LEFT :
                call1=True
        #algo
        if call :
            g.dijkstra(graph,2400,pos_1,pos_2,color,draw,list)
            call=False

        if call1 :
            b=BFS(pos_1)
            b.bfs(pos_2,pos_1,draw,color,list)
            call1=False
        if event.type==pygame.MOUSEBUTTONDOWN :
            if event.pos[0]>=cir1[0]-7 and event.pos[0]<=cir1[0]+7 and event.pos[1]>=cir1[1]-7 and event.pos[1]<=cir1[1]+7 :
                move=True
            if event.pos[0]>=cir2[0]-7 and event.pos[0]<=cir2[0]+7 and event.pos[1]>=cir2[1]-7 and event.pos[1]<=cir2[1]+7 :
                move1=True
            active=True
            if box.collidepoint(event.pos) :
                menu=True
            if da.collidepoint(event.pos) :
                text1="Dijksh algo"
                menu=False
        if active :
            for i in range(2400) :
                if r[i].collidepoint(event.pos) and not move and not move1 and not r[i].collidepoint(cir1) and not r[i].collidepoint(cir2):
                    color[i]=(0,0,0)
                    list.append(i)
        if event.type==pygame.MOUSEBUTTONUP :
            active=False
            move=False
            move1=False
    if move :
        cir1=event.pos
        for i in range(2400) :
            if r[i].collidepoint(event.pos) :
                newx=pos[i][0]+7
                newy=pos[i][1]+8
                cir1=(newx,newy)
                pos_1=i
    if move1 :
        cir2=event.pos
        for i in range(2400) :
            if r[i].collidepoint(event.pos) :
                newx=pos[i][0]+7
                newy=pos[i][1]+8
                cir2=(newx,newy)
                pos_2=i
    #pygame.display.update()