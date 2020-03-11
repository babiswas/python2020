def selection_sort(l):
   for i in range(0,len(l)):
      for j in range(i+1,len(l)):
         if l[i]>l[j]:
           l[i],l[j]=l[j],l[i]

if __name__=="__main__":
   l=[12,13,4,5,15,16,2,1]
   selection_sort(l)
   print(l)
