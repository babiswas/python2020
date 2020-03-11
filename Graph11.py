from collections import defaultdict
import sys

class Graph:
   def __init__(self,vertex):
       self.vertex=vertex
       self.graph=defaultdict(list)

   def add_edges(self,u,v):
       self.graph[u].append(v)

   def BFS(self,u,level):
       if level==1:
         print(u)
         return
       visited=[False]*self.vertex
       queue=[]
       queue.append(u)
       count=1
       while queue:
          len_queue=len(queue)
          while len_queue:
             m=queue.pop(0)
             for i in self.graph[m]:
                if not visited[i]:
                   queue.append(i)
                   visited[i]=True
             len_queue=len_queue-1
          count=count+1
          if level==count:
             print(queue)

if __name__=="__main__":
   graph=Graph(4)
   graph.add_edges(0,2)
   graph.add_edges(2,0)
   graph.add_edges(1,2)
   graph.add_edges(0,1)
   graph.add_edges(2,3)
   graph.add_edges(3,3)
   graph.BFS(2,1)