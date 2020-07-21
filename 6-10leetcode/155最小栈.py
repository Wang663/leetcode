# 设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。
#
#
#  push(x) —— 将元素 x 推入栈中。
#  pop() —— 删除栈顶的元素。
#  top() —— 获取栈顶元素。
#  getMin() —— 检索栈中的最小元素。
#
#
#
#
#  示例:
#
#  输入：
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]
#
# 输出：
# [null,null,null,null,-3,null,0,-2]
#
# 解释：
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> 返回 -3.
# minStack.pop();
# minStack.top();      --> 返回 0.
# minStack.getMin();   --> 返回 -2.
#
#
#
#
#  提示：
#
#
#  pop、top 和 getMin 操作总是在 非空栈 上调用。
#
#  Related Topics 栈 设计


# leetcode submit region begin(Prohibit modification and deletion)
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.minstack = []


    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.data.append(x)
        if not self.minstack or self.minstack[-1]>= x:
            self.minstack.append(x)


    def pop(self):
        """
        :rtype: None
        """
        if not self.data:
            return None
        if self.data[-1] == self.minstack[-1]:
            self.minstack.pop(-1)
        self.data.pop(-1)


    def top(self):
        """
        :rtype: int
        """
        if not self.data:
            return None
        return self.data[-1]


    def getMin(self):
        """
        :rtype: int
        """
        if not self.minstack:
            return None
        return self.minstack[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    print([] is True)