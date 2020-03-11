import queue

class Node:
   def __init__(self,x,dist):
       self.x=x
       self.dist=dist


def min_op(x,y):
   que=queue.Queue()
   s=set()
   node=Node(x,0)
   que.put(node)
   while queue:
       m=que.get()
       if m.x==y:
          return m.dist
       s.add(m.x)
       X=m.x*2
       Y=m.x-1
       if X==y or Y==y:
          return m.dist+1
       if X not in s:
          que.put(Node(X,m.dist+1))
       if Y>=0 and Y not in s:
          que.put(Node(Y,m.dist+1))

if __name__=="__main__":
   print(min_op(4,7))
             
       
          