# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
       self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        """
        从前序与中序遍历序列构造二叉树
        """
        if not preorder or not inorder:
            return
        root = TreeNode(preorder[0])
        pos = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:pos+1], inorder[:pos])
        root.right = self.buildTree(preorder[pos+1:], inorder[pos+1:])
        return root