class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        """
        N叉树的层序遍历
        """
        res = []
        if not root:
            return res        
        pre_layer = [root]

        while pre_layer:
            cur_layer = []
            res.append([])
            for node in pre_layer:
                res[-1].append(node.val)
                cur_layer.extend(node.children)
            pre_layer = cur_layer
        return res