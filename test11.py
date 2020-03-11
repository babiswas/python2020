from collections import defaultdict

class Graph:
   def __init__(self,vertex):
      self.vertex=vertex
      self.graph=defaultdict(list)

   def add_edges(self,u,v):
      self.graph[u].append(v)


   def transitive_closure_util(self,u,v,M):
       M[u][v]=1
       for i in self.graph[v]:
          if M[u][i]==0:
             self.transitive_closure_util(u,i,M)
             

   def tarnsitive_closure(self):
       M=[[0 for i in range(self.vertex)] for i in range(self.vertex)]
       visited=[False]*self.vertex
       for i in range(self.vertex):
          self.transitive_closure_util(i,i,M)
       print(M)

if __name__=="__main__":
   graph=Graph(4)
   graph.add_edges(0,2)
   graph.add_edges(2,0)
   graph.add_edges(0,1)
   graph.add_edges(1,2)
   graph.add_edges(2,3)
   graph.add_edges(3,3)
   graph.tarnsitive_closure()


       
