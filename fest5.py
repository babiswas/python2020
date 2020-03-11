class A:
   def __init__(self,a):
       print("A class executed")
       self.a=a

class C(A):
   def __init__(self,*args):
       super().__init__(args[0])
       self.c=args[1]

   def __str__(self):
      return f"{self.a} and {self.c} are the values"

if __name__=="__main__":
   a=C(2,3)
   print(a)


