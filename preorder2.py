class Node:
   def __init__(self,value):
       self.value=value
       self.left=None
       self.right=None

   def preorder(self):
      if self:
         if self.left:
            self.left.preorder()
         print(self.value)
         if self.right:
            self.right.preorder()

   def insert(self,value):
      if self.value>value:
         if self.left:
            self.left.insert(value)
         else:
            self.left=Node(value)
      elif self.value<value:
         if self.right:
            self.right.insert(value)
         else:
            self.right=Node(value)
      else:
         print("Duplication not allowed")

   def preorder(self):
     root=self
     if not root:
        return
     else:
         while root:
            if root.left==None:
               print(root.value)
               root=root.right
            else:
               curr=root.left
               while curr.right and curr.right!=root:
                   curr=curr.right
               if curr.right==root:
                    curr.right=None
                    print(root.value)
                    root=root.right
               else:
                    curr.right=root
                    root=root.left
if __name__=="__main__":
   node=Node(12)
   node.insert(21)
   node.insert(14)
   node.insert(25)
   node.insert(17)
   node.insert(13)
   node.insert(7)
   node.insert(1)
   node.insert(0)
   node.insert(4)
   node.insert(9)
   node.insert(8)
   node.insert(10)
   node.preorder()
