class Solution:
    def inorderTraversal(self, root):
        """
        二叉树的中序遍历
        """
        res = []
        def travel(root):
            if not root:
                return 
            travel(root.left)
            res.append(root.val)
            travel(root.right)
        travel(root)
        return res