def arrange(arr):
   brr=[-1]*len(arr)
   for i in range(len(arr)):
      if i in arr:
         brr[i]=i
   return brr



      

if __name__=="__main__":
   l=[-1, -1, 6, 1, 9, 3, 2, -1, 4, -1]
   print(arrange(l))
   