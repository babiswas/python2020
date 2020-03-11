class A:
   def __init__(self,a,b):
       self.x=a
       self.y=b
   def __str__(self):
      return f"{self.x} and {self.y}"

class C(A):
   def __init__(self,*args):
       super().__init__(args[0],args[1])
       self.z=args[2]
   def __str__(self):
       return f"{self.x} {self.y}  {self.z}"

if __name__=="__main__":
   a=C(1,2,3,4)
   print(a)
   print(a.x)
   print(a.y)
   print(a.__dict__)
   b=A(5,6)
   print(b.__dict__)
   print("Is C subclass of A")
   print(issubclass(C,A))
   print("Is A subclass of C")
   print(issubclass(A,C))


