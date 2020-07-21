# 给定一个二叉树，判断其是否是一个有效的二叉搜索树。
#
#  假设一个二叉搜索树具有如下特征：
#
#
#  节点的左子树只包含小于当前节点的数。
#  节点的右子树只包含大于当前节点的数。
#  所有左子树和右子树自身必须也是二叉搜索树。
#
#
#  示例 1:
#
#  输入:
#     2
#    / \
#   1   3
# 输出: true
#
#
#  示例 2:
#
#  输入:
#     5
#    / \
#   1   4
#      / \
#     3   6
# 输出: false
# 解释: 输入为: [5,1,4,null,null,3,6]。
#      根节点的值为 5 ，但是其右子节点值为 4 。
#
#  Related Topics 树 深度优先搜索


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # 递归判断
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.res = True
        self.recursion(root,float("-inf"),float("inf"))
        return self.res

    def recursion(self,node,lower,upper):
        if self.res:
            if node :
                return
            if node.val < lower or node.val > upper:
                self.res = False
            self.recursion(node.left,lower,node.val)
            self.recursion(node.right, node.val, upper)


    # 中序遍历
    def isValidBST(self, root):
        self.node_value = []
        self.recursion(root)
        if len(self.node_value) == 1:
            return True
        for i in range(1,len(self.node_value)):
            if self.node_value[i] < self.node_value[i-1]:
                return False
        return True

    def recursion(self,node):
        if not node:
            return
        self.recursion(node.left)
        self.node_value.append(node.value)
        self.recursion(node.right)





# leetcode submit region end(Prohibit modification and deletion)
