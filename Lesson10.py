import json
class A:
   test1="hello"
   def __init__(self,a,b):
       self.a=a
       self.b=b

   def display(self,str1):
       return f"{str1} displayed"

if __name__=="__main__":
   a=A(2,3)
   print(a.__dict__)
   print(json.dumps(a.__dict__))
   print(a.test1)
   print(A.test1)
   a.test1="bello"
   print(a.test1)
   print(a.__dict__)




  