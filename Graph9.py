from collections import defaultdict

class Graph:
   def __init__(self,vertex):
       self.vertex=vertex
       self.graph=defaultdict(list)

   def add_edges(self,u,v):
       self.graph[u].append(v)

   def mother_vertex_util(self,visited,u):
       visited[u]=True
       for i in self.graph[u]:
          if not visited[i]:
              self.mother_vertex_util(visited,i)
              
   def mother_vertex(self):
      v=0
      visited=[False]*self.vertex
      for i in range(self.vertex):
         if not visited[i]:
            self.mother_vertex_util(visited,i)
            v=i
      visited=[False]*self.vertex
      self.mother_vertex_util(visited,v)
      if False not in visited:
          print(f"{v} is the mother vertex")
      else:
          print("Couldn't find mother vertex")

if __name__=="__main__":
   graph=Graph(4)
   graph.add_edges(0,2)
   graph.add_edges(2,0)
   graph.add_edges(0,1)
   graph.add_edges(1,2)
   graph.add_edges(2,3)
   graph.add_edges(3,3)
   print(graph.mother_vertex())

