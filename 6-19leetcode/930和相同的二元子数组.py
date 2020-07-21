# 在由若干 0 和 1 组成的数组 A 中，有多少个和为 S 的非空子数组。
#
#
#
#  示例：
#
#  输入：A = [1,0,1,0,1], S = 2
# 输出：4
# 解释：
# 如下面黑体所示，有 4 个满足题目要求的子数组：
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
#
#
#
#
#  提示：
#
#
#  A.length <= 30000
#  0 <= S <= A.length
#  A[i] 为 0 或 1
#
#  Related Topics 哈希表 双指针


# leetcode submit region begin(Prohibit modification and deletion)
import collections
class Solution(object):
    def numSubarraysWithSum(self, A, S):
        """
        垃圾代码
        :type A: List[int]
        :type S: int
        :rtype: int
        """
        # self.res = 0
        # for i in range(len(A)):
        #     if A[i] == S:
        #         self.res += 1
        #     self.num = A[i]
        #     for j in range(i+1,len(A)):
        #         self.num += A[j]
        #         if self.num == S:
        #             self.res += 1
        # return self.res

        # p = [

class Solution(object):
    def numSubarraysWithSum(self, A, S):
        """前缀和"""

        P = [0]
        for x in A: P.append(P[-1] + x)
        count = collections.Counter()
        print(P)
        ans = 0
        for x in P:
            ans += count[x]
            count[x + S] += 1
            print(count,ans)
        return ans



if __name__ == '__main__':
    solution = Solution()
    res = solution.numSubarraysWithSum([1, 0, 1, 0, 1], 2)
    print(res)

# leetcode submit region end(Prohibit modification and deletion)
