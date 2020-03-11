class Cell:
   def __init__(self,x,dist):
       self.x=x
       self.dist=dist


def isinside(x,N):
    if x<0 or x>=N:
       return False
    return True

def min_steps(l,start):
    dx=[-1,1]
    visited=[False for i in range(len(l))]
    queue=[]
    queue.append(Cell(start,0))
    visited[start]=True
    while queue:
        m=queue.pop(0)
        if m.x==(len(l)-1):
            return m.dist
        for i in range(2):
           X=m.x+dx[i]
           if isinside(X,len(l)) and visited[X]==False:
              queue.append(Cell(X,m.dist+1))
        n=[i for i,j in enumerate(l) if j==l[m.x]]
        for i in n:
           if visited[i]==False:
              queue.append(Cell(i,m.dist+1))
              visited[i]=True

if __name__=="__main__":
   l=[0, 1, 2, 3, 4, 5, 6, 7, 5, 4, 3, 6, 0, 1, 2, 3, 4, 5, 7]
   print(min_steps(l,0))
