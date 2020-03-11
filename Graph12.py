class Cell:
   def __init__(self,x,y,dist):
       self.x=x
       self.y=y
       self.dist=dist

def isinside(x,y,M,N):
    if x>=N or x<0:
       return False
    if y>=N or y<0:
       return False
    if M[x][y]=='#':
       return False
    return True

def find_short_path(tar,pos,M):
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    queue=[]
    visited=[[False for i in range(len(M[0]))] for i in range(len(M[0]))]
    queue.append(Cell(pos[0],pos[1],0))
    visited[pos[0]][pos[1]]=True
    while queue:
       m=queue.pop(0)
       if m.x==tar[0] and m.y==tar[1]:
           return m.dist
       for i in range(4):
             X=m.x+dx[i]
             Y=m.y+dy[i]
             if isinside(X,Y,M,len(M[0])):
                if not visited[X][Y]:
                   queue.append(Cell(X,Y,m.dist+1))
                   visited[X][Y]=True

if __name__=="__main__":
  M=[[3,3,1,'#'],[3,'#',3,3],['E',3,'#',3],['#',3,3,3]]
  pos=[0,2]
  tar=[2,0]
  print(find_short_path(tar,pos,M))
    

