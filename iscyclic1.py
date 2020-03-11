from collections import defaultdict

class Graph:
   def __init__(self,vertex):
       self.vertex=vertex
       self.graph=defaultdict(list)

   def add_edges(self,u,v):
       self.graph[u].append(v)
       self.graph[v].append(u)

   def is_cyclic_util(self,visited,parent,u):
       visited[u]=True
       for i in self.graph[u]:
          if not visited[i]:
             if self.is_cyclic_util(visited,u,i):
                return True
          elif i!=parent:
               return True
       return False
       
   def is_cyclic(self):
       visited=[False]*self.vertex
       for i in range(self.vertex):
          if not visited[i]:
             if self.is_cyclic_util(visited,-1,i):
                  return True
       return False

if __name__=="__main__":
   graph=Graph(4)
   graph.add_edges(2,0)
   graph.add_edges(0,1)
   graph.add_edges(2,3)
   print(graph.is_cyclic())

   
   

