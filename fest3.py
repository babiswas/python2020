class A:
   def __init__(self,name):
       self.name=name
   def __enter__(self):
      self.m=open(self.name,'w')
      return self.m
   def __exit__(self,a,b,c):
      if self.m:
         self.m.close()

if __name__=="__main__":
  with open("test1.txt",'w') as b:
      b.write("Hello World\n")
      b.write("I am Bapan\n")
      b.write("I am alone at office\n")

      
      