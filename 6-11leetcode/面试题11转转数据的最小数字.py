# 把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。例如，数组 [3,4,5,1,2
# ] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。
#
#  示例 1：
#
#  输入：[3,4,5,1,2]
# 输出：1
#
#
#  示例 2：
#
#  输入：[2,2,2,0,1]
# 输出：0
#
#
#  注意：本题与主站 154 题相同：https://leetcode-cn.com/problems/find-minimum-in-rotated-sor
# ted-array-ii/
#  Related Topics 二分查找


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def minArray(self, numbers: List[int]) -> int:
        if not numbers:
            return None
        last_num = numbers[0]
        for i in numbers[1:]:
            if i < last_num:
                return i
            if i > last_num:
                continue
        return last_num


class Solution:
    def minArray(self, numbers: [int]) -> int:
        i, j = 0, len(numbers) - 1
        while i < j:
            m = (i + j) // 2
            if numbers[m] > numbers[j]:
                i = m + 1
            elif numbers[m] < numbers[j]:
                j = m
            else:
                j -= 1
        return numbers[i]


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    solution = Solution()
    res = solution.minArray([3, 5, 1])
    print(res)
    res = solution.minArray([1, 3, 5])
    print(res)
