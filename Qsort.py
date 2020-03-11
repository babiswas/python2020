def partition(l,start,end):
    trace=start-1
    pivot=l[end]
    for i in range(start,end):
        if l[i]<pivot:
          trace=trace+1
          l[i],l[trace]=l[trace],l[i]
    trace=trace+1
    l[trace],l[end]=pivot,l[trace]
    return trace

def Qsort(l,start,end):
    if start<end:
       index=partition(l,start,end)
       Qsort(l,start,index-1)
       Qsort(l,index+1,end)
if __name__=="__main__":
   l=[12,11,10,6,9,7,15]
   Qsort(l,0,6)
   print(l)



           
      