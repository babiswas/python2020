def bubble_sort(l):
   for i in range(0,len(l)-1):
     for j in range(0,len(l)-1):
        if l[j]>l[j+1]:
           l[j],l[j+1]=l[j+1],l[j]

if __name__=="__main__":
   l=[12,14,9,10,11,7,9,6]
   bubble_sort(l)
   print(l)
