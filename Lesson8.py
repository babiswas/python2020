class A:
   def __init__(self):
       pass

class B:
   def __init__(self):
       pass

class C(A,B):
   def __init__(self):
      A.__init__(self)
      B.__init__(self)

if __name__=="__main__":
   print(issubclass(C,A))
   print(issubclass(C,B))
   print(issubclass(A,C))
