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
    
    
    
    
    # DFS
    
    def inorder_traversal(self, root):
        if root is not None:
            self.inorder_traversal(root.left)
            print(root.data)
            self.inorder_traversal(root.right)
            
    def preorder_traversal(self, root):
        if root:
            print(root.data)
            self.preorder_traversal(root.left)
            self.preorder_traversal(root.right)
        
    def postorder_traversal(self, root):
        if root:
            self.postorder_traversal(root.left)
            self.postorder_traversal(root.right)
            print(root.data)

    # BFS
    def BFS(self, root):
        queue = []
        queue.append(root)
        while queue:
            current = queue[0]
            queue = queue[1:]
            print(current.data)
            
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
            
    # find node
    def find_node(self, root, val):
        if root.data>val and root.left:
            return self.find_node(root.left, val)
        if root.data<val and root.right:
            return self.find_node(root.right, val)
        
        return root.data == val

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
print('INAORDER TRAVERSAL')
tr.inorder_traversal(r)
print('------')
print('PREORDER TRAVERSAL')
tr.preorder_traversal(r)
print('------')
print('POSTORDER TRAVERSAL')
tr.postorder_traversal(r)
print('------')
print('BFS')
tr.BFS(r)
print('find -----')
print(tr.find_node(r,11))
# print(r.data, r.left.data, r.right.data)
# print(r.left.left.data, r.left.right.data)
# # print(r.right.left.data, r.right.right.data)