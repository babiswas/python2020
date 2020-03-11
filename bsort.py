def bubble_sort(l):
    for i in range(0,len(l)-1):
       for j in range(0,len(l)-1):
         if l[j]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
 

if __name__=="__main__":
   l=[12,11,10,6,9,8,15]
   bubble_sort(l)
   print(l)
