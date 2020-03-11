class A:
  number=12

  def __add__(self,other):
     print("Add method called")
     if isinstance(other,A):
        self.a=self.a+other.a
        self.b=self.b+other.b
     else:
        self.a=self.a+2
        self.b=self.b+2

  def __init__(self,a,b):
      self.a=a
      self.b=b

  def __str__(self):
     print("str called")
     return f"{self.a} and {self.b}"

  def __repr__(self):
     print("repr caled")
     return f"{self.a} and {self.b}"

  @property
  def set_a(self):
      return self.a

  @set_a.setter
  def set_a(self,b):
     self.a=b

if __name__=="__main__":
   a=A(2,3)
   print(a.__dict__)
   setattr(a,'test',2)
   print(a.__dict__)
   print(a.set_a)
   a.set_a=23
   print(a.__dict__)
   print(A.number)
   print(dir(a))
   print(a.__dict__)
   print(a)
   c=A(3,2)
   a+c
   print(a)
   print("Printing static variables")
   print(a.number)
   print(A.number)
   a.number=16
   print(a.__dict__)
   print(dir(a))








   
   

