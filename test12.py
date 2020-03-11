class Graph:
   def __init__(self,vertex):
       self.vertex=vertex
       self.graph=[]

   def add_edge(self,u,v,w):
       self.graph.append([u,v,w])

   def display(self,dist,source):
       for u,v in enumerate(dist):
         print(f"{source}--->{u}={v}")
          

   def bellman_ford(self,source):
       dist=[float("Inf")]*self.vertex
       dist[source]=0
       for i in range(self.vertex-1):
         for u,v,w in self.graph:
            if dist[u]!=float("Inf") and dist[u]+w<dist[v]:
               dist[v]=dist[u]+w
       self.display(dist,source)
       for u,v,w in self.graph:
           if dist[u]+w<dist[v] and dist[u]!=float("Inf"):
                 print(f"{v} is effected by negative cycle")

if __name__=="__main__":
   g=Graph(5)
   g.add_edge(0,1,-1)
   g.add_edge(0,2,4)
   g.add_edge(1,2,3)
   g.add_edge(1,3,2)
   g.add_edge(1,4,2)
   g.add_edge(3,2,5)
   g.add_edge(3,1,1)
   g.add_edge(4,3,-3)
   g.bellman_ford(0)
