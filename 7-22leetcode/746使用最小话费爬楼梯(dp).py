# 数组的每个索引作为一个阶梯，第 i个阶梯对应着一个非负数的体力花费值 cost[i](索引从0开始)。
#
#  每当你爬上一个阶梯你都要花费对应的体力花费值，然后你可以选择继续爬一个阶梯或者爬两个阶梯。
#
#  您需要找到达到楼层顶部的最低花费。在开始时，你可以选择从索引为 0 或 1 的元素作为初始阶梯。
#
#  示例 1:
#
#  输入: cost = [10, 15, 20]
# 输出: 15
# 解释: 最低花费是从cost[1]开始，然后走两步即可到阶梯顶，一共花费15。
#
#
#  示例 2:
#
#  输入: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
# 输出: 6
# 解释: 最低花费方式是从cost[0]开始，逐个经过那些1，跳过cost[3]，一共花费6。
#
#
#  注意：
#
#
#  cost 的长度将会在 [2, 1000]。
#  每一个 cost[i] 将会是一个Integer类型，范围为 [0, 999]。
#
#  Related Topics 数组 动态规划


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """

        # f1 = f2 = 0
        # for x in reversed(cost):
        #     f1, f2 = x + min(f1, f2), f1
        # return min(f1, f2)

        result = [0 for _ in range(len(cost))]
        result[0] = cost[0]
        result[1] = cost[1]
        for j in range(2, len(result)):
            result[j] = min(result[j - 1], result[j - 2]) + cost[j]
        return min(result[-2], result[-1])




if __name__ == '__main__':
    solution = Solution()
    costs = [10, 15, 20]
    res = solution.minCostClimbingStairs(costs)
    print(res)


