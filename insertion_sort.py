def insertion_sort(l,start,end):
   for i in range(start+1,end+1):
      current=l[i]
      hole=i
      while l[hole-1]>current and hole>0:
          l[hole]=l[hole-1]
          hole=hole-1
      l[hole]=current
   return l

if __name__=="__main__":
   l=[12,15,14,9,10,7,6]
   insertion_sort(l,0,6)
   print(l)
