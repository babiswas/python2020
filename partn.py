def partition(l,start,end):
    track=start-1
    pivot=l[end]
    for i in range(0,end):
        if l[i]<pivot:
           track=track+1
           l[i],l[track]=l[track],l[i]
    track=track+1
    l[track],l[end]=pivot,l[track]
    return track


if __name__=="__main__":
   l=[-1,2,3,-4,3,-7,0]
   print(partition(l,0,6))
   print(l)

 