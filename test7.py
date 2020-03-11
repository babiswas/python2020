from collections import defaultdict

class Graph:
   def __init__(self,vertex):
       self.vertex=vertex
       self.graph=defaultdict(list)

   def add_edges(self,u,v):
       self.graph[u].append(v)

   def iscyclic_util(self,visited,recstack,u):
       visited[u]=True
       recstack[u]=True
       for i in self.graph[u]:
           if not visited[i]:
              if self.iscyclic_util(visited,recstack,i):
                 return True
           elif recstack[i]==True:
                return True
       recstack[u]=False
       return False

   def iscyclic(self):
       visited=[False]*self.vertex
       recstack=[False]*self.vertex
       for i in range(self.vertex):
           if not visited[i]:
               if self.iscyclic_util(visited,recstack,i):
                  return True
       return False

if __name__=="__main__":
   graph=Graph(6)
   graph.add_edges(5,0)
   graph.add_edges(4,0)
   graph.add_edges(4,1)
   graph.add_edges(5,2)
   graph.add_edges(2,3)
   graph.add_edges(3,1)
   print(graph.iscyclic())
   print("Another Graph")
   graph=Graph(4)
   graph.add_edges(0,2)
   graph.add_edges(2,0)
   graph.add_edges(0,1)
   graph.add_edges(1,2)
   graph.add_edges(2,3)
   graph.add_edges(3,3)
   print(graph.iscyclic())


              