class A:
   def __init__(self,a,b):
       self.a=a
       self.b=b

   def __iter__(self):
       self.a=10
       self.b=0
       return self

   def __next__(self):
       if self.b<self.a:
          print(self.b)
          self.b=self.b+1
       else:
          raise StopIteration

if __name__=="__main__":
   a=A(0,0)
   a.__iter__()
   next(a)
   next(a)
   next(a)
   next(a)
   next(a)
   next(a)
   next(a)
   next(a)
   next(a)
   next(a)
   next(a)
   next(a)
