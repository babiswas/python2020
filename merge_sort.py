def merge_sort(l,start,end):
   if start<end:
      mid=(start+end)//2
      merge_sort(l,start,mid)
      merge_sort(l,mid+1,end)
      merge(l,start,end,mid)

def merge(l,start,end,mid):
    n1=mid-start+1
    n2=end-mid
    a=[0]*n1
    b=[0]*n2
    for i in range(0,n1):
        a[i]=l[start+i]
    for j in range(0,n2):
        b[j]=l[mid+1+j]
    i,j=0,0
    k=start
    while i!=n1 and j!=n2:
        if a[i]>b[j]:
          l[k]=b[j]
          k=k+1
          j=j+1
        else:
          l[k]=a[i]
          k=k+1
          i=i+1
    while i!=n1:
       l[k]=a[i]
       k=k+1
       i=i+1
    while j!=n2:
       l[k]=b[j]
       k=k+1
       j=j+1


if __name__=="__main__":
  l=[12,13,14,15,9,10,7,6]
  merge_sort(l,0,7)
  print(l)

  
    
    