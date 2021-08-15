import pygame 
import time
from algo import Graph

screen=pygame.display.set_mode((640,650))
pygame.display.set_caption('Pathfinder')
rect=pygame.Rect(0,0,20,20)
color=[pygame.Color(255,255,255)]*20
cir1=(10,41)
cir2=(31,62)
run=True
active=False
move=False
move1=False
r=[0]*20
pos=[0]*20
list=[]
call =False
g=Graph()
graph=[[0 if j!=i+1 and j!=i-1 and j!=i-5 and j!=i+5  else(2 if (j+i)%5!= 4 or (j-i)%5!=1  and (i-j)%5!=1 or (j+i)%5!=4  else 0)  for j in range(20)]for i in range(20) ]
# g.dijkstra(graph,20,5,7)
done=True
k=0
def col(i=-1,j=-1) :
    global color,k
    if i==-1 and j==-1:
        return color,k
    elif i!=-1 and j==1 :
        color[i]=(0,255,0)
        k+=1
        print('i')
        return 
    else :
        color[i]=(255,255,0)
        k+=1
        return 
clock=pygame.time.Clock()
#def draw() :
    # global rect,color,pos,r
    # rect.y=10 
    # for i in range(20) :
    #     if i%5==0 :
    #         rect.x=1
    #         rect.y+=21
    #     r[i]=pygame.draw.rect(screen,color[i],rect,0)
    #     pos[i]=rect[0:2]
    #     rect.x+=21
    #     #pygame.display.update()
    #global run,rect,screen,call,cir1,cir2,active,move,move1,r,pos,list
    #if done :
        
        #run=True
        #call=True
while run :
    screen.fill((150,246,255))
    for event in pygame.event.get() :
        if event.type==pygame.QUIT :
            run =False 
        if event.type==pygame.KEYDOWN :
            if event.key==pygame.K_RIGHT :
                call=True
        
        if call :
            g.dijkstra(graph,20,0,19,color,col)
            call=False
            done=True
            print('urd')
            #run=False
        
        if event.type==pygame.MOUSEBUTTONDOWN :
            if event.pos[0]>=cir1[0]-7 and event.pos[0]<=cir1[0]+7 and event.pos[1]>=cir1[1]-7 and event.pos[1]<=cir1[1]+7 :
                move=True
            if event.pos[0]>=cir2[0]-7 and event.pos[0]<=cir2[0]+7 and event.pos[1]>=cir2[1]-7 and event.pos[1]<=cir2[1]+7 :
                move1=True
            active=True
        if active :
            for i in range(20) :
                if r[i].collidepoint(event.pos) and not move and not move1 and not r[i].collidepoint(cir1) and not r[i].collidepoint(cir2):
                    color[i]=(0,0,0)
                    list.append(i)
        if event.type==pygame.MOUSEBUTTONUP :
            active=False
            move=False
            move1=False
    if move :
        cir1=event.pos
        for i in range(20) :
            if r[i].collidepoint(event.pos) :
                newx=pos[i][0]+10
                newy=pos[i][1]+11
                cir1=(newx,newy)
                pos_=i
    if move1 :
        cir2=event.pos
        for i in range(20) :
            if r[i].collidepoint(event.pos) :
                newx=pos[i][0]+10
                newy=pos[i][1]+11
                cir2=(newx,newy)
                pos_=i
    #draw()
# def draw(r,color,rect) :
    rect.y=10 
    color,k=col()
    
    if k>=0 :
        for i in range(20) :
            if i%5==0 :
                rect.x=1
                rect.y+=21
            r[i]=pygame.draw.rect(screen,(255,255,255),rect,0)
            pos[i]=rect[0:2]
            rect.x+=21
            #time.sleep(0.1)
        #pygame.display.update()
    if k>0 :
        rect.y=10 
        for i in range(20) :
            if i%5==0 :
                rect.x=1
                rect.y+=21
            r[i]=pygame.draw.rect(screen,color[i],rect,0)
            pos[i]=rect[0:2]
            rect.x+=21
            time.sleep(0.1)
            clock.tick(5)
            pygame.display.update()
    pygame.draw.circle(screen, (0,0,255), cir1, 7)
    pygame.draw.circle(screen, (255,0,255), cir2, 7)
    pygame.display.update()
    time.sleep(0.1)
    # if fin :
    #     #print('yes')
    #     run=False
    #     #call=False
    #     done=False
    #     break
# if <1:
# draw()
# k+=1
