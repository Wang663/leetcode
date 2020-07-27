# 给定一个整数 n，生成所有由 1 ... n 为节点所组成的 二叉搜索树 。
#
#
#
#  示例：
#
#  输入：3
# 输出：
# [
#   [1,null,3,2],
#   [3,2,null,1],
#   [3,1,null,null,2],
#   [2,1,3],
#   [1,null,2,null,3]
# ]
# 解释：
# 以上的输出对应以下 5 种不同结构的二叉搜索树：
#
#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3
#
#
#
#
#  提示：
#
#
#  0 <= n <= 8
#
#  Related Topics 树 动态规划


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """

        def recursion(i, start=1, end=n):
            if start > end:
                return [None]
            res = []
            for i in range(start, end + 1):
                left = recursion(i, start, i-1)
                right = recursion(i, i+1, end)
                for l in left:
                    for r in right:
                        node = TreeNode(i)
                        node.right = r
                        node.left = l
                        res.append(node)
            return res

        return recursion(n) if n else []
# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    solution = Solution()
    trees = solution.generateTrees(3)
    print(len(trees))
