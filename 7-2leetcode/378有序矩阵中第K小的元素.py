# 给定一个 n x n 矩阵，其中每行和每列元素均按升序排序，找到矩阵中第 k 小的元素。
# 请注意，它是排序后的第 k 小元素，而不是第 k 个不同的元素。
#
#
#
#  示例：
#
#  matrix = [
#    [ 1,  5,  9],
#    [10, 11, 13],
#    [12, 13, 15]
# ],
# k = 8,
#
# 返回 13。
#
#
#
#
#  提示：
# 你可以假设 k 的值永远是有效的，1 ≤ k ≤ n2 。
#  Related Topics 堆 二分查找
import heapq
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        自己写的垃圾代码
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        length = len(matrix)
        if length == 0:
            return None

        window = [[0, i[0]] for i in matrix]
        res = []
        while len(res) != k:
            min_num = window[0][1]
            min_index = 0
            for i, j in enumerate(window):
                if window[i][1] < min_num:
                    min_num = window[i][1]
                    min_index = i
            res.append(min_num)
            tmp = window[min_index]
            if tmp[0] + 1 > length - 1:
                window[min_index] = [tmp[0] + 1, float("inf")]
            else:
                window[min_index] = [tmp[0] + 1, matrix[min_index][tmp[0] + 1]]
        return res[-1]


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        """
        使用优先队列
        :param matrix:
        :param k:
        :return:
        """
        n = len(matrix)
        pq = [(matrix[i][0], i, 0) for i in range(n)]
        heapq.heapify(pq)

        ret = 0
        for i in range(k - 1):
            num, x, y = heapq.heappop(pq)
            if y != n - 1:
                heapq.heappush(pq, (matrix[x][y + 1], x, y + 1))

        return heapq.heappop(pq)[0]


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        def check(mid):
            i, j = n - 1, 0
            num = 0
            while i >= 0 and j < n:
                if matrix[i][j] <= mid:
                    num += i + 1
                    j += 1
                else:
                    i -= 1
            return num >= k

        left, right = matrix[0][0], matrix[-1][-1]
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1

        return left



# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    solution = Solution()
    matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
    k = 8
    res = solution.kthSmallest(matrix, k)
    print(res)