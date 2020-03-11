class Vector:
   def __init__(self,x,y):
      self.x=x
      self.y=y
   def set(self,x,y):
      self.x=x
      self.y=y
   def __repr__(self):
      return "{} is x and {} is y".format(self.x,self.y)
   @property
   def set_x(self):
     return self.x

   @property
   def set_y(self):
     return self.y

   @set_x.setter
   def set_x(self,a):
      self.x=a

   @set_y.setter
   def set_y(self,b):
      self.y=b

def main():
   v=Vector(2,3)
   v.set(5,6)
   print(v)

if __name__=="__main__":
   main()
   a=Vector(11,16)
   print(a)
   print(a.__dict__)
   a.set_x=21
   print(a.__dict__)
   a.set_y=31
   print(a.__dict__)
   