def BFS(element,al):
    visited=[False]*len(al)
    queue=[]
    queue.append(element)
    visited[element]=True
    while queue:
         m=queue.pop(0)
         print(m)
         for i in al[m]:
            if visited[i]==False:
               queue.append(i)
               visited[i]=True

if __name__=="__main__":
   al=[[1,2],[2],[0,3],[3]]
   BFS(2,al)

    