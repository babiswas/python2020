class A:
   def __init__(self,a):
       print("A executed")
       self.a=a

class B:
   def __init__(self,b):
      print("B executed")
      self.b=b


class C(A,B):
   def __init__(self,*args):
      A.__init__(self,args[0])
      B.__init__(self,args[1])

   def __str__(self):
      return f"{self.a} and {self.b}"

if __name__=="__main__":
   c=C(4,5)
   print(c)
