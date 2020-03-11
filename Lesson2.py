class A:
   def __init__(self,a,b):
      self.a=a
      self.b=b

   def __add__(self,other):
       if type(other)==int:
          self.a=self.a+other
          self.b=self.b+other
       return self

   def __str__(self):
     return f"{self.a} and {self.b}"
   
   def __radd__(self,other):
       if type(other)==int:
          if other==0:
             return self
          else:
             return self.__add__(other)

if __name__=="__main__":
   a=A(3,4)
   print(a)
   print(3+a)




          
