class Cell:
   def __init__(self,x,y,dist):
       self.x=x
       self.y=y
       self.dist=dist


def isinside(x,y,N,M):
   if x<0 or x>=N:
       return False
   if y<0 or y>=N:
       return False
   if M[x][y]=='#':
       return False
   return True

def find_shortest_path(pos,tar,M,N):
   dx=[1,-1,0,0]
   dy=[0,0,-1,1]
   queue=[]
   queue.append(Cell(pos[0],pos[1],0))
   visited=[[False for i in range(N)] for i in range(N)]
   while queue:
       m=queue.pop(0)
       if m.x==tar[0] and m.y==tar[1]:
            return m.dist
       for i in range(4):
           X=m.x+dx[i]
           Y=m.y+dy[i]
           if isinside(X,Y,N,M):
              if visited[X][Y]==False:
                 queue.append(Cell(X,Y,m.dist+1))
                 visited[X][Y]=True

if __name__=="__main__":
  N=4
  M=[[3,3,1,'#'],[3,'#',3,3],['E',3,'#',3],['#',3,3,3]]
  pos=[0,2]
  tar=[2,0]
  print(find_shortest_path(pos,tar,M,N))