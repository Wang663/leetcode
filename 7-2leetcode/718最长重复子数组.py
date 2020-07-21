# 给两个整数数组 A 和 B ，返回两个数组中公共的、长度最长的子数组的长度。
#
#
#
#  示例：
#
#  输入：
# A: [1,2,3,2,1]
# B: [3,2,1,4,7]
# 输出：3
# 解释：
# 长度最长的公共子数组是 [3, 2, 1] 。
#
#
#
#
#  提示：
#
#
#  1 <= len(A), len(B) <= 1000
#  0 <= A[i], B[i] < 100
#
#  Related Topics 数组 哈希表 二分查找 动态规划


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    """
    滑动窗口
    """
    def findLength(self, A: List[int], B: List[int]) -> int:
        def maxLength(addA: int, addB: int, length: int) -> int:
            ret = k = 0
            for i in range(length):
                if A[addA + i] == B[addB + i]:
                    k += 1
                    ret = max(ret, k)
                else:
                    k = 0
            return ret

        n, m = len(A), len(B)
        ret = 0
        for i in range(n):
            length = min(m, n - i)
            ret = max(ret, maxLength(i, 0, length))
        for i in range(m):
            length = min(n, m - i)
            ret = max(ret, maxLength(0, i, length))
        return ret

    """
    动态规划
    """

    def findLength(self, A: List[int], B: List[int]) -> int:
        res = 0
        arr = [[0 for i in range(len(A)+1)] for j in range(len(B)+1)]

        for i in range(1,len(B)+1):
            for j in range(1, len(A) + 1):
                if A[j - 1] == B[i - 1]:
                    arr[i][j] = arr[i - 1][j - 1] + 1
                else:
                    arr[i][j] = 0
                res = max(res,arr[i][j])
        return res


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    solution = Solution()
    res = solution.findLength([1, 2, 3, 2, 1], [3, 2, 1, 4, 7])
    print(res)
