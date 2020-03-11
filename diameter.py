class Node:
   def __init__(self,value):
       self.value=value
       self.left=None
       self.right=None

def height(node):
    if node:
       queue=[]
       queue.append(node)
       count=0
       while queue:
           queue_len=len(queue)
           if queue_len:
              count=count+1
           while queue_len:
               m=queue.pop(0)
               if m.left:
                  queue.append(m.left)
               if m.right:
                  queue.append(m.right)
               queue_len=queue_len-1
       return count
    else:
      return 0

def diameter(node):
   right=0
   left=0
   lheight=0
   rheight=0
   if not node:
      return 0
   if node.left:
      left=diameter(node.left)
   if node.right:
      right=diameter(node.right)
   if node.left:
      lheight=height(node.left)
   if node.right:
      rheight=height(node.right)
   return max(lheight+rheight+1,max(left,right))
   

if __name__=="__main__":
   node=Node(12)
   node.left=Node(15)
   node.left.right=Node(21)
   node.left.left=Node(25)
   node.right=Node(20)
   node.right.left=Node(19)
   node.right.right=Node(26)
   node.right.right.right=Node(30)
   node.right.right.right.right=Node(45)
   node.right.right.right.right.right=Node(62)
   print(diameter(node))
