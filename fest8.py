from abc import ABC,abstractmethod

class C(ABC):
   @abstractmethod
   def help(self):
      print("please help")
   @abstractmethod
   def wait(self):
      print("Waited")


class B(C):
  def __init__(self):
      self.name="Hello"
  def __str__(self):
      return f"{self.name}"

if __name__=="__main__":
   b=B()
   print(b)


