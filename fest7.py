from contextlib import contextmanager

@contextmanager
def fun(name):
   try:
      m=open(name,'w')
      yield m
   finally:
      m.close()

if __name__=="__main__":
   with fun("test2.txt") as b:
       b.write("Hello world")
       b.write("Hi world")
