class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        """
        二叉树的前序遍历
        """
        res = []
        def travel(root):
            if not root:
                return 
            res.append(root.val)
            travel(root.left)
            travel(root.right)
        travel(root)
        return res