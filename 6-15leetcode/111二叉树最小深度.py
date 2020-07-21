# 给定一个二叉树，找出其最小深度。
#
#  最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
#
#  说明: 叶子节点是指没有子节点的节点。
#
#  示例:
#
#  给定二叉树 [3,9,20,null,null,15,7],
#
#      3
#    / \
#   9  20
#     /  \
#    15   7
#
#  返回它的最小深度 2.
#  Related Topics 树 深度优先搜索 广度优先搜索


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        quene = []
        if root.left or root.right:
            quene.append(root)
        depth = 1
        while quene:
            for i in range(len(quene)):
                node = quene.pop(0)
                if not node.left and not node.right:
                    return depth + 1
                if node.left:
                    quene.append(node.left)
                if node.right:
                    quene.append(node.right)
            depth += 1
        return depth


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1

        depth = float("inf")
        if root.left:
            depth = min(self.minDepth(root.left), depth)
        if root.right:
            depth = min(self.minDepth(root.right), depth)

        return depth + 1



# leetcode submit region end(Prohibit modification and deletion)
