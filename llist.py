class Node:
   def __init__(self,value):
       self.value=value
       self.next=None

class Linklist:
   def __init__(self):
       self.head=None

   def reverse_list(self):
       curr=None
       prev=None
       nex=None
       if self.head:
          curr=self.head
       else:
          return
       while curr.next:
          nex=curr.next
          curr.next=prev
          prev=curr
          curr=nex
       curr.next=prev
       self.head=curr
       nex=None
       prev=None

   def display(self):
      temp=self.head
      while temp.next:
          print(temp.value)
          temp=temp.next
      print(temp.value)

   def add_node(self,value):
      node=Node(value)
      if not self.head:
         self.head=node
      else:
         temp=self.head
         while temp.next:
            temp=temp.next
         temp.next=node

if __name__=="__main__":
   head=Linklist()
   head.add_node(2)
   head.add_node(3)
   head.add_node(4)
   head.display()
   print("Printing second linklist")
   head=Linklist()
   head.add_node(100)
   head.display()
   print("Reversing a link list")
   head=Linklist()
   head.add_node(10)
   head.add_node(11)
   head.add_node(12)
   head.display()
   print("After reverse")
   head.reverse_list()
   head.display()



