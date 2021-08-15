#from screen import *
import time
class Graph :

    def minKey(self,key,visited) :
        minn=9999
        u=0
        v=2400
        for i in range(v) :
            if key[i]<minn and not visited[i] and key[i]!=-1:
                minn=key[i]
                u=i
        return u
    
    def dijkstra(self,graph,v,src,f,color,col,list) :
        #list=[]
        key=[999]*v
        visited=[False]*v
        parent=[-1]*v
        parent[src]=-1
        key[src]=0
        for i in list :
            key[i]=-1
        for i in range(v-1) :
            if parent[f]!=-1 :
                break
            u=self.minKey(key,visited)
            visited[u]=True
            for j in range(v) :
                
                if graph[u][j]>0 and graph[u][j]+key[u]<key[j] and not visited[j]  :
                    key[j]=graph[u][j]+key[u]
                    parent[j]=u
                    color[j]=(0,255,0)
                    time.sleep(0.01)
                    col()
                    
        #draw(False,False)
        #time.sleep(1)
        self.printsol(parent,f,src,color,col)
        #draw(True,False)
    def printsol(self,parent,i,src,color,col) :
        if i == src:
            print(i,end=" ")
            #draw(True,True)
            return 
        else :
            self.printsol(parent,parent[i],src,color,col)
            print (i,end=" ")
            #time.sleep(1)
            
            color[i]=(255,255,0)
            time.sleep(0.1)
            col()
            #time.sleep(0.1)
            #draw(True,True)
# g=Graph()
# v=2500
# src=int(input('Enter the src '))
# f=int(input('Enter the dest'))
# graph=[[0 if j!=i+1 and j!=i-1 and j!=i-50 and j!=i+50  else(0 if (i==j-1 and j%50==0)or(i==j+1 and i%50==0)  else 2)  for j in range(2500)]for i in range(2500) ]

# #print(graph)
# g.dijkstra(graph,2500,src,f)
#9.14=97
# print(g.parent[1])

class BFS :
    def __init__(self,v) :
        # self.graph=[ [0, 2, 0, 6, 0],
        #     [2, 0, 3, 8, 5],
        #     [0, 3, 0, 0, 7],
        #     [6, 8, 0, 0, 9],
        #     [0, 5, 7, 9, 0]]
        
        self.graph=[[0 if j!=i+1 and j!=i-1 and j!=i-60 and j!=i+60  else(0 if (i==j-1 and j%60==0)or(i==j+1 and i%60==0)  else 2)  for j in range(2400)]for i in range(2400) ]
        self.queue=[v]
        
    def bfs(self,f,v,draw,color,list) :
        c=0
        parent=[0]*2400
        parent[self.queue[0]]=-1
        for j in range(2400):
            for i in list:
                self.graph[j][i]=0
        while c<2400:
            k=0
            if parent[f]!=0 :
                break
            for i in self.graph[self.queue[c]] :
            
            #for j in range(len(i)) :
                if i!=0 and k not in self.queue : 
                    self.queue.append(k)   
                    parent[k]=self.queue[c]
                    color[k]=(0,255,0)
                    time.sleep(0.1)
                    draw()
                k+=1
            #print(self.queue[c])
            c+=1
        self.printsol(parent,f,v,color,draw)
    def printsol(self,parent,i,src,color,draw) :
        if i == src:
            print(i,end="")
            return 
        else :
            self.printsol(parent,parent[i],src,color,draw)
            print (i,end="")
            color[i]=(255,255,0)
            time.sleep(0.1)
            draw()
# ob=BFS(0)
# ob.bfs()

