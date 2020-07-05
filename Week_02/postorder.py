class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        """
        N 叉树的后序遍历
        """
        res = []
        if not root:
            return res
        for child in root.children:
            res.extend(self.postorder(child))
        res.append(root.val)
        return res