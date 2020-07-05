class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        """
        N 叉树的前序遍历
        """
        res = []
        if not root:
            return res
        res.append(root.val)
        for child in root.children:
            res.extend(self.preorder(child))
        return res