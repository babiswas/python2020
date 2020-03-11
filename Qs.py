
def partition(l,start,end):
    pivot=l[end]
    track=start-1
    for i in range(start,end):
        if l[i]<pivot:
           track=track+1
           l[i],l[track]=l[track],l[i]
    track=track+1
    l[track],l[end]=l[end],l[track]
    return track

def Qsort(l,start,end):
    if start<end:
       index=partition(l,start,end)
       Qsort(l,start,index-1)
       Qsort(l,index+1,end)


if __name__=="__main__":
   l=[12,14,11,10,7,9,3]
   Qsort(l,0,6)
   print(l)



