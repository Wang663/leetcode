# 实现函数double Power(double base, int exponent)，求base的exponent次方。不得使用库函数，同时不需要考虑大数
# 问题。
#
#
#
#  示例 1:
#
#  输入: 2.00000, 10
# 输出: 1024.00000
#
#
#  示例 2:
#
#  输入: 2.10000, 3
# 输出: 9.26100
#
#
#  示例 3:
#
#  输入: 2.00000, -2
# 输出: 0.25000
# 解释: 2-2 = 1/22 = 1/4 = 0.25
#
#
#
#  说明:
#
#
#  -100.0 < x < 100.0
#  n 是 32 位有符号整数，其数值范围是 [−231, 231 − 1] 。
#
#
#  注意：本题与主站 50 题相同：https://leetcode-cn.com/problems/powx-n/
#  Related Topics 递归


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if x == 0:
            return 0
        if n < 0:
            x = 1/x
            n = -n
        res = 1
        while n:
            if n&1:
                res = res * x
            x *=x
            n = n >> 1
        return res
# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    solution = Solution()
    my_pow = solution.myPow(2.1, 2)
    print(my_pow)
