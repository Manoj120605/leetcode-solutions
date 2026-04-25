class Solution:
    def sortedListToBST(self, head):
        
        # Step 1: get length
        def getSize(node):
            size = 0
            while node:
                size += 1
                node = node.next
            return size
        
        size = getSize(head)
        self.head = head
        
        # Step 2: build BST using inorder simulation
        def build(l, r):
            if l > r:
                return None
            
            mid = (l + r) // 2
            
            # build left subtree
            left = build(l, mid - 1)
            
            # root node
            root = TreeNode(self.head.val)
            self.head = self.head.next
            
            # build right subtree
            right = build(mid + 1, r)
            
            root.left = left
            root.right = right
            
            return root
        
        return build(0, size - 1)