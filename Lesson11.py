class A:
   def __new__(cls,*args):
       print("new method executed")
       return object.__new__(cls)
   def __init__(self,a,b):
      self.a=a
      self.b=b

if __name__=="__main__":
   a=A(1,2)
   print(a.__dict__)
