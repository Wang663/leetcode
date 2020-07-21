# 班上有 N 名学生。其中有些人是朋友，有些则不是。他们的友谊具有是传递性。如果已知 A 是 B 的朋友，B 是 C 的朋友，那么我们可以认为 A 也是 C
# 的朋友。所谓的朋友圈，是指所有朋友的集合。
#
#  给定一个 N * N 的矩阵 M，表示班级中学生之间的朋友关系。如果M[i][j] = 1，表示已知第 i 个和 j 个学生互为朋友关系，否则为不知道。你
# 必须输出所有学生中的已知的朋友圈总数。
#
#  示例 1:
#
#
# 输入:
# [[1,1,0],
#  [1,1,0],
#  [0,0,1]]
# 输出: 2
# 说明：已知学生0和学生1互为朋友，他们在一个朋友圈。
# 第2个学生自己在一个朋友圈。所以返回2。
#
#
#  示例 2:
#
#
# 输入:
# [[1,1,0],
#  [1,1,1],
#  [0,1,1]]
# 输出: 1
# 说明：已知学生0和学生1互为朋友，学生1和学生2互为朋友，所以学生0和学生2也是朋友，所以他们三个在一个朋友圈，返回1。
#
#
#  注意：
#
#
#  N 在[1,200]的范围内。
#  对于所有学生，有M[i][i] = 1。
#  如果有M[i][j] = 1，则有M[j][i] = 1。
#
#  Related Topics 深度优先搜索 并查集


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        parent = [-1 for i in range(len(M))]

        def union(i, j):
            i_root = find(i)
            j_root = find(j)
            if i_root != j_root:
                parent[i_root] = j_root
            print(parent)

        def find(i):
            if parent[i] == -1:
                return i
            return find(parent[i])

        for i in range(len(M)):
            for j in range(len(M)):
                if M[i][j] == 1 and i != j:
                    union(i, j)
        count = 0
        print(parent)
        for i in parent:
            if i == -1:
                count += 1
        return count


if __name__ == '__main__':
    solution = Solution()
    M = [[1,1,0],
     [1,1,1],
     [0,1,1]]
    res = solution.findCircleNum(M)
    print(res)
# leetcode submit region end(Prohibit modification and deletion)
