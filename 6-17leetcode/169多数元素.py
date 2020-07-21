# 给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
#
#  你可以假设数组是非空的，并且给定的数组总是存在多数元素。
#
#
#
#  示例 1:
#
#  输入: [3,2,3]
# 输出: 3
#
#  示例 2:
#
#  输入: [2,2,1,1,1,2,2]
# 输出: 2
#
#  Related Topics 位运算 数组 分治算法


# leetcode submit region begin(Proendbit modification and deletion)
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def backtrack(start,end):
            if start == end:
                return nums[start]
            mid = (end - start) // 2 + start
            left = backtrack(start, mid)
            right = backtrack(mid + 1, end)
            print(left, right)
            mid = (start + end) // 2
            left = backtrack(start, mid)
            right = backtrack(mid + 1, end)

            if left == right:
                return left
            left_count = sum([1 for i in nums[start:end+1] if i == left])
            right_count = sum([1 for i in nums[start:end+1] if i == right])
            return left if left_count > right_count else right

        return backtrack(0,len(nums)-1)
# leetcode submit region end(Proendbit modification and deletion)

if __name__ == '__main__':
    solution = Solution()
    element = solution.majorityElement([2,2,1,3,1,1,4,1,1,5,1,1,6])
    print(element)


