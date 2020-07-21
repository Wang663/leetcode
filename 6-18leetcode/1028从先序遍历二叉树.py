# 我们从二叉树的根节点 root 开始进行深度优先搜索。
#
#  在遍历中的每个节点处，我们输出 D 条短划线（其中 D 是该节点的深度），然后输出该节点的值。（如果节点的深度为 D，则其直接子节点的深度为 D + 1。
# 根节点的深度为 0）。
#
#  如果节点只有一个子节点，那么保证该子节点为左子节点。
#
#  给出遍历输出 S，还原树并返回其根节点 root。
#
#
#
#  示例 1：
#
#
#
#  输入："1-2--3--4-5--6--7"
# 输出：[1,2,5,3,4,6,7]
#
#
#  示例 2：
#
#
#
#  输入："1-2--3---4-5--6---7"
# 输出：[1,2,5,3,null,6,null,4,null,7]
#
#
#  示例 3：
#
#
#
#  输入："1-401--349---90--88"
# 输出：[1,401,null,349,88,90]
#
#
#
#
#  提示：
#
#
#  原始树中的节点数介于 1 和 1000 之间。
#  每个节点的值介于 1 和 10 ^ 9 之间。
#
#  Related Topics 树 深度优先搜索


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
import collections


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def recoverFromPreorder(self, S):
        """
        :type S: str
        :rtype: TreeNode
        """
        # 垃圾的代码
        dict_ = collections.defaultdict(list)
        start = 0
        while S:
            if S[start] != "-":
                start +=1
            else:
                break
        dict_[0].append(TreeNode(S[:start]))
        num = 0
        tmp = ""
        for i in S[start:]:
            if i != "-":
                tmp = tmp+i
            else:
                if len(tmp):
                    current_node = TreeNode(tmp)
                    node = dict_[num - 1][-1]
                    if not node.left:
                        node.left = current_node
                    else:
                        node.right = current_node
                    dict_[num].append(current_node)
                    tmp = ""
                    num = 0
                num += 1

        if len(tmp) != 0:
            current_node = TreeNode(tmp)
            node = dict_[num - 1][-1]
            if not node.left:
                node.left = current_node
            else:
                node.right = current_node

        root = dict_[0][0]
        return root

    # 优秀的代码
    def recoverFromPreorder(self, S):
        stack, i = [], 0
        while i < len(S):
            level, val = 0, ""
            while i < len(S) and S[i] == '-':
                level, i = level + 1, i + 1
            while i < len(S) and S[i] != '-':
                val, i = val + S[i], i + 1
            while len(stack) > level:
                stack.pop()
            node = TreeNode(val)
            if stack and stack[-1].left is None:
                stack[-1].left = node
            elif stack:
                stack[-1].right = node
            stack.append(node)
        return stack[0]


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    solution = Solution()
    res = solution.recoverFromPreorder("1-401--349---90--88")
    print(res)
