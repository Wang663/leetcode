# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
#
#  ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
#
#  请找出其中最小的元素。
#
#  你可以假设数组中不存在重复元素。
#
#  示例 1:
#
#  输入: [3,4,5,1,2]
# 输出: 1
#
#  示例 2:
#
#  输入: [4,5,6,7,0,1,2]
# 输出: 0
#  Related Topics 数组 二分查找


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # If the list has just one element then return that element.
        if len(nums) == 1:
            return nums[0]
        left = 0
        right = len(nums) - 1
        if nums[right] > nums[0]:
            return nums[0]
        while right >= left:
            mid = left + (right - left) // 2
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            if nums[mid] > nums[0]:
                left = mid + 1
            else:
                right = mid - 1



class Solution(object):
    def findMin(self, nums):
        if not nums:
            return None
        l = 0
        r = len(nums)-1
        while l <= r:
            if l == r:
                return nums[l]
            mid = (l + r) // 2
            # print(mid)
            if nums[mid] > nums[0]:
                l = mid + 1
            elif nums[mid] < nums[-1]:
                r = mid - 1





# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    solution = Solution()
    res = solution.findMin([4, 5, 6, 7, 0, 1, 2])
    print(res)
