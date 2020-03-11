def merge_sort(l,start,end):
    if start<end:
       mid=(start+end)//2
       merge_sort(l,start,mid)
       merge_sort(l,mid+1,end)
       merge(l,start,end,mid)

def merge(l,start,end,mid):
    n1=mid-start+1
    n2=end-mid
    A=[0]*n1
    B=[0]*n2
    for i in range(0,n1):
       A[i]=l[start+i]
    for i in range(0,n2):
       B[i]=l[mid+1+i]
    i=0
    j=0
    k=start
    while i!=n1 and j!=n2:
        if A[i]<B[j]:
          l[k]=A[i]
          k=k+1
          i=i+1
        else:
          l[k]=B[j]
          k=k+1
          j=j+1
    while i!=n1:
       l[k]=A[i]
       k=k+1
       i=i+1
    while j!=n2:
       l[k]=B[j]
       k=k+1
       j=j+1

if __name__=="__main__":
   l=[12,11,10,9,4,15,1]
   merge_sort(l,0,6)
   print(l)

    
    
