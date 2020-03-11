class Node:
   def __init__(self,value):
       self.value=value
       self.left=None
       self.right=None


def distance(root,x):
    dist=-1
    dist1=0
    dist2=0
    if not root:
       return -1
    elif root==x:
       return 0
    else:
      if node.left:
         dist1=distance(node.left,x)
      if node.right:
         dist2=distance(node.right,x)
      if dist1>0:
         dist=dist1+1
      elif dist2>0:
         dist=dist2+1
      return dist

if __name__=="__main__":
   node=Node(12)
   node.left=Node(21)
   node.right=Node(13)
   node.right.left=Node(17)
   node.right.right=Node(19)
   node.left.right=Node(25)
   node.left.left=Node(31)
   node.right.right.left=Node(40)
   node.right.right.right=Node(34)
   print(distance(node,node.right.right.left))

        
        
