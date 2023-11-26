
class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
        
class Tree:
    def createNode(self, data):
        return Node(data)

    def insert(self, node, data):
        if node is None:
            return self.createNode(data)
        
        if data < node.data:
            node.left = self.insert(node.left, data)
        else:
            node.right = self.insert(node.right, data)
        return node
    
    def inorder_traversal(self, root):
        if root is not None:
            self.inorder_traversal(root.left)
            print(root.data)
            self.inorder_traversal(root.right)

    def inorder_loop(self, root):
        ans=[]
        stack=[]
        cur=root
        while stack or cur:
            if cur:
                stack.append(cur)
                cur=cur.left
            else:
                cur=stack.pop()
                ans.append(cur.val)
                cur=cur.right
        return ans

tr = Tree()
r = tr.createNode(5)
tr.insert(r,2)
tr.insert(r,10)
tr.insert(r,7)
tr.insert(r,15)
tr.insert(r,12)
tr.insert(r,20)
tr.insert(r,30)
tr.insert(r,6)
tr.insert(r,8)
tr.inorder_traversal(r)