# 在一个 2 x 3 的板上（board）有 5 块砖瓦，用数字 1~5 来表示, 以及一块空缺用 0 来表示.
#
#  一次移动定义为选择 0 与一个相邻的数字（上下左右）进行交换.
#
#  最终当板 board 的结果是 [[1,2,3],[4,5,0]] 谜板被解开。
#
#  给出一个谜板的初始状态，返回最少可以通过多少次移动解开谜板，如果不能解开谜板，则返回 -1 。
#
#  示例：
#
#
# 输入：board = [[1,2,3],[4,0,5]]
# 输出：1
# 解释：交换 0 和 5 ，1 步完成
#
#
#
# 输入：board = [[1,2,3],[5,4,0]]
# 输出：-1
# 解释：没有办法完成谜板
#
#
#
# 输入：board = [[4,1,2],[5,0,3]]
# 输出：5
# 解释：
# 最少完成谜板的最少移动次数是 5 ，
# 一种移动路径:
# 尚未移动: [[4,1,2],[5,0,3]]
# 移动 1 次: [[4,1,2],[0,5,3]]
# 移动 2 次: [[0,1,2],[4,5,3]]
# 移动 3 次: [[1,0,2],[4,5,3]]
# 移动 4 次: [[1,2,0],[4,5,3]]
# 移动 5 次: [[1,2,3],[4,5,0]]
#
#
#
# 输入：board = [[3,2,4],[1,5,0]]
# 输出：14
#
#
#  提示：
#
#
#  board 是一个如上所述的 2 x 3 的数组.
#  board[i][j] 是一个 [0, 1, 2, 3, 4, 5] 的排列.
#
#  Related Topics 广度优先搜索


# leetcode submit region begin(Prohibit modification and deletion)
from queue import PriorityQueue
import copy


class Solution(object):
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        step = {0: [1, 3], 1: [0, 2, 4], 2: [1, 5], 3: [0, 4], 4: [1, 3, 5], 5: [4, 2]}
        visited,step_num = set(), 0
        cur_list,next_list = [''.join([str(j) for i in board for j in i])],[]
        while cur_list:
            for elem in cur_list:
                if elem == "123450":
                    return step_num
                elem = list(elem)
                print(elem)
                index = elem.index("0")
                print(index)
                for i in step[index]:
                    tmp = elem[:]
                    tmp[i],tmp[index] = tmp[index],tmp[i]
                    tmp_str = "".join(tmp)
                    if tmp_str not in visited:
                        visited.add(tmp_str)
                        next_list.append(tmp_str)
            step_num+=1
            cur_list = next_list
            next_list = []
        return -1




if __name__ == '__main__':
    solution = Solution()
    res = solution.slidingPuzzle([[3,2,4],[1,5,0]])
    print(res)
# leetcode submit region end(Prohibit modification and deletion)


# (3, 2, 4, 1, 0, 5) 1
# (3, 0, 4, 1, 2, 5) 2
# (3, 4, 0, 1, 2, 5) 3
# (3, 4, 5, 1, 2, 0) 4
# (3, 4, 5, 1, 0, 2) 5
# (3, 0, 5, 1, 4, 2) 6
# (0, 3, 5, 1, 4, 2) 7
# (1, 3, 5, 0, 4, 2) 8
# (1, 3, 5, 4, 0, 2) 9
# (1, 3, 5, 4, 2, 0) 10
# (1, 3, 0, 4, 2, 5) 11
# (1, 0, 3, 4, 2, 5) 12
# (1, 2, 3, 4, 0, 5) 13
# (1, 2, 3, 4, 5, 0) 14