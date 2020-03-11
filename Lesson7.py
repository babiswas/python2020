class A:
   """Best is the movie"""

   def __init__(self):
      self.name="Bello"

   name="Bapan"

   @staticmethod
   def foo(str1):
      return str1

   @classmethod
   def doo(cls):
      print(cls.name)

   def fun(self):
      print(self.name)

if __name__=="__main__":
   a=A()
   A.fun(a)
   A.doo()
   print(A.foo("test1"))
   print(a.__dict__)
   print(a.__doc__)

