class A:
  def __init__(self,a):
      self.a=a

class B:
  def __init__(self,b):
     self.b=b


class C(A):
   def __init__(self,*args):
      super().__init__(args[0])
      self.c=args[1]

class D(A,B):
   def __init__(self,*args):
       A.__init__(self,args[0])
       B.__init__(self,args[1])
       self.d=args[2]

if __name__=="__main__":
   a=A(1)
   b=B(2)
   d=D(3,4,5)
   print(a.__dict__)
   print(b.__dict__)
   print(d.__dict__)
